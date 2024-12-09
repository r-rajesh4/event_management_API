from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .models import User,Event,Ticket
from .serializers import UserSerializer,EventSerializer,TicketSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # In practice, hash the password here
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_event(request):
    if request.user.role != 'admin':
        return Response({"error": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        total_tickets = request.data.get('total_tickets')
        if total_tickets <=0:
            return Response({'detail': 'Not enough tickets are Enter.'}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_events(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)





@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])  # Ensures the user is authenticated
def purchase_ticket(request, event_id):
    user = request.user

    # Get the event directly, relying on Django's ORM to handle potential exceptions
    event = Event.objects.get(id=event_id)
    print(event)

    # Check if the event has available tickets
    available_tickets = event.total_tickets - event.tickets_sold
    quantity = request.data.get('quantity')

    if quantity <= 0:
        return Response({'detail': 'Quantity must be greater than 0.'}, status=status.HTTP_400_BAD_REQUEST)

    # Validate if the requested quantity would exceed the available tickets
    if quantity > available_tickets:
        return Response({'detail': 'Not enough tickets available.'}, status=status.HTTP_400_BAD_REQUEST)

    # Proceed with ticket creation and event update
    ticket = Ticket.objects.create(user=user, event=event, quantity=quantity)

    # Update the `tickets_sold` count in the Event model and save
    event.tickets_sold=quantity
    event.save()

    # Return the response with ticket details
    return Response(TicketSerializer(ticket).data, status=status.HTTP_201_CREATED)
from rest_framework import serializers
from .models import User, Event, Ticket

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

    def validate(self, data):
        event = data['event']
        quantity = data['quantity']
        if event.tickets_sold + quantity > event.total_tickets:
            raise serializers.ValidationError("Not enough tickets available")
        return data

    def create(self, validated_data):
        event = validated_data['event']
        quantity = validated_data['quantity']
        
        # Update tickets_sold in the event
        event.tickets_sold += quantity
        print(event.tickets_sold)
        event.save()

        # Create the ticket
        ticket = Ticket.objects.create(**validated_data)
        return ticket

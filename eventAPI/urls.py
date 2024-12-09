# urls.py
from django.urls import path
from .views import UserRegisterView, EventListView, TicketPurchaseView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('events/', EventListView.as_view(), name='event-list'),
    path('events/<int:id>/purchase/', TicketPurchaseView.as_view(), name='ticket-purchase'),
]

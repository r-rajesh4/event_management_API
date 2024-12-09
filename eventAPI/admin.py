from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Event, Ticket

# Register the User model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'role')  # Display these fields in the list view
    search_fields = ('username',)  # Add search functionality for username
    list_filter = ('role',)  # Filter by role

# Register the Event model
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'total_tickets', 'tickets_sold')  # Display these fields in the list view
    search_fields = ('name',)  # Add search functionality for event name
    list_filter = ('date',)  # Filter by event date

# Register the Ticket model
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'event', 'quantity', 'purchase_date')  # Display these fields in the list view
    search_fields = ('user__username', 'event__name')  # Add search functionality for user and event name
    list_filter = ('purchase_date',)  # Filter by purchase date

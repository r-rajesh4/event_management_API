from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user),
    path('events/', views.create_event),
    path('eventsList/', views.get_events),
    path('events/<int:event_id>/purchase/', views.purchase_ticket),
]
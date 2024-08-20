# events/views.py
from rest_framework import viewsets
from .models import Event, Booking
from .serializers import EventSerializer, BookingSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer




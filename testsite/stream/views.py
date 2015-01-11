from django.shortcuts import render
from stream.models import Stream
from django.http import HttpResponse

# Create your views here.


def stream(request):
    stream_items = Stream.objects.all()
    return render(request, 'stream.html', {'stream':stream_items})
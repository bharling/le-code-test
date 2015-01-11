from django.shortcuts import render
from stream.models import Stream
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.


def stream(request):
    stream_items = Stream.objects.filter( Q ( photo__deleted=False ) | Q  (tweet__deleted=False )   )
    return render(request, 'stream.html', {'stream':stream_items})
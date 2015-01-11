from django.shortcuts import render
from stream.models import Stream
from django.http import HttpResponse

# Create your views here.


def stream(request):
    #return HttpResponse('ok')
    stream_items = Stream.objects.filter(photo__deleted=False, tweet__deleted=False)
    return render(request, 'stream.html', {stream:stream_items})
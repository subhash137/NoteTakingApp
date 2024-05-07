from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NoteSerializer
from .models import Note

@api_view(['GET'])
def getroute(request):
    routes = [
        {
            'Endpoint':'/notes/',
            'method':'GET',
            'body':None,
            'description':'Returns an array of notes',
        },
        {
            'Endpoint':'/notes/id',
            'method':'GET',
            'body':None,
            'description':'Returns a single note object',
        },
        {
            'Endpoint':'/notes/create/',
            'method':'POST',
            'body':{'body':""},
            'description':'Creates new note with data sent in post request'
        }

    ]
    return Response(routes)

@api_view(['GET'])
def getnotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getnote(request,pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes, many=False)
    return Response(serializer.data)
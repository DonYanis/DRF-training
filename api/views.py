from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Note
from .serializers import NoteSerializer
from . import utils
 
@api_view(['GET'])
def getRoutes(request):
    
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET, POST',
            'body':{'body': ""}
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET, DELETE, PUT',
            'body': {'body': ""},
        }
    ]
    
    return Response(routes)


@api_view(['GET','POST'])
def getNotes(request):

    if request.method == 'GET':
        return utils.getAllNotes(request)

    elif request.method == 'POST':
        return utils.createNote(request)


@api_view(['GET','PUT','DELETE'])
def getNote(request,pk):

    if request.method == 'GET':
        return utils.getNote(request, pk)

    elif request.method == 'PUT':
        return utils.updateNote(request, pk)

    elif request.method == 'DELETE':
        return utils.deleteNote(request, pk)

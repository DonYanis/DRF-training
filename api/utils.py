from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note


def getAllNotes(request):
    notes = Note.objects.all().order_by('-updated')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

def createNote(request):
    data  = request.data
    note = Note.objects.create(body = data['body'])
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

def getNote(request,pk):
    note = Note.objects.filter(id=pk).first()
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

def updateNote(request,pk):
    data  = request.data
    note = Note.objects.filter(id=pk).first()
    serializer = NoteSerializer(instance = note,data = data) #updating

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

def deleteNote(request,pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('delete OK!')
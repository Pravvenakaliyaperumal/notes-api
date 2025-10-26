from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Note
from .permissions import IsOwnerOrReadOnly
from rest_framework import filters

from .serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('-created_at')  # Order by creation date, newest first
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user).order_by('-created_at')



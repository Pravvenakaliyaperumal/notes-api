from rest_framework import serializers

from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'  # This will include all fields of the Note model (title, content, created_at)
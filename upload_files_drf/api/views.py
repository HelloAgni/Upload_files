from rest_framework import generics, status, viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from .models import File
from .serializers import FileSerializer
from .tasks import upload


class FileViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Check all or single File objects.
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer


class FileUploadView(generics.CreateAPIView):
    """
    Upload File.
    Simulate long process with 10 sec delay.
    """
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = FileSerializer

    def perform_create(self, serializer, format=None):
        if serializer.is_valid():
            file_obj = serializer.save()
            upload.delay(file_obj.id)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

import re

from rest_framework import serializers

from .models import File


class FileSerializer(serializers.ModelSerializer):
    """
    File Serializer.
    Response 'processed' with normal human format.
    """
    # uploaded_at = serializers.DateTimeField(format='%m.%d.%Y %H:%m:%S')

    class Meta:
        model = File
        fields = ['id', 'file', 'uploaded_at', 'processed']
        read_only_fields = ['processed']

    def to_representation(self, instance):
        """Replace 'T' and 'Z' from datetime."""
        ret = super().to_representation(instance)
        new = ret.get('uploaded_at')
        if new:
            ret['uploaded_at'] = re.sub('[TZ]', ' ', new[:-8])
        return ret

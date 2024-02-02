from django.db import models


class File(models.Model):
    file = models.FileField('File', upload_to='files/')
    uploaded_at = models.DateTimeField('Upload date', auto_now_add=True)
    processed = models.BooleanField('Processed', default=False)

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'
        ordering = ['uploaded_at']

    def __str__(self):
        return str(self.uploaded_at.date())

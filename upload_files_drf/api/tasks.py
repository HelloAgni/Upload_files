import time

from celery import shared_task

from .models import File

TIME_DELAY = 10


@shared_task
def upload(id):
    time.sleep(TIME_DELAY)  # Simulate slow process...
    file = File.objects.get(id=id)
    file.processed = True
    file.save()
    return 'Done!'

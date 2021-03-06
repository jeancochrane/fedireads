''' background tasks '''
import os
from celery import Celery

from fedireads import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fr_celery.settings')
app = Celery(
    'tasks',
    broker=settings.CELERY_BROKER,
)

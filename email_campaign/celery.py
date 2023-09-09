import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

app = Celery('email_campaign')
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Kolkata')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'run-campaigns-daily': {
        'task': 'email_campaign.tasks.run_campaigns_daily',
        'schedule': crontab(minute="*"),  # Schedule to run daily at midnight
    },
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
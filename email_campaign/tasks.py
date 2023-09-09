from celery import shared_task
from django.core.management import call_command


@shared_task(bind=True)
def run_campaigns_daily(self):
    call_command('create_campaigns')

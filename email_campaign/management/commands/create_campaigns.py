from django.core.management.base import BaseCommand
from email_campaign.models import Subscriber, Campaign
from django.core.mail import send_mail
from django.template.loader import get_template
from datetime import date
class Command(BaseCommand):
    help = 'create daily campaigns to send subscribers.'

    def handle(self, *args, **options):
        subscribers = Subscriber.objects.filter(is_active=True).values_list('email')
        recipient_list = []
        for email in subscribers:
            recipient_list.append(email[0])

        today = date.today()
        campaigns = Campaign.objects.filter(published_date=today).values()

        if campaigns:
            for campaign in campaigns:
                self.stdout.write(self.style.SUCCESS(f'Sending campaign: {campaign.get("subject")}'))
                subject = campaign.get('subject')

                email_from = 'example@gmail.com'
                html_template = get_template('custom_email_template.html').render(campaign)

                send_mail(subject,None,email_from,recipient_list,fail_silently=False,html_message=html_template)
        else:
            self.stdout.write(self.style.SUCCESS('No campaigns scheduled for today.'))





from django.core.management.base import BaseCommand
from email_campaign.models import Subscriber, Campaign
from django.core.mail import send_mail
from datetime import date

class Command(BaseCommand):
    help = 'create daily campaigns to send subscribers.'

    def handle(self, *args, **options):
        subscribers = Subscriber.objects.filter(is_active=True).values_list('email')
        #print(len(subscribers), subscribers[0][0])
        recipient_list = []
        for email in subscribers:
            recipient_list.append(email[0])

        # print(email_list)

        today = date.today()
        campaigns = Campaign.objects.filter(published_date=today).values()
        #print(len(campaigns), campaigns[0].get('html_content'))

        if campaigns:
            for campaign in campaigns:
                self.stdout.write(self.style.SUCCESS(f'Sending campaign: {campaign.get("subject")}'))
                subject = campaign.get('subject')
                message = campaign.get('plain_text_content')
                email_from = 'raj@gmail.com'
                send_mail(subject,message,email_from,recipient_list,fail_silently=False)
        else:
            self.stdout.write(self.style.SUCCESS('No campaigns scheduled for today.'))





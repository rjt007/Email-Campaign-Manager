from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Subscriber,Campaign
from .serializers import SubscriberSerializer, CampaignSerializer


#Subscriber ViewSet
class SubscriberViewSet(viewsets.ModelViewSet):   
        queryset = Subscriber.objects.all()
        serializer_class = SubscriberSerializer
        
        @action(details=True, method=['post'])
        def unsubscribe(self, request, pk=None):
                try:
                    subscriber = self.get_object()
                    subscriber.is_active = False
                    subscriber.save()
                    return Response({'message':'user unsubscribed succesfully!'}, status = status.HTTP_200_OK)
                except Exception as e:
                    return Response({'error':e},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#Campaign ViewSet
class CampaignViewSet(viewsets.ModelViewSet):
        queryset = Campaign.objects.all()
        serializer_class = CampaignSerializer

        @action(details=False, method=['post'])
        def send_daily_campagin(self,request):
              pass


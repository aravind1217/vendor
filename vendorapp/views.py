from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import *
from .models import *
from .serializers import *
from django.utils.timezone import now

from rest_framework.response import Response
from django.utils import timezone
from django.db.models import Avg
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status

class VendorListCreateView(generics.ListCreateAPIView):

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class PurchaseOrderListCreateView(generics.ListCreateAPIView):

    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):

    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class VendorPerformanceView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        performance_data = {
            'on_time_delivery_rate': serializer.data.get('on_time_delivery_rate', 0),
            'quality_rating_avg': serializer.data.get('quality_rating_avg', 0),
            'average_response_time': serializer.data.get('average_response_time', 0),
            'fulfillment_rate': serializer.data.get('fulfillment_rate', 0),
        }

        return Response(performance_data)




class AcknowledgePurchaseOrderView(generics.UpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.acknowledgment_date = request.data.get('acknowledgment_date', now())
        instance.save()

        response_times = PurchaseOrder.objects.filter(vendor=instance.vendor, acknowledgment_date__isnull=False).values_list('acknowledgment_date', 'issue_date')
        average_response_time = sum((ack_date - issue_date).total_seconds() for ack_date, issue_date in response_times) / len(response_times) if response_times else 0

        instance.vendor.average_response_time = average_response_time
        instance.vendor.save()

        return Response({'acknowledgment_date': instance.acknowledgment_date})
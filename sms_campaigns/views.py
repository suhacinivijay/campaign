# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Phonebook, Contacts, SMSReports, Campaign
import sms
from . import serializers
from rest_framework import viewsets, status
from rest_framework.response import Response


class PhonebookViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.PhonebookSerializer
    queryset = Phonebook.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactsViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.ContactSerializer
    queryset = Contacts.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CampaignViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.CampaignSerializer
    queryset = Campaign.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            phonebook_id = serializer.data['phonebook_id']
            all_contacts = Contacts.objects.values_list('contact_no', flat=True).filter(phonebook_id=phonebook_id[0])
            print all_contacts
            sms.send_bulk_sms()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReportViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.SMSReports
    queryset = SMSReports.objects.all()




# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Phonebook, Contacts, SMSReports
from phonebook import Contacts
from campaign import Campaign
import sms
from . import serializers
from rest_framework import viewsets, status
from rest_framework.response import Response


from django.shortcuts import render

#Using dict instead of model
# contacts = {
#     1: Contacts(phonebook_id=1, contact_name='suha', contact_number=9181055333)
# }

contacts = ['918105533307', '918105533307']

campaigns = {
    1: Campaign(campaign_id=1, campaign_name='Test', user_id ='1', type='sms', phonebook_id='1')
}

'''{ message_uuid : status}'''
sms_reports = {

}
# Create your views here.


def get_all_contacts():
    contact = contacts.values()
    pass


def add_reports(response):
    message_uuids = response['message_uuid']
    status = response['message']
    for msg_uuid in message_uuids:
        sms_reports[msg_uuid] = status
    # invalid_numbers = response['invalid_number']
    # for num in invalid_numbers:
    #     sms_reports[]


def get_camp_id():
    return max(campaigns) + 1


class ContactViewSet(viewsets.ViewSet):
    # Required for the Browsable API renderer to have a nice form.
    serializer_class = serializers.ContactSerializer

    def list(self, request):
        serializer = serializers.ContactSerializer(
            instance=contacts.values(), many=True)
        return Response(serializer.data)


class CampaignViewSet(viewsets.ViewSet):
    serializer_class = serializers.CampaignSerializer

    def list(self, request):
        serializer = serializers.CampaignSerializer(
            instance=campaigns.values(), many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = serializers.CampaignSerializer(data=request.data)
        msg = request.data['message']
        if serializer.is_valid():
            camp = serializer.save()
            camp.id = get_camp_id()
            campaigns[camp.id] = camp
            response = sms.send_bulk_sms(contacts, msg)
            add_reports(response)
            # sms.add_response(response)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# class ReportViewSet(viewsets.ViewSet):
#     serializer_class = serializers.SMSReportSerializer

# @csrf_exempt
# def campaign(request):
#     if request.method == 'POST':
#         if isinstance(campaign_name, str) and phonebook.check_valid_phonebook_id(phonebook_id):
#             all_contacts = contacts.get_all_contacts(phonebook_id)
#             response = sms.send_bulk_sms(all_contacts)
#             '''response sms'''
#             return response
#     if request.method == 'GET':
#         '''campaign details'''
#         pass
#
# @csrf_exempt
# def campaign_callback(request):
#     if request.method == 'POST':
#         '''requires async call to save all message_uuid/ this post should not block other requests'''
#         message_uuids = response['message_uuid']
#         for uuid in response['message_uuid']:
#             sms_reports.update_message_uuid(uuid)
#         for i in response['invalid_numbers']:
#             sms_reports.invalid_numbers()





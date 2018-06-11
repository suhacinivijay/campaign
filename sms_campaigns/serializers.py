from rest_framework import serializers
from models import Phonebook, Campaign, Contacts, SMSReports


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contacts
        queryset = Contacts.objects.all()
        fields = '__all__'


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        queryset = Campaign.objects.all()
        fields = '__all__'


class PhonebookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phonebook
        queryset = Phonebook.objects.all()
        fields = '__all__'


class SMSReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = SMSReports
        queryset = SMSReports.objects.all()
        fields = '__all__'

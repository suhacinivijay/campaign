from rest_framework import serializers
from phonebook import Contacts
from campaign import Campaign


class ContactSerializer(serializers.Serializer):
    phonebook_id = serializers.IntegerField()
    contact_name = serializers.CharField()
    contact_number = serializers.IntegerField()

    def create(self, validated_data):
        return Contacts(phonebook_id=None, **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance


class CampaignSerializer(serializers.Serializer):
    campaign_id = serializers.IntegerField()
    campaign_name = serializers.CharField()
    user_id = serializers.IntegerField()
    type = serializers.CharField()
    phonebook_id = serializers.IntegerField()
    message = serializers.CharField()

    def create(self, validated_data):
        return Campaign(**validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance


# class SMSReportSerializer(serializers.Serializer):
#     campaign_id = serializers.IntegerField()
#     contact_number = serializers.IntegerField()
#     status = serializers.CharField()
#     message_uuid = serializers.CharField()
#
#     def create(self, validated_data):
#         return

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Phonebook(models.Model):

    phonebook_id = models.IntegerField()
    phonebook_name = models.CharField(max_length=200)

    def check_valid_phonebook_id(self, id):
        if id == self.phonebook_id:
            return True
        else:
            return False


class Campaign(models.Model):
    campaign_id = models.IntegerField()
    campaign_name = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    phonebook_id = models.ForeignKey(Phonebook)
    message = models.CharField(max_length=200)


class Contacts:
    def __init__(self):
        self.phonebook_id = models.ManyToManyField(Phonebook)
        self.contact_name = models.IntegerField()
        self.contact_no = models.IntergerField()

    def get_all_contacts(self, phonebook_id):
        '''query and return all contacts for particular phonebook id'''
        pass


class SMSReports:
    def __init__(self):
        self.campaign_id = models.ForeignKey(Campaign)
        self.contact_number = models.IntegerField()
        self.status = models.CharField(max_length=200)
        self.message_uuid = models.CharField(max_length=200)

    def update_message_uuid(self, message_uuid):
        '''update the record with particular contact number'''

    def update_message_status(self, message_status):
        '''url given to plivo api to update message status'''

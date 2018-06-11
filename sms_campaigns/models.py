# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Phonebook(models.Model):

    phonebook_id = models.IntegerField()
    phonebook_name = models.CharField(max_length=200)

    # def check_valid_phonebook_id(self, id):
    #     if id == self.phonebook_id:
    #         return True
    #     else:
    #         return False


class Campaign(models.Model):
    campaign_id = models.IntegerField()
    campaign_name = models.CharField(max_length=200)
    user_id = models.IntegerField()
    type = models.CharField(max_length=200)
    phonebook_id = models.ManyToManyField(Phonebook)
    message = models.CharField(max_length=200)


class Contacts(models.Model):
    phonebook_id = models.ManyToManyField(Phonebook)
    contact_name = models.CharField(max_length=200)
    contact_no = models.IntegerField()


class SMSReports(models.Model):
    campaign_id = models.ForeignKey(Campaign)
    contact_number = models.IntegerField()
    status = models.CharField(max_length=200)
    message_uuid = models.CharField(max_length=200)


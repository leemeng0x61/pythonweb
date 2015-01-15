# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class DiguaUserApacheNotMacUntil2015(models.Model):
    id = models.IntegerField(primary_key=True)# Field name made lowercase.
    imei = models.CharField(db_column='IMEI', max_length=100, blank=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE', blank=True, null=True)  # Field name made lowercase.
    num = models.CharField(db_column='NUM', max_length=20, blank=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=30, blank=True)  # Field name made lowercase.
    resolution_id = models.IntegerField(db_column='RESOLUTION_ID', blank=True, null=True)  # Field name made lowercase.
    resolution_name = models.CharField(db_column='RESOLUTION_NAME', max_length=20, blank=True)  # Field name made lowercase.
    os_id = models.IntegerField(db_column='OS_ID', blank=True, null=True)  # Field name made lowercase.
    os_name = models.CharField(db_column='OS_NAME', max_length=20, blank=True)  # Field name made lowercase.
    version = models.CharField(db_column='VERSION', max_length=500, blank=True)  # Field name made lowercase.
    client_channel_id = models.CharField(db_column='CLIENT_CHANNEL_ID', max_length=100, blank=True)  # Field name made lowercase.
    client_channel_name = models.CharField(db_column='CLIENT_CHANNEL_NAME', max_length=500, blank=True)  # Field name made lowercase.
    device = models.CharField(db_column='DEVICE', max_length=500, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'digua_user_apache_not_mac_until_2015'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class ImeiDistinct(models.Model):
    imei = models.CharField(max_length=100)
    count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'imei_distinct'


class Imeidata(models.Model):
    imei = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'imeidata'

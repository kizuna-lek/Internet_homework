# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DormitoryNum(models.Model):
    dormitory_name = models.CharField(max_length=30)
    dormitory_num = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dormitory_num'


class Order(models.Model):
    stu_num = models.CharField(max_length=254, blank=True, null=True)
    dormitory_num = models.IntegerField()
    male = models.IntegerField()
    people_num = models.IntegerField()
    is_correct = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order'


class OrderInfo(models.Model):
    stu_num = models.IntegerField()
    room_name = models.CharField(max_length=30)
    room_mate1 = models.CharField(max_length=254)
    room_mate2 = models.CharField(max_length=254)
    room_mate3 = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'order_info'


class RoomNum(models.Model):
    dormitory_num = models.IntegerField()
    unit_num = models.IntegerField()
    room_name = models.CharField(max_length=30)
    male = models.IntegerField()
    all_beds = models.IntegerField()
    free_beds = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_num'


class RoomStuInfo(models.Model):
    room_id = models.IntegerField()
    room_name = models.CharField(max_length=30)
    room_mate1 = models.CharField(max_length=254)
    room_mate2 = models.CharField(max_length=254)
    room_mate3 = models.CharField(max_length=254)
    room_mate4 = models.CharField(max_length=254)
    room_mate5 = models.CharField(max_length=254)
    room_mate6 = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'room_stu_info'


class UnitNum(models.Model):
    dormitory_num = models.IntegerField(blank=True, null=True)
    unit_num = models.IntegerField()
    unit_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'unit_num'


class UserInfo(models.Model):
    stu_num = models.CharField(unique=True, max_length=254, blank=True, null=True)
    name = models.CharField(max_length=30)
    male = models.IntegerField()
    havedor = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_info'

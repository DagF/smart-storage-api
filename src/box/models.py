#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import uuid
from enum import Enum

from django.db.models import TextField, DateField, Model, CharField, ForeignKey, \
    DateTimeField, UUIDField, OneToOneField
from rest_framework.exceptions import ValidationError


class Box(Model):
    uuid = UUIDField(primary_key=False, unique=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=4)

    def __str__(self):
        return self.name


class RFID(Model):
    uuid = UUIDField(primary_key=False, unique=True, default=uuid.uuid4, editable=False)
    box = ForeignKey(Box)
    value = CharField(max_length=100)
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.box.name + " : " + self.value


class Activity(Model):
    uuid = UUIDField(primary_key=False, unique=True, default=uuid.uuid4, editable=False)
    box = ForeignKey(Box)
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.box.name

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import uuid
from enum import Enum

from django.db.models import TextField, DateField, Model, CharField, ForeignKey, \
    DateTimeField, UUIDField, OneToOneField, FloatField
from rest_framework.exceptions import ValidationError


class Box(Model):
    uuid = UUIDField(primary_key=False, unique=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=8, unique=True)
    description = CharField(max_length=500, null=True)

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


class Item(Model):
    uuid = UUIDField(primary_key=False, unique=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=100)
    rfid = CharField(max_length=100, null=True)
    description = CharField(max_length=500, null=True)
    created = DateTimeField(auto_now_add=True)
    weight = FloatField(null=True)
    empty_weight = FloatField(null=True)
    full_weight = FloatField(null=True)

    PART = 'PAR'
    CONTAINER = 'CON'
    TOOL = 'TOO'
    PROTOTYPE = 'PRO'
    TYPE_CHOICES = (
        (PART, 'Part'),
        (CONTAINER, 'Container'),
        (TOOL, 'Tool'),
        (PROTOTYPE, 'Prototype'),
    )
    type = CharField(
        max_length=3,
        choices=TYPE_CHOICES,
        default=PART,
    )

    def __str__(self):
        return self.name


class User(Model):
    uuid = UUIDField(primary_key=False, unique=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=100)
    rfid = CharField(max_length=100, null=True)
    created = DateTimeField(auto_now_add=True)


class Weight(Model):
    uuid = UUIDField(primary_key=False, unique=True, default=uuid.uuid4, editable=False)
    box = ForeignKey(Box)
    created = DateTimeField(auto_now_add=True)
    value = FloatField()

    def __str__(self):
        return self.box.name + " : " + str(self.value) + " Gram"

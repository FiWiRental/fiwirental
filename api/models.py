from datetime import datetime
from bson.objectid import ObjectId
from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    DateTimeField, ReferenceField, StringField, ObjectIdField
    , FileField, DateField, DecimalField, IntField, ListField, 
    EmailField, LazyReferenceField, ImageField, EmbeddedDocumentListField,
    EmbeddedDocumentField
)


class UploadedImages(EmbeddedDocument):
    meta = {'collection': 'images'}
    photos = StringField(required=True)


class BaseAddress(EmbeddedDocument):
    meta = {'collection': 'addresses'}
    lot_num = IntField(required=True)
    Street_name = StringField(required=True)
    Community = StringField()
    City = StringField(required=True)
    Parish = StringField(required=True)


class Vehicle(Document):
    meta = {'collection': 'vehicle'}
    chassis_num = StringField(primary_key=True,required=True, unique=True)
    photos = EmbeddedDocumentListField(UploadedImages)
    model = StringField()
    make = StringField()
    year = DateField()
    owner_id = StringField()
    transmission_type = StringField()
    Description = StringField()
    Price = DecimalField(required=True)   


class Person(Document):
    meta = {'collection': 'person'}
    uuid = StringField(primary_key=True, required=True) 
    idType = StringField(required=True)
    photo_id = StringField(required=True)
    name = StringField()
    age = IntField()
    dob = DateField()
    member_since = DateTimeField(default=datetime.now) 
    Description = StringField()
    address = EmbeddedDocumentField(BaseAddress)
    email_address = ListField(EmailField())
    phone_number = ListField(StringField())
    Language = ListField(StringField())
    Number_of_rentals = IntField()
    Rating = DecimalField()
    # vehicles_owned = ListField(LazyReferenceField(Vehicle), default=list)


class Rental(Document):
    meta = {'collection': 'rental'}
    rental_id = ObjectIdField(Primary_key=True,required=True, default=ObjectId)
    start_date = DateField(required=True)
    end_date = DateField(required=True)
    renter_id = LazyReferenceField(Person,required=True)
    vehicle_id = LazyReferenceField(Vehicle,required=True)
    address = EmbeddedDocumentField(BaseAddress)
    location_type = StringField(required=True)
    pickup_time = DateTimeField()
    dropoff_time = DateTimeField()

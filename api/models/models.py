from datetime import datetime
from bson.objectid import ObjectId
from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    DateTimeField, StringField, ObjectIdField
, DateField, DecimalField, IntField, ListField,
    EmailField, LazyReferenceField, EmbeddedDocumentListField,
    EmbeddedDocumentField
)


class UploadedImages(EmbeddedDocument):
    meta = {'collection': 'images'}
    photo_url = StringField(required=True)


class BaseAddress(EmbeddedDocument):
    meta = {'collection': 'addresses'}
    lot_num = IntField(required=True)
    Street_name = StringField(required=True)
    community = StringField()
    City = StringField(required=True)
    Parish = StringField(required=True)


class Person(Document):
    meta = {'collection': 'person'}
    uuid = StringField(primary_key=True, required=True) 
    idType = StringField(required=True)
    photo_id = EmbeddedDocumentField(UploadedImages)
    name = StringField()
    age = IntField()
    dob = DateField()
    member_since = DateTimeField(default=datetime.now)
    description = StringField()
    address = EmbeddedDocumentField(BaseAddress)
    email_address = ListField(EmailField())
    phone_number = ListField(StringField())
    language = ListField(StringField())
    number_of_rentals = IntField()
    rating = DecimalField()
    # vehicles_owned = ListField(LazyReferenceField(Vehicle), default=list)


class Vehicle(Document):
    meta = {'collection': 'vehicle'}
    chassis_num = StringField(primary_key=True, required=True, unique=True)
    photos = EmbeddedDocumentListField(UploadedImages)
    model = StringField()
    make = StringField()
    year = DateField()
    owner_id = StringField(LazyReferenceField(Person))
    transmission_type = StringField()
    description = StringField()
    price = DecimalField(required=True)


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

"""Populating the database with dummy data to start working with.
 We can probably extend it's use to something else though"""

import os

from mongoengine import connect

from Models.models import Vehicle, Person, UploadedImages, BaseAddress


connect(os.getenv("MONGODB_DATABASE"), host=os.getenv("MONGODB_CONNECTION_STRING"), alias='default')


def init_db():

    # Create the fixtures
    addr = BaseAddress(lot_num=80, street_name="Brooklyn Ave", community="Greendale", city="Spanish Town",
                       parish="St.Catherine")
    person_pics = UploadedImages(photo_url='www.amazons3.com/upload-test/test-image.jpg')
    me = Person()
    me.uuid = "123-456-789"
    me.idType = "TRN"
    me.photo_id = person_pics
    me.name = 'Danielle Jackson'
    me.age = 20
    me.dob = '10/10/1999'
    me.description = "An Anime lover and local weeboo specialist"
    me.email_address = ["dkjackson@gmail.com"]
    me.language = ["English"]
    me.address = addr
    # me.photo_id.replace(customer_image, filename="man-img.png", content_type='image/jpg')
    me.save()

    vehicle_pics = UploadedImages(photo_url="www.amazons3.com/upload-test/test-image.jpg")
    mazda = Vehicle()
    mazda.chassis_num = "1233456677"
    mazda.photos = [vehicle_pics]
    mazda.model = "RX7"
    mazda.owner_id = me.uuid
    mazda.make = "Mazda"
    mazda.year = "01/01/1994"
    mazda.transmission_type = "Manual"
    mazda.description = "Initial-D anyone?"
    mazda.price = 1011.98
    mazda.save()

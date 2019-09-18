"""Populating the database with dummy data to start working with.
 We can probably extend it's use to something else though"""

import os

from mongoengine import connect

from models import Vehicle, Person, UploadedImages


connect(os.getenv("MONGODB_DATABASE"), host=os.getenv("MONGODB_CONNECTION_STRING"), alias='default')

def init_db():

    # Create the fixtures
    with open('test-images/man.png','rb') as customer_image:
        me = Person(uuid="123-456-789",name='Daniel Jackson',age=20,dob='10/10/1999',Description="An Anime lover and local weeboo specialist",
        email_address=["dkjackson@gmail.com"],Language=["English"], lot_num=80,Street_name="Brooklyn Ave",
        City="Spanish Town",Parish="St. Catherine")
        me.photo_id.replace(customer_image, filename="man-img.png", content_type='image/jpg')
        me.save()

    vehicle_img_1 = UploadedImages()
    with open('test-images/mazda-1.jpg','rb') as vehicle_image:
        vehicle_img_1.photos.replace(vehicle_image, filename="mazda.jpg", content_type='image/jpg')

    vehicle_img_2 = UploadedImages()
    with open('test-images/mazda-2.jpg','rb') as vehicle_image:
        vehicle_img_2.photos.replace(vehicle_image, filename="mazda-second.jpg", content_type='image/jpg')

    mazda = Vehicle(model="RX7",owner_id=me.uuid, make="Mazda",year="01/01/1994",
     transmission_type="Manual", Description="Intial-D anyone?",Price=1011.98)
    mazda.photos.append(vehicle_img_1)
    mazda.photos.append(vehicle_img_2)
    mazda.save()

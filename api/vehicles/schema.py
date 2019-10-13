import graphene

from Models.models import Vehicle, UploadedImages


class CreateVehicleEntry(graphene.Mutation):
    chassis_num = graphene.String()
    photo_url = graphene.String()
    model = graphene.String()
    make = graphene.String()
    year = graphene.Date()
    owner_id = graphene.String()
    transmission_type = graphene.String()
    description = graphene.String()
    price = graphene.Float()

    class Arguments:
        chassis_num = graphene.String()
        photo_url = graphene.List(graphene.String)
        model = graphene.String()
        make = graphene.String()
        year = graphene.Date()
        owner_id = graphene.String()
        transmission_type = graphene.String()
        description = graphene.String()
        price = graphene.Float()

    @staticmethod
    def mutate(self, info, chassis_num, photo_url, model, make, year, owner_id, transmission_type, description, price):
        vehicle_images = UploadedImages(photo_url=photo_url)
        vehicle = Vehicle(chassis_num=chassis_num, model=model, make=make, year=year, owner_id=owner_id,
                          transmission_type=transmission_type, description=description, price=price)
        vehicle.photo_url = vehicle_images
        # print(type(vehicle_images))
        print(vehicle_images.photo_url)
        vehicle.save()
        return CreateVehicleEntry(
            chassis_num=Vehicle.chassis_num,
            photo_url=Vehicle.photo_url,
            model=Vehicle.model,
            make=Vehicle.make,
            year=Vehicle.year,
            owner_id=Vehicle.owner_id,
            transmission_type=Vehicle.transmission_type,
            description=Vehicle.description,
            price=Vehicle.price
        )
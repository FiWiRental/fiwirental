import graphene

from Models.models import Vehicle, UploadedImages


class CreateVehicleEntry(graphene.Mutation):
    chassis_num = graphene.String()
    photos = graphene.String()
    model = graphene.String()
    make = graphene.String()
    year = graphene.Date()
    owner_id = graphene.String()
    transmission_type = graphene.String()
    description = graphene.String()
    price = graphene.Decimal()

    class Arguments:
        chassis_num = graphene.String()
        photos = graphene.String()
        model = graphene.String()
        make = graphene.String()
        year = graphene.Date()
        owner_id = graphene.String()
        transmission_type = graphene.String()
        description = graphene.String()
        price = graphene.Decimal()

    def mutate(self, info, chassis_num, photos, model, make, year, owner_id, transmission_type, description, price):
        vehicle_images = UploadedImages(photo_url=photos)
        vehicle = Vehicle(chassis_num=chassis_num, model=model, make=make, year=year, owner_id=owner_id,
                          transmission_type=transmission_type, description=description, price=price)
        vehicle.photos = vehicle_images
        vehicle.save()
        return CreateVehicleEntry(
            chassis_num=Vehicle.chassis_num,
            photos=Vehicle.photos,
            model=Vehicle.model,
            make=Vehicle.make,
            year=Vehicle.year,
            owner_id=Vehicle.owner_id,
            transmission_type=Vehicle.transmission_type,
            description=Vehicle.description,
            price=Vehicle.price
        )
import graphene

from Models.models import Person, BaseAddress, UploadedImages


class CreateCustomer(graphene.Mutation):
    uuid = graphene.String()
    idtype = graphene.String()
    photo_id = graphene.String()
    name = graphene.String()
    age = graphene.Int()
    dob = graphene.Date()
    member_since = graphene.DateTime()
    description = graphene.String()
    lot_num = graphene.Int()
    street_name = graphene.String()
    community = graphene.String()
    city = graphene.String()
    parish = graphene.String()
    email_address = graphene.List(graphene.String)
    phone_number = graphene.List(graphene.String)
    language = graphene.List(graphene.String)
    number_of_rentals = graphene.Int()
    rating = graphene.Decimal()

    class Arguments:
        uuid = graphene.String()
        idtype = graphene.String()
        name = graphene.String()
        photo_id = graphene.String()
        age = graphene.Int()
        dob = graphene.Date()
        description = graphene.String()
        lot_num = graphene.Int()
        street_name = graphene.String()
        community = graphene.String()
        city = graphene.String()
        parish = graphene.String()
        email_address = graphene.List(graphene.String)
        phone_number = graphene.List(graphene.String)
        language = graphene.List(graphene.String)

    @staticmethod
    def mutate(self, info, uuid, idtype, name, photo_id, age, dob, description, lot_num, street_name, community, city,
               parish,
               email_address, phone_number, language):
        person_photo = UploadedImages(photo_url=photo_id)
        addr = BaseAddress(lot_num=lot_num, street_name=street_name, community=community, city=city, parish=parish)
        customer = Person(uuid=uuid, idtype=idtype, name=name, age=age, dob=dob, description=description,
                          email_address=email_address, phone_number=phone_number, language=language)
        customer.photo_id = person_photo
        customer.address = addr
        customer.save()
        return CreateCustomer(
            uuid=customer.uuid,
            idtype=customer.idtype,
            name=customer.name,
            photo_id=customer.photo_id.photo_url,
            age=customer.age,
            dob=customer.dob,
            description=customer.description,
            lot_num=customer.address.lot_num,
            street_name=customer.address.street_name,
            community=customer.address.community,
            city=customer.address.city,
            parish=customer.address.parish,
            email_address=customer.email_address,
            phone_number=customer.phone_number,
            language=customer.language
        )
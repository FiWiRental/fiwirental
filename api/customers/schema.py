import graphene

from Models.models import Person, BaseAddress, UploadedImages


class CreateCustomer(graphene.Mutation):
    pid = graphene.ID()
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
    email_address = graphene.List()
    phone_number = graphene.List()
    language = graphene.List()
    number_of_rentals = graphene.Int()
    rating = graphene.Decimal()

    class Arguments:
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
        """Work and read up on the below attributes"""
        email_address = graphene.List()
        phone_number = graphene.List()
        language = graphene.List()

    def mutate(self, info, name, photo_id, age, dob, description, lot_num, street_name, community, city, parish,
               email_address, phone_number, language):
        person_photo = UploadedImages(photo_url=photo_id)
        addr = BaseAddress(lot_num=lot_num, street_name=street_name, community=community, city=city, parish=parish)
        customer = Person(name=name, age=age, dob=dob, description=description,
                          email_address=email_address, phone_number=phone_number, language=language)
        customer.photo_id = person_photo
        customer.address = addr
        customer.save()
        return CreateCustomer(
            name=customer.name,
            photo_id=customer.photo_id,
            age=customer.age,
            dob=customer.dob,
            description=customer.description,
            address=customer.address,
            email_address=customer.email_address,
            phone_number=customer.phone_number,
            Language=customer.language
        )
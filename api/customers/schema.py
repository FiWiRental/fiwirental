import graphene
# noinspection PyUnresolvedReferences
from Models import Person


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
        email_address = graphene.List()
        phone_number = graphene.List()
        language = graphene.List()

    def mutate(self, info, name, photo_id, age, dob, description, lot_num, street_name, community, city, parish,
               email_address, phone_number, language):
        customer = Person(name=name, photo_id=photo_id, age=age, dob=dob, description=description, lot_num=lot_num,
                          street_name=street_name,
                          community=community, city=city, parish=parish, email_address=email_address,
                          phone_number=phone_number, language=language)
        customer.save()
        return CreateCustomer(
            name=customer.name,
            photo_id=customer.photo_id,
            age=customer.age,
            dob=customer.dob,
            description=customer.Description,
            lot_num=customer.lot_num,
            Street_name=customer.Street_name,
            Community=customer.Community,
            City=customer.City,
            Parish=customer.Parish,
            email_address=customer.email_address,
            phone_number=customer.phone_number,
            Language=customer.Language
        )


class MyMutations(graphene.ObjectType):
    create_person = CreateCustomer.Field()
import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import Person

class CreateCustomer(graphene.Mutation):
    
    #image storage here
    pid = graphene.ID()
    name = graphene.String()
    age = graphene.Int()
    dob = graphene.Date()
    member_since = graphene.DateTime()
    description = graphene.String()
    lot_num = graphene.Int()
    Street_name = graphene.String()
    Community = graphene.String()
    City =  graphene.String()
    Parish =  graphene.Sting()
    email_address = graphene.List()
    phone_number = graphene.List()
    Language = graphene.List()
    Number_of_rentals = graphene.Int()
    Rating = graphene.Decimal()

    class Arguments:
        name = graphene.String()
        age = graphene.Int()
        dob = graphene.Date()
        description = graphene.String()
        lot_num = graphene.Int()
        Street_name = graphene.String()
        Community = graphene.String()
        City =  graphene.String()
        Parish =  graphene.Sting()
        email_address = graphene.List()
        phone_number = graphene.List()
        Language = graphene.List()
    
    def mutate(self, info, name, age,dob, description, 
    lot_num,Street_name,Community,City,Parish,email_address,phone_number,Language):
        customer = Person(name=name, age=age,dob=dob, description=description, lot_num=lot_num,Street_name=Street_name,Community=Community,City=City,Parish=Parish,email_address=email_address,phone_number=phone_number,Language=Language)
        customer.save()
        return CreateCustomer(
            name = customer.name,
            age = customer.age,
            dob = customer.dob,
            description = customer.Description,
            lot_num = customer.lot_num,
            Street_name = customer.Street_name,
            Community = customer.Community,
            City = customer.City,
            Parish = customer.Parish,
            email_address = customer.email_address,
            phone_number = customer.phone_number,
            Language = customer.Language
        )

class MyMutations(graphene.ObjectType):
    create_person = CreateCustomer.Field()
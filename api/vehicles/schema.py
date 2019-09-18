import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType

class CreateVehicleEntry(graphene.Mutation):
    #find out how to insert images
    chassis_num = graphene.String()
    model = graphene.String()
    make = graphene.String()
    year = graphene.Date()
    owner_id = graphene.String()
    transmission_type = graphene.String()
    Description = graphene.String()
    Price = graphene.Decimal() 

    class Arguments:
        chassis_num = graphene.String()
        model = graphene.String()
        make = graphene.String()
        year = graphene.Date()
        owner_id = graphene.String()
        transmission_type = graphene.String()
        Description = graphene.String()
        Price = graphene.Decimal() 
    
import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from Models.models import Vehicle as VehicleModel
from Models.models import Person as PersonModel
from Models.models import Rental as RentalModel
from Rentals.schema import CreateRental
from Customers.schema import CreateCustomer
from Vehicles.schema import CreateVehicleEntry


class Vehicle(MongoengineObjectType):

    class Meta:
        model = VehicleModel
        interfaces = (Node,)


class Person(MongoengineObjectType):

    class Meta:
        model = PersonModel
        interfaces = (Node,)


class Rental(MongoengineObjectType):

    class Meta:
        model = RentalModel
        interfaces = (Node,)


class MyMutations(graphene.ObjectType):
    create_customer = CreateCustomer.Field()
    create_vehicle_entry = CreateVehicleEntry.Field()
    create_rental = CreateRental.Field()


class Query(graphene.ObjectType):
    node = Node.Field()
    all_customers = MongoengineConnectionField(Person)
    all_rentals = MongoengineConnectionField(Rental)
    all_vehicles = MongoengineConnectionField(Vehicle)
    person = graphene.Field(Person)
    rental = graphene.Field(Rental)
    Vehicles = graphene.Field(Vehicle)


schema = graphene.Schema(query=Query, types=[Vehicle, Person, Rental], mutation=MyMutations)

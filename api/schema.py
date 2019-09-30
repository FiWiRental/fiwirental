import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from Models.models import Vehicle as VehicleModel
from Models.models import Person as PersonModel
from Models.models import Rental as RentalModel
from Rentals.schema import CreateRental as newRental
from Customers.schema import CreateCustomer as newCustomer
from Vehicles.schema import CreateVehicleEntry as newVehicle


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
    create_person = newCustomer.Field()
    create_vehicle = newVehicle.Field()
    create_rental = newRental.Field()


class Query(graphene.ObjectType):
    node = Node.Field()
    all_customers = MongoengineConnectionField(Person)
    all_rentals = MongoengineConnectionField(Rental)
    all_vehicles = MongoengineConnectionField(Vehicle)
    Vehicles = graphene.Field(Vehicle)


schema = graphene.Schema(query=Query, types=[Vehicle, Person, Rental], mutation=MyMutations)

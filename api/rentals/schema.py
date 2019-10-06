import graphene
from Models.models import Rental, BaseAddress


class CreateRental(graphene.Mutation):
    start_date = graphene.Date()
    end_date = graphene.Date()
    renter_id = graphene.String()
    vehicle_id = graphene.String()
    lot_num = graphene.Int()
    street_name = graphene.String()
    community = graphene.String()
    city = graphene.String()
    parish = graphene.String()
    location_type = graphene.String()
    pickup_time = graphene.DateTime()
    dropoff_time = graphene.DateTime()

    class Arguments:
        start_date = graphene.Date()
        end_date = graphene.Date()
        renter_id = graphene.String()
        vehicle_id = graphene.String()
        lot_num = graphene.Int()
        street_name = graphene.String()
        community = graphene.String()
        city = graphene.String()
        parish = graphene.String()
        location_type = graphene.String()
        pickup_time = graphene.DateTime()
        dropoff_time = graphene.DateTime()

    @staticmethod
    def mutate(self, info, start_date, end_date, renter_id, vehicle_id, lot_num, street_name, community, city, parish,
               location_type, pickup_time
               , dropoff_time):
        rental_address = BaseAddress(lot_num=lot_num, street_name=street_name, community=community,
                                     city=city, parish=parish)
        rental = Rental(start_date=start_date, end_date=end_date, renter_id=renter_id, vehicle_id=vehicle_id
                        , location_type=location_type, pickup_time=pickup_time,
                        dropoff_time=dropoff_time)
        rental.address = rental_address
        rental.save()
        return CreateRental(
            start_date=rental.start_date,
            end_date=rental.end_date,
            renter_id=rental.renter_id,
            vehicle_id=rental.vehicle_id,
            lot_num=rental.address.lot_num,
            street_name=rental.address.street_name,
            community=rental.address.community,
            city=rental.address.city,
            parish=rental.address.parish,
            location_type=rental.location_type,
            pickup_time=rental.pickup_time,
            dropoff_time=rental.dropoff_time
        )

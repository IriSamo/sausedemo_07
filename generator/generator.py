from data.data import Person
from faker import Faker

faker = Faker('en_Us')
Faker.seed()


def generated_person():
    yield Person(first_name=faker.first_name(),
                  last_name=faker.last_name(),
                  postal_code=faker.postcode())

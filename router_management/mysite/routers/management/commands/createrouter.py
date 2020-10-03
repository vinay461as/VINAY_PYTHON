from django.core.management.base import BaseCommand, CommandError

from mysite.routers.models import Router
from faker import Faker
# from faker.providers import internet

class Command(BaseCommand):
    help = 'Command for creating router'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of router to be created')


    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker()
        for _ in range(total):
            sapid = fake.bothify('???-########')
            loopback = fake.ipv4()
            mac_address = fake.mac_address()
            hostname = fake.hostname()

            Router.objects.get_or_create(sapid=sapid, loopback=loopback, mac_address=mac_address, hostname=hostname)

        return 'Router created Successfully'
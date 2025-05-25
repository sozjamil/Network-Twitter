from django.core.management.base import BaseCommand
from faker import Faker
from network.models import User, Post

class Command(BaseCommand):
    help = 'Generate fake users and posts'

    def handle(self, *args, **kwargs):
        fake = Faker()
        users = []
        for _ in range(10):
            username = fake.user_name()
            user = User.objects.create_user(username=username, password="password123")
            users.append(user)
        for user in users:
            for _ in range(5):
                Post.objects.create(
                    user=user,
                    content=fake.sentence(nb_words=12),
                )
        self.stdout.write(self.style.SUCCESS('Fake data created!'))
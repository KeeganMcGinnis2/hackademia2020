from django.db import models
from django.contrib.auth.models import User

PLANETS = (
    ('MERCURY', 'Mercury'),
    ('VENUS', 'Venus'),
    ('EARTH', 'Earth'),
    ('MARS', 'Mars'),
    ('JUPITER', 'Jupiter'),
    ('SATURN', 'Saturn'),
    ('URANUS', 'Uranus'),
    ('NEPTUNE', 'Neptune'),
    ('PLUTO', 'Pluto')
)

class SBUser(User):
    planet = models.CharField(max_length=7, choices=PLANETS, default='EARTH')

class Message(models.Model):
    author = models.ForeignKey(SBUser, related_name='author', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_10_messages():
        return Message.objects.order_by('-timestamp').all()[:10]
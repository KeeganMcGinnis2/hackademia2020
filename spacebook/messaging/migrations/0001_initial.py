# Generated by Django 3.0.8 on 2020-07-12 00:09

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='SBUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('planet', models.CharField(choices=[('MERCURY', 'Mercury'), ('VENUS', 'Venus'), ('EARTH', 'Earth'), ('MARS', 'Mars'), ('JUPITER', 'Jupiter'), ('SATURN', 'Saturn'), ('URANUS', 'Uranus'), ('NEPTUNE', 'Neptune'), ('PLUTO', 'Pluto')], default='EARTH', max_length=7)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]

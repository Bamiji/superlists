# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lists', '0004_item_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='owner',
<<<<<<< HEAD
            field=models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL),
=======
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True),
>>>>>>> 9ae3dc6ed7a103727e5453a7be6490491a53fac3
        ),
    ]

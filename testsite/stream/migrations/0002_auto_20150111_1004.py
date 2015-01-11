# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
        ('stream', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='photo',
            field=models.ForeignKey(related_name='streams', to='items.PhotoItem', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stream',
            name='tweet',
            field=models.ForeignKey(related_name='streams', to='items.TweetItem', null=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0002_auto_20150111_1004'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stream',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='stream',
            name='photo',
            field=models.ForeignKey(related_name='streams', blank=True, to='items.PhotoItem', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stream',
            name='tweet',
            field=models.ForeignKey(related_name='streams', blank=True, to='items.TweetItem', null=True),
            preserve_default=True,
        ),
    ]

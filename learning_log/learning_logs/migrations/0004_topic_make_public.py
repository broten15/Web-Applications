# Generated by Django 3.0.7 on 2020-07-01 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_topic_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='make_public',
            field=models.BooleanField(default=False, verbose_name='make public'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-08 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='summary',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]

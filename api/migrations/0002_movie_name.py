# Generated by Django 4.0.6 on 2022-07-16 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='name',
            field=models.CharField(default='titulo', max_length=255),
        ),
    ]

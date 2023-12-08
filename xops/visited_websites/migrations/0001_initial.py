# Generated by Django 5.0 on 2023-12-07 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VisitedLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.UUIDField(editable=False)),
                ('link', models.URLField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

# Generated by Django 3.2 on 2021-05-01 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name of the site to identify and compare with other results')),
                ('category', models.CharField(choices=[('ED', 'Education'), ('SM', 'Social Media'), ('GA', 'Gaming'), ('CS', 'Cloud Service')], max_length=2, verbose_name='service category')),
                ('endpoint', models.CharField(max_length=5000, verbose_name='endpoint to hit when testing')),
                ('request_datetime', models.DateTimeField(verbose_name='datetime when the request was sent')),
                ('response_time', models.DecimalField(decimal_places=3, max_digits=12, verbose_name='response time in seconds')),
                ('response_status_code', models.PositiveIntegerField()),
                ('response_result', models.CharField(max_length=1000)),
            ],
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-15 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('file_ref_no', models.CharField(max_length=200)),
                ('account_code_no', models.CharField(max_length=200)),
                ('marketer', models.CharField(max_length=200)),
                ('director_name', models.CharField(max_length=200)),
                ('director_no', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('product_description', models.TextField()),
                ('comodity', models.CharField(max_length=200)),
                ('communication', models.CharField(max_length=200)),
                ('travelling_accomodation', models.CharField(max_length=200)),
                ('advertising', models.CharField(max_length=200)),
                ('total', models.CharField(max_length=200)),
                ('remarks', models.TextField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('customer', models.CharField(max_length=200)),
                ('file_no', models.CharField(max_length=200)),
                ('origin_port', models.CharField(max_length=200)),
                ('destination_port', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('product', models.CharField(max_length=200)),
                ('forwarder', models.CharField(max_length=200)),
                ('clearing_agent', models.CharField(max_length=200)),
                ('marketer', models.CharField(max_length=200)),
                ('buying', models.CharField(max_length=200)),
                ('selling', models.CharField(max_length=200)),
                ('margin', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

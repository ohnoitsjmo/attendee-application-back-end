# Generated by Django 2.1 on 2018-09-13 21:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=250)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be enteredin the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('is_eighteen', models.BooleanField(default=False)),
                ('school', models.CharField(max_length=250)),
                ('graduation_date', models.DateField()),
                ('major', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('dietary_restrictions', models.IntegerField(choices=[(0, 'None'), (1, 'Kosher'), (2, 'Gluten-Free'), (3, 'Vegan'), (4, 'Vegetarian')], default=0)),
                ('allergies', models.TextField()),
                ('github', models.CharField(max_length=250)),
                ('linkedin', models.CharField(max_length=250)),
                ('personal_website', models.CharField(max_length=250)),
                ('resume', models.FileField(upload_to='resume/')),
                ('short_answer', models.TextField()),
                ('gender', models.IntegerField(choices=[(0, 'Female'), (1, 'Male'), (2, 'Other')], default=0)),
                ('ethnicity', models.IntegerField(choices=[(0, 'American Indian or Alaska Native'), (1, 'Asian'), (2, 'Black or African American'), (3, 'Hispanic or Latino'), (4, 'Native Hawaiian or Other Pacific Islander'), (5, 'White'), (6, 'Other')], default=0)),
                ('anything_else', models.TextField()),
                ('agreed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
    ]

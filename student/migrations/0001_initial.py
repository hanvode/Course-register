# Generated by Django 3.0.5 on 2020-07-14 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('idno', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=15)),
                ('mobile', models.BigIntegerField(unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.TextField()),
                ('pic', models.ImageField(blank=True, upload_to='student_pics/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

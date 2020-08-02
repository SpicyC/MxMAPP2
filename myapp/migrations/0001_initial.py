# Generated by Django 3.0.8 on 2020-08-02 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('position', models.DateField()),
                ('image_url', models.TextField(blank=True, null=True)),
                ('company', models.TextField(blank=True, null=True)),
            ],
            options={
                'order_with_respect_to': 'name',
            },
        ),
    ]

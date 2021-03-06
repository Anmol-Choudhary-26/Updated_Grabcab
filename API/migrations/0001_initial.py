# Generated by Django 3.2.10 on 2022-01-13 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modl', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('rentrate', models.IntegerField()),
                ('buyrate', models.IntegerField()),
                ('odometer', models.IntegerField()),
                ('IsAvailable', models.BooleanField()),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RentedCab', to='API.user')),
            ],
        ),
    ]

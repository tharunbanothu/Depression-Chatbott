# Generated by Django 4.1.3 on 2022-11-28 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_join_date', models.DateField(auto_now_add=True)),
                ('user_name', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_password', models.CharField(max_length=100)),
                ('user_phone', models.BigIntegerField(null=True)),
                ('user_city', models.CharField(max_length=100)),
                ('user_profile', models.ImageField(null=True, upload_to='images/')),
            ],
            options={
                'db_table': 'user_details',
            },
        ),
    ]

# Generated by Django 4.0.5 on 2023-02-14 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestEnv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('account', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('account_xpath', models.CharField(max_length=1000)),
                ('password_xpath', models.CharField(max_length=1000)),
                ('login_button_xpath', models.CharField(max_length=1000)),
            ],
        ),
    ]

# Generated by Django 3.0.8 on 2020-07-07 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite_post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSigin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password1', models.CharField(max_length=50)),
                ('password2', models.CharField(max_length=50)),
            ],
        ),
    ]

# Generated by Django 2.1.7 on 2019-03-25 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testmerch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupbarang', models.CharField(max_length=200)),
                ('namabarang', models.CharField(max_length=200)),
                ('deskripbarang', models.CharField(max_length=200)),
            ],
        ),
    ]

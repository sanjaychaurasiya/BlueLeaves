# Generated by Django 4.1 on 2022-08-20 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0008_alter_farmblock_block_name_alter_farmblock_unit_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmblock',
            name='block_id',
            field=models.CharField(default='b1', max_length=10),
        ),
        migrations.AlterField(
            model_name='farmblock',
            name='block_name',
            field=models.CharField(default='Xa9FfzO-PA', max_length=10),
        ),
    ]

# Generated by Django 4.1 on 2022-08-20 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0005_alter_farmblock_block_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmblock',
            name='block_name',
            field=models.CharField(default='NzUErLpjw5x3vg', max_length=10),
        ),
    ]
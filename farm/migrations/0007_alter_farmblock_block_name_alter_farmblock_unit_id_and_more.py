# Generated by Django 4.1 on 2022-08-20 07:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0006_alter_farmblock_block_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmblock',
            name='block_name',
            field=models.CharField(default='Pv5cfh4GXA', max_length=10),
        ),
        migrations.AlterField(
            model_name='farmblock',
            name='unit_id',
            field=models.CharField(default='u2', max_length=10),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='group_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]

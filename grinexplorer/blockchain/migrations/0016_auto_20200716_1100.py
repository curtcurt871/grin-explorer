# Generated by Django 2.1.1 on 2020-07-16 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0015_auto_20200414_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='kernel_mmr_size',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='block',
            name='output_mmr_size',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.1.5 on 2019-01-26 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0003_auto_20190125_0649'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_user_attribute',
            name='baptised',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=10),
        ),
        migrations.AddField(
            model_name='t_user_attribute',
            name='spiritual_maturity',
            field=models.CharField(default='ordinary', max_length=20),
        ),
        migrations.AddField(
            model_name='t_user_attribute',
            name='years_in_ministry',
            field=models.IntegerField(default=8),
            preserve_default=False,
        ),
    ]

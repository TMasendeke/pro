# Generated by Django 2.1.5 on 2019-02-17 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_t_dict_sub_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='t_dict',
            name='sub_category',
        ),
    ]

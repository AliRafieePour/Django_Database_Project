# Generated by Django 2.0.7 on 2018-12-31 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_dept_dept_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dept',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='dept',
            name='phonenum',
            field=models.CharField(max_length=110),
        ),
    ]
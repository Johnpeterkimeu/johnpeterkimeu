# Generated by Django 4.1.1 on 2022-10-19 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_customuser_age_alter_customuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False),
        ),
    ]

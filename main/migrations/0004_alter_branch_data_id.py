# Generated by Django 4.2.2 on 2023-06-27 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_branch_data_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch_data',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

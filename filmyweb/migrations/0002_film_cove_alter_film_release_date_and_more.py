# Generated by Django 4.2.6 on 2023-10-25 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='cove',
            field=models.ImageField(blank=True, null=True, upload_to='covers'),
        ),
        migrations.AlterField(
            model_name='film',
            name='release_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='writer',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]

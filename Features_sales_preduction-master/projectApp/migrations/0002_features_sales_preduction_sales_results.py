# Generated by Django 4.1.2 on 2022-10-23 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='features_sales_preduction',
            name='Sales_Results',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
# Generated by Django 4.2.3 on 2023-07-20 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="item_image",
            field=models.CharField(
                default="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.vectorstock.com%2Froyalty-free-vectors%2Fdefault-vectors&psig=AOvVaw0KZ2VYfBnS8B_ZKyFZfXch&ust=1689932604437000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCMiP4tf_nIADFQAAAAAdAAAAABAE",
                max_length=500,
            ),
        ),
    ]

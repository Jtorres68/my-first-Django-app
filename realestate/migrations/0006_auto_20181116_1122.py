# Generated by Django 2.0.9 on 2018-11-16 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0005_post_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='seller',
            field=models.CharField(choices=[('On Sale', 'onsale'), ('Contract Pending', 'contract_pending'), ('Sold', 'sold')], default='On Sale', max_length=16),
        ),
    ]
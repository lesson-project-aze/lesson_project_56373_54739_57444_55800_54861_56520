# Generated by Django 4.1.3 on 2023-01-06 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0015_alter_review_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='title_az',
        ),
    ]

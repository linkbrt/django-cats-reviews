# Generated by Django 5.1.1 on 2024-10-02 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0002_alter_cat_age_alter_cat_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cat',
            old_name='describtion',
            new_name='description',
        ),
    ]

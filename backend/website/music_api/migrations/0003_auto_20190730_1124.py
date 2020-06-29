# Generated by Django 2.2.3 on 2019-07-30 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_api', '0002_auto_20190730_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritesongs',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='joined_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterUniqueTogether(
            name='favoritesongs',
            unique_together={('user', 'song')},
        ),
    ]
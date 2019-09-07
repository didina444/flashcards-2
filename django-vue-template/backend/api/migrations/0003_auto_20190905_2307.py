# Generated by Django 2.1.4 on 2019-09-05 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='binNum',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='card',
            name='nextReviewAt',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='wrongCount',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]

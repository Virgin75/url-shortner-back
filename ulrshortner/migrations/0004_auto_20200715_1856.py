# Generated by Django 3.0.8 on 2020-07-15 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ulrshortner', '0003_auto_20200715_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='slug',
            field=models.CharField(default='r4HlKr', max_length=6, unique=True),
        ),
    ]

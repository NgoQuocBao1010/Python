# Generated by Django 3.0.3 on 2020-02-21 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeddingDress', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weddingdress',
            name='image',
            field=models.ImageField(default='default.jbg', upload_to='sample_pics'),
        ),
    ]

# Generated by Django 3.0.7 on 2020-07-02 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]

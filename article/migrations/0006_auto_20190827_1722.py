# Generated by Django 2.1.5 on 2019-08-27 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_date']},
        ),
    ]

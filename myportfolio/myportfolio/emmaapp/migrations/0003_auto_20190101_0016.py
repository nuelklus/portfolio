# Generated by Django 2.2.5 on 2019-01-01 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emmaapp', '0002_pdf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='message',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='subject',
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]

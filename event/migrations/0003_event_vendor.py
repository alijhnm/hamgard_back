# Generated by Django 2.2.2 on 2019-06-16 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('event', '0002_auto_20190616_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='vendor',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='account.Vendor'),
            preserve_default=False,
        ),
    ]

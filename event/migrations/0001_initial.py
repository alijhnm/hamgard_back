# Generated by Django 2.2.2 on 2019-06-16 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('address_text', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.CharField(blank=True, max_length=50, null=True)),
                ('lat', models.FloatField(blank=True, default=None, null=True)),
                ('lng', models.FloatField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('summary', models.TextField(blank=True, null=True)),
                ('discount', models.FloatField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('address', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='event.Address')),
            ],
        ),
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PlaceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_fa', models.CharField(max_length=500)),
                ('name_en', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_fa', models.CharField(max_length=500)),
                ('name_en', models.CharField(blank=True, max_length=500, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Address')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.PlaceCategory')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.City')),
                ('tags', models.ManyToManyField(blank=True, to='event.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='EventVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='')),
                ('alt', models.CharField(max_length=100)),
                ('Event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='video', to='event.Event')),
            ],
        ),
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('alt', models.CharField(max_length=100)),
                ('Event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='event.Event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.EventCategory'),
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(blank=True, to='event.Tag'),
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='event.Province'),
        ),
    ]

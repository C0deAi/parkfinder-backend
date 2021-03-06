# Generated by Django 2.0.2 on 2018-03-03 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AmenityType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('zipcode', models.CharField(max_length=50)),
                ('county', models.CharField(max_length=250)),
                ('district', models.IntegerField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('notes', models.TextField(blank=True)),
                ('former_name', models.CharField(blank=True, max_length=250)),
                ('neighborhood', models.CharField(blank=True, max_length=250)),
                ('global_id', models.UUIDField()),
                ('park_id', models.CharField(max_length=50)),
                ('parcel_id', models.CharField(max_length=250)),
                ('shape_length', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('park_class', models.CharField(blank=True, max_length=50, verbose_name='class')),
                ('npu1', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ParkAmenity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('size', models.IntegerField(default=0)),
                ('size_unit', models.CharField(blank=True, max_length=50)),
                ('notes', models.TextField(blank=True)),
                ('amenity_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parks.AmenityType')),
                ('park', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parks.Park')),
            ],
        ),
        migrations.AddField(
            model_name='park',
            name='amenities',
            field=models.ManyToManyField(related_name='parks', through='parks.ParkAmenity', to='parks.AmenityType'),
        ),
    ]

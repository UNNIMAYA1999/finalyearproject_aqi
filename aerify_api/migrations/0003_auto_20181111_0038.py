# Generated by Django 2.1.2 on 2018-11-11 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aerify_api', '0002_auto_20181109_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='aerifyDailyAPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_city', models.CharField(blank=True, max_length=100, null=True)),
                ('daily_date', models.CharField(blank=True, max_length=20, null=True)),
                ('daily_aqi', models.FloatField(blank=True, null=True)),
                ('daily_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('daily_updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'aerifyDailyAPI',
            },
        ),
        migrations.CreateModel(
            name='aerifyMonthlyAPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monthly_city', models.CharField(blank=True, max_length=100, null=True)),
                ('monthly_date', models.CharField(blank=True, max_length=20, null=True)),
                ('monthly_aqi', models.FloatField(blank=True, null=True)),
                ('monthly_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('monthly_updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'aerifyMonthlyAPI',
            },
        ),
        migrations.CreateModel(
            name='aerifyYearlyAPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yearly_city', models.CharField(blank=True, max_length=100, null=True)),
                ('yearly_date', models.CharField(blank=True, max_length=20, null=True)),
                ('yearly_aqi', models.FloatField(blank=True, null=True)),
                ('yearly_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('yearly_updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'aerifyYearlyAPI',
            },
        ),
        migrations.DeleteModel(
            name='aerifyAPI',
        ),
    ]
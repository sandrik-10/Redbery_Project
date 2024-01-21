# Generated by Django 4.2 on 2024-01-19 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('text_color', models.CharField(max_length=100)),
                ('background_color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=500)),
                ('published_date', models.DateTimeField()),
                ('author', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('categories', models.ManyToManyField(to='redbery_app.category')),
            ],
        ),
    ]

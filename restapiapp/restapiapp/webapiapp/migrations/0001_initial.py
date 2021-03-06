# Generated by Django 3.0.5 on 2020-04-22 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipename', models.CharField(max_length=20)),
                ('ingredients', models.CharField(max_length=200)),
                ('instructions', models.CharField(max_length=1000)),
                ('servingsize', models.IntegerField()),
                ('category', models.CharField(max_length=20)),
                ('notes', models.CharField(max_length=100)),
                ('dateadded', models.DateField()),
                ('datemodified', models.DateField()),
            ],
        ),
    ]

# Generated by Django 3.0.3 on 2020-09-02 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SideProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('link', models.URLField()),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
            ],
        ),
    ]

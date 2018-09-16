# Generated by Django 2.1.1 on 2018-09-15 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('video', '0001_initial'),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('play_on', models.DateTimeField(auto_now_add=True)),
                ('total_play_time', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='authentication.User')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='video.Video')),
            ],
        ),
    ]

# Generated by Django 2.2.3 on 2019-07-13 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='real_time_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('heart_rate', models.IntegerField(default=0)),
                ('EEG_reading', models.IntegerField(default=0)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.devices')),
            ],
        ),
    ]
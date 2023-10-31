# Generated by Django 4.0.8 on 2023-11-26 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreditCard_Name', models.TextField(max_length=50)),
                ('CreditCard_Detail', models.TextField(max_length=100)),
                ('CreditCard_PayDate', models.DateField(blank=True, default='')),
                ('User_Email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TrackType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Spend_Type', models.TextField(max_length=50)),
                ('User_Email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TrackRecord',
            fields=[
                ('Track_ID', models.AutoField(primary_key=True, serialize=False, verbose_name='TrackID')),
                ('Track_Amount', models.IntegerField(max_length=100, verbose_name='TrackAmount')),
                ('Track_Detail', models.TextField(max_length=100, verbose_name='TrackDetail')),
                ('Track_Date', models.DateField(verbose_name='TrackDate')),
                ('Credit_Card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Track.creditcard', verbose_name='CreditCard')),
                ('Track_Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Track.tracktype', verbose_name='TrackType')),
                ('User_Email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='CustomUser')),
            ],
        ),
    ]

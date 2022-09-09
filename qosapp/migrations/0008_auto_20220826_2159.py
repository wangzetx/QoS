# Generated by Django 2.1.15 on 2022-08-26 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qosapp', '0007_auto_20220824_0829'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('burst_size', models.IntegerField()),
                ('limited_rate', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='QoSconfigure',
        ),
        migrations.AddField(
            model_name='flow',
            name='statisitcs',
            field=models.TextField(null=True),
        ),
    ]

# Generated by Django 2.0 on 2021-01-17 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(default='', max_length=20)),
                ('system', models.CharField(default='', max_length=10)),
                ('sn', models.CharField(default='', max_length=128)),
                ('architecture', models.CharField(default='', max_length=10)),
                ('os_family', models.CharField(default='', max_length=10)),
                ('distribution', models.CharField(default='', max_length=10)),
                ('distribution_version', models.CharField(default='', max_length=10)),
                ('memtotal_mb', models.PositiveIntegerField(default=0)),
                ('swaptotal_mb', models.PositiveIntegerField(default=0)),
                ('processor_count', models.IntegerField(default=0)),
                ('processor_cores', models.IntegerField(default=0)),
                ('diskdevice', models.CharField(default='{}', max_length=100)),
                ('diskmount', models.CharField(default='{}', max_length=512)),
                ('ip_business', models.GenericIPAddressField(default='0.0.0.0')),
                ('ip_manager', models.GenericIPAddressField(default='0.0.0.0')),
                ('rack_number', models.CharField(default='', max_length=20)),
                ('unit_number', models.CharField(default='', max_length=10)),
                ('status', models.CharField(default='', max_length=5)),
                ('remark', models.CharField(default='', max_length=100)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField()),
            ],
        ),
    ]

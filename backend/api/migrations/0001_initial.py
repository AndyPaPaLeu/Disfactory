# Generated by Django 2.2.3 on 2019-10-09 11:09

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=3857)),
                ('landcode', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('factory_type', models.CharField(choices=[('1', '金屬'), ('2-1', '沖床、銑床、車床、鏜孔'), ('2-2', '焊接、鑄造、熱處理'), ('2-3', '金屬表面處理、噴漆'), ('3', '塑膠加工、射出'), ('4', '橡膠加工'), ('5', '非金屬礦物（石材）'), ('6', '食品'), ('7', '皮革'), ('8', '紡織'), ('9', '其他')], default='9', max_length=3)),
                ('status', models.CharField(choices=[('D', '已舉報'), ('F', '資料不齊'), ('A', '待審核')], max_length=1)),
                ('status_time', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReportRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_ip', models.GenericIPAddressField(blank=True, default='192.168.0.1', null=True)),
                ('action_type', models.CharField(max_length=10)),
                ('action_body', django.contrib.postgres.fields.jsonb.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('contact', models.CharField(blank=True, max_length=64, null=True)),
                ('others', models.CharField(blank=True, max_length=1024)),
                ('factory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Factory')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image_path', models.URLField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('orig_time', models.DateTimeField(blank=True, null=True)),
                ('factory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Factory')),
                ('report_record', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.ReportRecord')),
            ],
        ),
    ]
# Generated by Django 3.1.2 on 2020-10-20 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201020_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='api.group'),
        ),
    ]

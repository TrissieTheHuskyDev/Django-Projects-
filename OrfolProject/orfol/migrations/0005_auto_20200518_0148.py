# Generated by Django 3.0.5 on 2020-05-17 20:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orfol', '0004_auto_20200518_0041'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='category',
            field=models.ForeignKey(default=-1.0, on_delete=django.db.models.deletion.CASCADE, to='orfol.Category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='report',
            name='date_occurrence',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]

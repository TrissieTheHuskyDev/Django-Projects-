# Generated by Django 3.0.5 on 2020-05-16 23:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orfol', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterField(
            model_name='report',
            name='description',
            field=models.TextField(validators=[django.core.validators.MaxLengthValidator(300)]),
        ),
        migrations.AlterField(
            model_name='report',
            name='type',
            field=models.CharField(choices=[('L', 'Lost'), ('F', 'Found')], max_length=80),
        ),
        migrations.AlterField(
            model_name='reportimage',
            name='report_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orfol.Report'),
        ),
    ]

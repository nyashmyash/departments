# Generated by Django 3.0 on 2023-06-28 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('foto', models.CharField(blank=True, max_length=100, null=True)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('salary', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('age', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='department.Department')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='director',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='director_department', to='department.Employee'),
        ),
    ]

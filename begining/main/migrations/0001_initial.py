# Generated by Django 4.1.7 on 2023-03-23 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('layer', models.IntegerField(verbose_name='Layer')),
                ('parent_field', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.field')),
                ('table_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.menu')),
            ],
            options={
                'verbose_name': 'Поле',
                'verbose_name_plural': 'Поля',
            },
        ),
    ]

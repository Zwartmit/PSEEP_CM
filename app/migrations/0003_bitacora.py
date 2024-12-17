# Generated by Django 5.1.4 on 2024-12-17 15:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_aprendiz_instructor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bitacora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(null=True, verbose_name='Fecha')),
                ('descripcion', models.TextField(null=True, verbose_name='Descripción')),
                ('aprendiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Aprendiz', to='app.aprendiz')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.instructor', verbose_name='Instructor')),
            ],
            options={
                'verbose_name': 'Bitácora',
                'verbose_name_plural': 'Bitácoras',
                'db_table': 'Bitacora',
            },
        ),
    ]

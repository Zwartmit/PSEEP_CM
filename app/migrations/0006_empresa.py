# Generated by Django 5.1.4 on 2024-12-30 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_aprendiz_contrasena_aprendiz_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True, verbose_name='Nombre')),
                ('nit', models.PositiveIntegerField(null=True, verbose_name='NIT')),
                ('modalidad', models.CharField(choices=[('Contrato de aprendizaje', 'Contrato de aprendizaje'), ('Vínculo laboral o contractual', 'Vínculo laboral o contractual'), ('Proyecto productivo', 'Proyecto productivo'), ('Apoyo a una unidad productiva familiar', 'Apoyo a una unidad productiva familiar'), ('Apoyo a institución estatal nacional, territorial, ONG o entidad sin ánimo de lucro', 'Apoyo a institución estatal nacional, territorial, ONG o entidad sin ánimo de lucro'), ('Monitoria', 'Monitoria'), ('Pasantia', 'Pasantia')], max_length=100, null=True, verbose_name='Modalidad')),
                ('jefe', models.CharField(max_length=200, null=True, verbose_name='Jefe')),
                ('numero_telefono', models.PositiveIntegerField(null=True, verbose_name='Nº de teléfono')),
                ('correo', models.EmailField(max_length=254, null=True, verbose_name='Correo')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
                'db_table': 'Empresa',
            },
        ),
    ]

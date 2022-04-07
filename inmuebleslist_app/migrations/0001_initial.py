# Generated by Django 4.0.2 on 2022-04-07 02:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=255)),
                ('pais', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=500)),
                ('imagen', models.CharField(max_length=900)),
                ('avg_calificacion', models.FloatField(default=0)),
                ('number_calification', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('empresa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empresas', to='inmuebleslist_app.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.PositiveIntegerField()),
                ('texto', models.CharField(blank=True, max_length=200, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comentario_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('inmueble_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='inmuebleslist_app.inmueble')),
            ],
        ),
    ]

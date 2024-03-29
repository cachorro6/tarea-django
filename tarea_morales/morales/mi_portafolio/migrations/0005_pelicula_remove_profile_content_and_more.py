# Generated by Django 4.2.10 on 2024-02-18 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_portafolio', '0004_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('fecha_estreno', models.PositiveIntegerField()),
                ('director', models.CharField(max_length=255)),
                ('sinopsis', models.TextField()),
                ('mas_veces_vistas', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='content',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='skills',
        ),
        migrations.AddField(
            model_name='profile',
            name='pelicula_favorita',
            field=models.CharField(default='ValorPredeterminado', max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='ultima_pelicula_vista',
            field=models.CharField(default='ValorPredeterminado', max_length=255),
        ),
    ]

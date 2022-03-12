# Generated by Django 4.0.2 on 2022-03-12 20:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_apellido_usuario_alias'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='birthday',
            field=models.DateField(default='2022-03-12'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Poke',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokes_hechos', to='app.usuario')),
                ('recipiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokes_recibidos', to='app.usuario')),
            ],
        ),
    ]
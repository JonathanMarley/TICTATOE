from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partidas', '0003_alter_partida_jugador_0_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.CharField(max_length=255)),
                ('enviado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partidas.partida')),
            ],
        ),
    ]
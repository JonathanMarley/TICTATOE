from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('partidas', '0002_alter_tablero_options_alter_tablero_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='jugador_0',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jugador_0', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='partida',
            name='jugador_ganador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jugador_ganador', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='partida',
            name='jugador_x',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jugador_x', to=settings.AUTH_USER_MODEL),
        ),
    ]

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partidas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tablero',
            options={'verbose_name': 'Tablero', 'verbose_name_plural': 'Tableros'},
        ),
        migrations.AlterModelTable(
            name='tablero',
            table='Tablero',
        ),
    ]
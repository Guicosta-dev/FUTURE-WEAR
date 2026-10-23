# Generated manually after hardening the Produto model.
from django.db import migrations, models
from django.core.validators import MinValueValidator


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_produto_foto_alter_produto_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='estoque',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(
                decimal_places=2,
                max_digits=10,
                validators=[MinValueValidator(0)],
            ),
        ),
    ]

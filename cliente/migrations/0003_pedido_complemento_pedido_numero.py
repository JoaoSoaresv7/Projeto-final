<<<<<<< HEAD
# Generated by Django 5.2.1 on 2025-05-28 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_pedido_concluido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='complemento',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='numero',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
=======
# Generated by Django 5.2.1 on 2025-05-28 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_pedido_concluido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='complemento',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='numero',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
>>>>>>> 81e4968abde002e858a3addca30aac4f09a89e45

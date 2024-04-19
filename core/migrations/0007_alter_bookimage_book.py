# Generated by Django 5.0 on 2024-04-07 16:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_cartitem_user_alter_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookimage',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_images', to='core.book'),
        ),
    ]

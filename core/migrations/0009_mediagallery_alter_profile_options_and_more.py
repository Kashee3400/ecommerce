# Generated by Django 5.0 on 2024-04-17 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_order_order_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='gallery/')),
                ('image_url', models.URLField(blank=True, null=True)),
                ('video_url', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Media Gallery',
                'verbose_name_plural': 'Media Gallerys',
                'db_table': 'tbl_medias',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'managed': True, 'verbose_name': 'User Profile', 'verbose_name_plural': 'User Profiles'},
        ),
        migrations.AlterModelTable(
            name='profile',
            table='tbl_user_profile',
        ),
    ]

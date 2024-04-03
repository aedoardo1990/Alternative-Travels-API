# Generated by Django 3.2.25 on 2024-04-03 17:47

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
            name='Marketplace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('status', models.IntegerField(choices=[(0, 'Available'), (1, 'Sold')], default=0)),
                ('condition', models.CharField(max_length=255)),
                ('details', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, default='../default_post_g5kn5h', upload_to='images/')),
                ('address', models.CharField(max_length=255)),
                ('contact_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('image_filter', models.CharField(choices=[('_1977', '1977'), ('brannan', 'Brannan'), ('earlybird', 'Earlybird'), ('hudson', 'Hudson'), ('inkwell', 'Inkwell'), ('lofi', 'Lo-Fi'), ('kelvin', 'Kelvin'), ('normal', 'Normal'), ('nashville', 'Nashville'), ('rise', 'Rise'), ('toaster', 'Toaster'), ('valencia', 'Valencia'), ('walden', 'Walden'), ('xpro2', 'X-pro II')], default='normal', max_length=32)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]

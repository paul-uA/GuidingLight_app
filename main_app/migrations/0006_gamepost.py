# Generated by Django 4.0.3 on 2022-03-11 03:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0005_delete_gamepost'),
    ]

    operations = [
        migrations.CreateModel(
            name='GamePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bungieid', models.CharField(max_length=100)),
                ('activity_name', models.CharField(max_length=200)),
                ('activity_rank', models.CharField(max_length=150)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

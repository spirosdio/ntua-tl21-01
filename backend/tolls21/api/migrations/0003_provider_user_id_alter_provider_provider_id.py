# Generated by Django 4.0.2 on 2022-02-23 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_alter_provider_provider_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='user_id',
            field=models.ForeignKey(default=5272828939389, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='provider',
            name='provider_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
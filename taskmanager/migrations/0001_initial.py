# Generated by Django 3.2.4 on 2021-07-05 14:21

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
            name='TaskAndEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('due', models.DateTimeField()),
                ('complete', models.CharField(default='nc', max_length=10)),
                ('priority', models.IntegerField(choices=[(10, 'high'), (5, 'low')], default=5)),
                ('name_type', models.IntegerField(choices=[(1, 'Task'), (2, 'Event')], default=1)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

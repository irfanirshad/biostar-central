# Generated by Django 2.0.6 on 2018-08-15 21:26

import biostar.message.models
from django.conf import settings
import django.contrib.auth
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(0, 'Local messages'), (1, 'Email messages'), (2, 'Digest email messages')], db_index=True, default=0)),
                ('source', models.IntegerField(choices=[(0, 'From project discussion'), (1, 'Mentioned in a post'), (2, 'Regular')], db_index=True, default=0)),
                ('uid', models.CharField(max_length=32, unique=True)),
                ('subject', models.CharField(max_length=120)),
                ('body', models.TextField(max_length=10000)),
                ('unread', models.BooleanField(default=True)),
                ('sent_date', models.DateTimeField(db_index=True, null=True)),
                ('parent_msg', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_messages', to='message.Message')),
                ('recipient', models.ForeignKey(on_delete=models.SET(biostar.message.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=models.SET(django.contrib.auth.get_user_model), related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

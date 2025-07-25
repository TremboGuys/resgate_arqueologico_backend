# Generated by Django 5.2.3 on 2025-07-04 17:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_question_id_quiz_playerquiz'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hit', models.BooleanField()),
                ('id_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='core.player')),
                ('id_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='core.question')),
                ('id_quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players_question', to='core.quiz')),
            ],
            options={
                'verbose_name_plural': 'Players Question',
            },
        ),
    ]

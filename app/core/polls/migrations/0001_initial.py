# Generated by Django 3.0.3 on 2021-04-11 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=4096)),
                ('visible', models.BooleanField(default=False)),
                ('max_points', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TestChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_answer', models.CharField(max_length=255)),
                ('points', models.BooleanField()),
                ('lock_other', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TestQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=150, verbose_name='Текст вопроса')),
            ],
        ),
        migrations.CreateModel(
            name='TestTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_name', models.CharField(max_length=255)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group', to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.TestChoice')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.TestQuestion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='testquestion',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.TestTheme'),
        ),
        migrations.AddField(
            model_name='testchoice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.TestQuestion'),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=4096)),
                ('points', models.FloatField()),
                ('lock_other', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.Choice')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

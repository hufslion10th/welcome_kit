# Generated by Django 4.0.3 on 2023-03-17 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_student3'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tm', models.TextField(blank=True, null=True, verbose_name='팀장')),
                ('src', models.TextField(blank=True, null=True, verbose_name='이미지주소')),
                ('hi', models.TextField(blank=True, null=True, verbose_name='좌우명')),
            ],
            options={
                'verbose_name': '팀장소개',
                'verbose_name_plural': '팀장소개',
                'db_table': '팀장소개',
            },
        ),
    ]
# Generated by Django 5.1.2 on 2024-10-25 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_alter_jugador_dorsal'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='imagen',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='club',
            name='liga',
            field=models.CharField(choices=[('Primera A', 'Primera división'), ('Primera B', 'Segunda división'), ('Sin división', 'club sin división')], default='Sin división', max_length=100),
        ),
    ]
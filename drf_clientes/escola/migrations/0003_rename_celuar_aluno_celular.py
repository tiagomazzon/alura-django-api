# Generated by Django 4.1.7 on 2023-02-16 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0002_aluno_celuar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aluno',
            old_name='celuar',
            new_name='celular',
        ),
    ]

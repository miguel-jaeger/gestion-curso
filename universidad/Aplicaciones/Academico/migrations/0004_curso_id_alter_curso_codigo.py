# Generated by Django 4.1.7 on 2023-03-13 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0003_remove_curso_id_alter_curso_codigo'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='curso',
            name='codigo',
            field=models.CharField(max_length=6),
        ),
    ]

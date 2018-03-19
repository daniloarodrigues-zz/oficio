# Generated by Django 2.0.2 on 2018-03-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oficio', '0004_oficio_tratamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oficio',
            name='tratamento',
            field=models.CharField(choices=[('Sr.', 'Senhor'), ('Srª', 'Senhora'), ('V.S.ª', 'Vossa Senhoria'), ('V.Ex.ª', 'Vossa Excelência')], default='Sr.', max_length=20),
        ),
    ]
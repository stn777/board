# Generated by Django 2.0.5 on 2018-08-28 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, unique=True, verbose_name='Название')),
                ('order', models.SmallIntegerField(db_index=True, default=0, verbose_name='Порядок')),
                ('super_rubric', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.Rubric', verbose_name='Надрубрика')),
            ],
        ),
    ]

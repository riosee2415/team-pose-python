# Generated by Django 3.2 on 2021-04-20 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='membermodel',
            name='gender',
            field=models.CharField(choices=[('Male', 'male'), ('Female', 'female'), ('Other', 'other')], max_length=10),
        ),
        migrations.AddField(
            model_name='membermodel',
            name='skills',
            field=models.ManyToManyField(blank=True, to='members.SkillModel'),
        ),
    ]

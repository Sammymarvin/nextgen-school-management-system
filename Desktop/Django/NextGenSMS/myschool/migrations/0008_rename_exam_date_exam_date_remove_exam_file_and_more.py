# Generated by Django 5.0.4 on 2024-05-20 19:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myschool', '0007_studentperformance_grade_parallel_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam',
            old_name='exam_date',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='file',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='student',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='subject',
        ),
        migrations.AddField(
            model_name='exam',
            name='grade_parallel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myschool.gradeparallel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exam',
            name='term',
            field=models.CharField(choices=[('Term 1', 'Term 1'), ('Term 2', 'Term 2'), ('Term 3', 'Term 3')], default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='staffprofile',
            name='formation',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='staffprofile',
            name='specialty',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='ExamScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myschool.exam')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myschool.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myschool.subject')),
            ],
        ),
        migrations.CreateModel(
            name='ReportCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=10)),
                ('total_score', models.FloatField()),
                ('comment', models.CharField(max_length=255)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myschool.student')),
            ],
        ),
        migrations.CreateModel(
            name='TermReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=10)),
                ('average_score', models.FloatField()),
                ('highest_score', models.FloatField()),
                ('lowest_score', models.FloatField()),
                ('grade_parallel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myschool.gradeparallel')),
            ],
        ),
    ]
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('myschool', '0005_alter_staffprofile_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffprofile',
            name='name',
            field=models.CharField(default='default_name', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='staffprofile',
            name='formation',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='staffprofile',
            name='specialty',
            field=models.TextField(max_length=100),
        ),
    ]

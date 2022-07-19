# Generated by Django 4.0.6 on 2022-07-18 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceLocator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('center', models.CharField(max_length=200, null=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.district')),
                ('local_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.localarea')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.service')),
            ],
        ),
    ]

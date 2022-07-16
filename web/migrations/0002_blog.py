# Generated by Django 4.0.6 on 2022-07-15 06:35

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='images/blog/', verbose_name='Image')),
                ('heading', models.TextField()),
                ('category', models.TextField(max_length=200)),
                ('date', models.DateField(editable=False)),
                ('content', models.TextField()),
            ],
        ),
    ]
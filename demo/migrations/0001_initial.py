# Generated by Django 4.1.2 on 2022-10-20 09:37

from django.db import migrations, models
import picklefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='demoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crds', picklefield.fields.PickledObjectField(editable=False)),
            ],
        ),
    ]

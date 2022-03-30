# Generated by Django 3.2 on 2021-11-02 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=100, null=True)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.RemoveField(
            model_name='car',
            name='user',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Table',
        ),
        migrations.DeleteModel(
            name='Car',
        ),
    ]

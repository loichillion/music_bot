# Generated by Django 2.1.15 on 2021-03-26 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message_facebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_id', models.CharField(default='', max_length=200)),
                ('message', models.TextField(blank=True, default='', null=True)),
                ('date_envoie', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Message facebook',
                'verbose_name_plural': 'Messages facebook',
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='accord',
            options={'ordering': ['id'], 'verbose_name': 'Accord', 'verbose_name_plural': 'Accords'},
        ),
    ]
# Generated by Django 2.2.6 on 2020-05-17 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rozetka', '0003_auto_20200517_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='category_product', to='rozetka.Category'),
        ),
    ]
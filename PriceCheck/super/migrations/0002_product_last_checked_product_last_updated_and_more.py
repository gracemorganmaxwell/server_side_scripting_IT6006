# Generated by Django 5.1 on 2024-09-10 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='last_checked',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='product',
            name='last_updated',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='product',
            name='original_unit_quantity',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_size',
            field=models.CharField(default=None, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_source_site',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]

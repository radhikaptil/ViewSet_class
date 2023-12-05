# Generated by Django 4.2.7 on 2023-12-05 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('category_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pname', models.CharField(max_length=100)),
                ('Pid', models.IntegerField()),
                ('Price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product_category')),
            ],
        ),
    ]

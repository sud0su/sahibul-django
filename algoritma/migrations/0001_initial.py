# Generated by Django 4.2.1 on 2023-05-18 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='excel')),
            ],
        ),
        migrations.CreateModel(
            name='Penjualan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waktu_order', models.TimeField()),
                ('nama_produk', models.CharField(max_length=50)),
                ('jumlah_produk', models.PositiveIntegerField()),
                ('jumlah_pembayaran', models.PositiveIntegerField()),
            ],
        ),
    ]

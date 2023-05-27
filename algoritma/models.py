from django.db import models

class Penjualan(models.Model):
    waktu_order = models.TimeField()
    nama_produk = models.CharField(max_length=50)
    jumlah_produk = models.PositiveIntegerField()
    jumlah_pembayaran = models.PositiveIntegerField()

    def __str__(self):
        return f"Order {self.pk}"
    
class ExcelFile(models.Model):
    file = models.FileField(upload_to="excel")
from import_export import resources
from .models  import Penjualan

class PenjualanResource(resources.ModelResource):
    class Meta:
        model = Penjualan  # Ganti dengan model Penjualan Anda
        fields = ('id', 'waktu_order', 'nama_produk', 'jumlah_produk', 'jumlah_pembayaran')

        # Atur kolom untuk sesuai dengan header yang diberikan
        export_order = ('id', 'waktu_order', 'nama_produk', 'jumlah_produk', 'jumlah_pembayaran')


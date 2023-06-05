from django.views import View
from django.shortcuts import render

from .apriori import calculate_apriori
# from .models import Penjualan, ExcelFile
from .resources import PenjualanResource
from import_export.formats.base_formats import CSV, XLS, DEFAULT_FORMATS
from tablib import Dataset
# import pandas as pd


def home(request):
    return render(request, 'index.html')


class ImportPreviewView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        file = request.FILES['file']
        getsupport = request.POST.get('support')
        getconfidence = request.POST.get('confidence')

        file_extension = file.name.split('.')[-1].lower()
        # resource = PenjualanResource() #digunakan untuk menyimpan data kedalam sistem
        dataset = Dataset()

        if file_extension == 'csv':
            file_format = 'csv'
        elif file_extension == 'xlsx':
            file_format = 'xlsx'
        elif file_extension == 'xls':
            file_format = 'xls'
        else:
            return render(request, 'index.html', {'error_message': 'Format file tidak didukung.'})

        # resource = PenjualanResource()
        preview_data = dataset.load(file.read(), format=file_format)

        if ['Tanggal','ID Transaksi','Items'] != dataset.headers[:3]:
            return render(request, 'index.html', {'error_message': 'Format data tabel excel salah.'})


        result = calculate_apriori(df=preview_data.export(
            "df"), support=int(getsupport), confidence=int(getconfidence))
        

        return render(request, '_result.html', {'preview_data': preview_data, 'preview_head': result.head(2),'result_apriori': result, 'support': getsupport, 'confidence': getconfidence})

import requests
from django.shortcuts import render
from django.http import HttpResponse
from respons.utils import get_api_data, generate_pdf, create_zip_from_pdfs


def login_page(request):
    return render(request, "login.html")

def register_page(request):
    return render(request, 'register.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def download_zip_view(request):
    question_data = get_api_data()  # API'dan yoki boshqa manbadan ma'lumotlarni olish
    pdf_files = generate_pdf(question_data)

    # ZIP faylini yaratish
    zip_content = create_zip_from_pdfs(pdf_files)

    # ZIP faylini HTTP javobi sifatida yuborish
    response = HttpResponse(zip_content, content_type="application/zip")
    response['Content-Disposition'] = 'attachment; filename="questions.zip"'
    return response

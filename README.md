# E-Ticaret AI Projesi

Bu proje, yapay zeka kullanarak e-ticaret platformlarında görsel arama yapabilmeyi sağlayan bir uygulamadır.

## Projeyi Çalıştırma

### Backend

```bash
# Backend klasörüne geçin
cd ecommerce-ai/backend

# Python sanal ortamı oluşturun (ilk kez çalıştırırken)
python -m venv venv

# Sanal ortamı aktifleştirin:
# Windows için:
venv\Scripts\activate
# Linux/MacOS için:
# source venv/bin/activate

# Gerekli paketleri yükleyin
pip install -r requirements.txt

# Sunucuyu başlatın
python app.py
```

### Frontend

```bash
# Frontend klasörüne geçin
cd ecommerce-ai/frontend

# Bağımlılıkları yükleyin
npm install

# Geliştirme sunucusunu başlatın
npm start
```

## Notlar

- Backend sunucusu varsayılan olarak `http://localhost:5000` adresinde çalışır
- Frontend uygulaması varsayılan olarak `http://localhost:3000` adresinde çalışır
- Görsel arama için örnek resimler `test_images` klasöründe bulunmaktadır

## Özellikler

- Görsel arama teknolojisi
- Ürün öneri sistemi
- Akıllı kategorizasyon

## Kurulum

### Gereksinimler

- Python 3.7+
- Node.js 14+

### Backend Kurulumu

```bash
cd ecommerce-ai/backend
python -m venv venv
# Windows için:
venv\Scripts\activate
# Linux/MacOS için:
# source venv/bin/activate
pip install -r requirements.txt
```

### Frontend Kurulumu

```bash
cd ecommerce-ai/frontend
npm install
```

## Katkı Sağlama

Katkıda bulunmak istiyorsanız, lütfen [CONTRIBUTING.md](CONTRIBUTING.md) dosyasını inceleyin.

## Lisans

MIT 
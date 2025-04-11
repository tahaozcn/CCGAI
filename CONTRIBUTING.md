# Katkı Sağlama Rehberi

Bu proje için katkıda bulunurken lütfen aşağıdaki adımları takip edin.

## Geliştirme Süreci

1. İlgilendiğiniz konu için bir issue açın veya mevcut bir issue'ya atanın
2. Repository'yi fork edin
3. Kodunuzu geliştirin
4. Pull request (PR) açın

## Branching Stratejisi

- `main`: Kararlı sürüm, üretim ortamı için
- `develop`: Geliştirme süreci, özelliklerin birleştirildiği branch
- `feature/<özellik-adı>`: Yeni özellikler için
- `bugfix/<hata-adı>`: Hata düzeltmeleri için
- `hotfix/<acil-düzeltme>`: Üretim ortamı için acil düzeltmeler

## Commit Mesajları

Commit mesajları [Conventional Commits](https://www.conventionalcommits.org/) formatını takip etmelidir:

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

### Tipler:

- `feat`: Yeni özellikler
- `fix`: Hata düzeltmeleri
- `docs`: Dokümantasyon değişiklikleri
- `style`: Kod formatlaması, noktalama, isimlendirme vs. (kod değişikliği yok)
- `refactor`: Kod yeniden düzenleme (özellik ekleme veya hata düzeltme yok)
- `perf`: Performans iyileştirmeleri
- `test`: Test ekleme veya güncelleme
- `chore`: Derleme süreci veya yardımcı araçlar ve bağımlılıklarla ilgili değişiklikler

### Örnekler:

```
feat(auth): kullanıcı kayıt formuna telefon numarası ekle
fix(search): ürün arama algoritmasındaki performans sorunu giderildi
docs(readme): kurulum talimatları güncellendi
```

## Kod Stili ve Standartlar

### Python

- [PEP 8](https://www.python.org/dev/peps/pep-0008/) stil rehberini takip edin
- Docstring'ler için [Google tarzı](https://google.github.io/styleguide/pyguide.html) kullanın
- Kodunuzu `flake8` ile kontrol edin

### JavaScript/TypeScript

- [Airbnb JavaScript Stil Rehberi](https://github.com/airbnb/javascript) kullanın
- Kodunuzu ESLint ile kontrol edin

## Pull Request Süreci

1. PR açmadan önce kodunuzu düzgünce test edin
2. PR'ınızın tek bir amacı olmalı (örn. tek bir özellik veya hata düzeltmesi)
3. PR başlığı commit mesajı formatına uygun olmalı
4. PR açıldıktan sonra CI testleri geçmelidir
5. En az bir ekip üyesinin incelemesi ve onayı gereklidir

## Environment Değişkenleri

- Hassas bilgiler (API anahtarları, veritabanı bağlantıları) doğrudan koda yazılmamalı
- `.env.example` dosyasında gereken değişkenleri belirtin
- `.env` dosyasını `.gitignore` içinde tutun

## Soru ve Sorunlar

Herhangi bir sorunuz veya sorununuz olduğunda, repository'deki Issues bölümünü kullanın. 
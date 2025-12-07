# 📑 Alarm Waker - İçindekiler

Tüm rehberler ve dosyalar için hızlı erişim.

## 🚀 BAŞLAYANLAR İÇİN

1. **[BENIOKU.md](BENIOKU.md)** ⭐ - Türkçe ana rehber
2. **[QUICK_START.md](QUICK_START.md)** ⭐ - 5 dakikada başlayın
3. **[DOSYA_LISTESI.txt](DOSYA_LISTESI.txt)** - Tüm dosyaların listesi

## 📚 DETAYLI REHBERLER

### Firebase Kurulumu
- **[FIREBASE_SETUP.md](FIREBASE_SETUP.md)** - Firebase adım adım kurulum
  - Proje oluşturma
  - Android uygulaması kaydetme
  - Cloud Messaging API etkinleştirme
  - Credentials dosyaları indirme

### Tam Kurulum
- **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Detaylı kurulum rehberi
  - Android uygulaması derlemesi
  - Python kurulumu
  - Gönderici uygulaması kurulumu
  - Sorun giderme

### Kontrol Listesi
- **[CHECKLIST.md](CHECKLIST.md)** - Kurulum kontrol listesi
  - Firebase kontrolleri
  - Android kontrolleri
  - Python kontrolleri
  - Test kontrolleri

## 🏗️ TEKNIK DOKÜMANTASYON

- **[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)** - Proje yapısı
  - Dosya açıklamaları
  - Veri akışı diyagramı
  - Bağımlılıklar
  - Güvenlik

- **[README.md](README.md)** - İngilizce README
  - Proje özeti
  - Teknoloji stack
  - Kurulum özeti

## 📁 PROJE DOSYALARI

### Android Uygulaması
```
app/
├── build.gradle.kts
├── google-services.json (indirmeniz gerekli)
├── AndroidManifest.xml
└── src/main/
    ├── java/com/example/alarmwaker/
    │   ├── MainActivity.kt
    │   ├── service/
    │   │   ├── AlarmService.kt
    │   │   └── FirebaseMessagingService.kt
    │   ├── receiver/
    │   │   └── AlarmReceiver.kt
    │   └── ui/theme/
    │       ├── Theme.kt
    │       ├── Color.kt
    │       └── Type.kt
    └── res/
        └── values/
            ├── strings.xml
            └── themes.xml
```

### Python Gönderici
```
sender/
├── requirements.txt
├── send_alarm.py
├── web_sender.py
├── setup.bat
├── setup.sh
├── serviceAccountKey.json (indirmeniz gerekli)
└── templates/
    └── index.html
```

### Gradle Dosyaları
```
├── build.gradle.kts
├── settings.gradle.kts
└── proguard-rules.pro
```

## 🔄 KURULUM AKIŞI

```
1. BENIOKU.md veya QUICK_START.md oku
   ↓
2. FIREBASE_SETUP.md takip et
   ├─ Firebase projesi oluştur
   ├─ google-services.json indir
   └─ serviceAccountKey.json indir
   ↓
3. SETUP_GUIDE.md takip et
   ├─ Android uygulamasını derle
   ├─ Python kurulumunu yap
   └─ Gönderici uygulamasını başlat
   ↓
4. CHECKLIST.md ile kontrol et
   ├─ Tüm adımları doğrula
   └─ Test et
   ↓
5. Alarm gönder! 🔔
```

## 🎯 HIZLI BAĞLANTILAR

### Hızlı Başlangıç
- 5 dakikada başlamak: [QUICK_START.md](QUICK_START.md)
- Türkçe rehber: [BENIOKU.md](BENIOKU.md)

### Firebase
- Firebase kurulumu: [FIREBASE_SETUP.md](FIREBASE_SETUP.md)
- Firebase Console: https://console.firebase.google.com

### Kurulum
- Detaylı kurulum: [SETUP_GUIDE.md](SETUP_GUIDE.md)
- Kontrol listesi: [CHECKLIST.md](CHECKLIST.md)

### Teknik
- Proje yapısı: [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)
- İngilizce README: [README.md](README.md)

## ❓ SORUN GIDERME

Sorun yaşarsanız:

1. **[QUICK_START.md](QUICK_START.md)** - Hızlı çözümler
2. **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Detaylı sorun giderme
3. **[FIREBASE_SETUP.md](FIREBASE_SETUP.md)** - Firebase sorunları
4. **[CHECKLIST.md](CHECKLIST.md)** - Kontrol listesi

## 📊 DOSYA ÖZETI

| Dosya | Tür | Açıklama |
|-------|-----|----------|
| BENIOKU.md | 📖 | Türkçe ana rehber |
| QUICK_START.md | ⚡ | 5 dakikada başlayın |
| FIREBASE_SETUP.md | 🔥 | Firebase kurulumu |
| SETUP_GUIDE.md | 📚 | Detaylı kurulum |
| CHECKLIST.md | ✅ | Kontrol listesi |
| PROJECT_STRUCTURE.md | 🏗️ | Proje yapısı |
| README.md | 📄 | İngilizce README |
| INDEX.md | 📑 | Bu dosya |
| DOSYA_LISTESI.txt | 📋 | Dosya listesi |

## 🚀 BAŞLAYIN!

### Yeni Başlayanlar
1. [BENIOKU.md](BENIOKU.md) oku
2. [QUICK_START.md](QUICK_START.md) takip et

### Deneyimli Kullanıcılar
1. [FIREBASE_SETUP.md](FIREBASE_SETUP.md) takip et
2. [SETUP_GUIDE.md](SETUP_GUIDE.md) takip et

### Sorun Giderme
1. [CHECKLIST.md](CHECKLIST.md) kontrol et
2. [SETUP_GUIDE.md](SETUP_GUIDE.md) sorun giderme bölümünü oku

---

**Arkadaşınızı uyandırmaya hazır mısınız? 🔔**

Başlamak için: [BENIOKU.md](BENIOKU.md) veya [QUICK_START.md](QUICK_START.md)

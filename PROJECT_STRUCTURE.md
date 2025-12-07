# 📁 Proje Yapısı

```
yigit/
│
├── 📄 README.md                    # Proje hakkında
├── 📄 QUICK_START.md               # Hızlı başlangıç (5 dakika)
├── 📄 SETUP_GUIDE.md               # Detaylı kurulum rehberi
├── 📄 FIREBASE_SETUP.md            # Firebase kurulumu
├── 📄 PROJECT_STRUCTURE.md         # Bu dosya
│
├── 🔧 build.gradle.kts             # Gradle root konfigürasyonu
├── 🔧 settings.gradle.kts          # Gradle ayarları
├── 🔧 proguard-rules.pro           # Kod obfuskasyonu kuralları
├── 🔧 .gitignore                   # Git ignore dosyası
│
├── 📱 app/                         # Android Uygulaması
│   ├── 🔧 build.gradle.kts         # App Gradle konfigürasyonu
│   ├── 📄 google-services.json     # Firebase config (indirmeniz gerekli)
│   │
│   └── src/main/
│       ├── 📄 AndroidManifest.xml  # Android manifest
│       │
│       ├── java/com/example/alarmwaker/
│       │   ├── 🎯 MainActivity.kt                    # Ana ekran
│       │   │
│       │   ├── service/
│       │   │   ├── 🔔 AlarmService.kt               # Alarm sesi çalma
│       │   │   └── 📨 FirebaseMessagingService.kt   # FCM mesaj alma
│       │   │
│       │   ├── receiver/
│       │   │   └── 📡 AlarmReceiver.kt              # Alarm broadcast receiver
│       │   │
│       │   └── ui/theme/
│       │       ├── 🎨 Theme.kt                      # Material Design tema
│       │       ├── 🎨 Color.kt                      # Renkler
│       │       └── 🎨 Type.kt                       # Tipografi
│       │
│       └── res/
│           ├── values/
│           │   ├── strings.xml                      # Yazı kaynakları
│           │   └── themes.xml                       # Tema kaynakları
│           └── ... (drawable, layout, vb.)
│
└── 💻 sender/                      # Python Gönderici
    ├── 🔧 requirements.txt         # Python bağımlılıkları
    ├── 🔧 setup.bat                # Windows kurulum scripti
    ├── 🔧 setup.sh                 # Linux/Mac kurulum scripti
    │
    ├── 📄 serviceAccountKey.json   # Firebase credentials (indirmeniz gerekli)
    │
    ├── 🐍 send_alarm.py            # Komut satırı aracı
    ├── 🐍 web_sender.py            # Web sunucusu
    │
    └── templates/
        └── 🌐 index.html           # Web arayüzü
```

## 📋 Dosya Açıklamaları

### 🔧 Konfigürasyon Dosyaları

| Dosya | Açıklama |
|-------|----------|
| `build.gradle.kts` | Gradle root konfigürasyonu |
| `settings.gradle.kts` | Gradle modül ayarları |
| `app/build.gradle.kts` | Android uygulaması bağımlılıkları |
| `proguard-rules.pro` | Kod obfuskasyonu kuralları |
| `.gitignore` | Git tarafından yoksayılacak dosyalar |

### 📱 Android Uygulaması

| Dosya | Açıklama |
|-------|----------|
| `MainActivity.kt` | Ana ekran, FCM token gösterimi |
| `AlarmService.kt` | Alarm sesini çalma servisi |
| `FirebaseMessagingService.kt` | FCM mesajları alma ve işleme |
| `AlarmReceiver.kt` | Broadcast receiver, alarm tetikleme |
| `Theme.kt` | Material Design 3 tema |
| `Color.kt` | Renk paleti |
| `Type.kt` | Tipografi ayarları |

### 💻 Python Gönderici

| Dosya | Açıklama |
|-------|----------|
| `send_alarm.py` | Komut satırı aracı, etkileşimli mod |
| `web_sender.py` | Flask web sunucusu |
| `templates/index.html` | Web arayüzü (responsive) |
| `requirements.txt` | Python bağımlılıkları |
| `setup.bat` | Windows kurulum scripti |
| `setup.sh` | Linux/Mac kurulum scripti |

## 🔄 Veri Akışı

```
┌─────────────────────────────────────────────────────────────┐
│                    Gönderici (Python)                       │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Web Arayüzü (index.html)                            │   │
│  │  - Token girişi                                      │   │
│  │  - Alarm türü seçimi                                 │   │
│  │  - Süresi ayarlama                                   │   │
│  └──────────────────────────────────────────────────────┘   │
│                           ↓                                  │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Flask Web Sunucusu (web_sender.py)                  │   │
│  │  - /api/send-alarm endpoint                          │   │
│  │  - Firebase Admin SDK ile mesaj gönderme             │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                           ↓
                    Firebase Cloud Messaging
                           ↓
┌─────────────────────────────────────────────────────────────┐
│                  Alıcı (Android)                            │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  FirebaseMessagingService                            │   │
│  │  - FCM mesajını alır                                 │   │
│  │  - AlarmReceiver'ı tetikler                          │   │
│  └──────────────────────────────────────────────────────┘   │
│                           ↓                                  │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  AlarmReceiver                                       │   │
│  │  - Broadcast mesajı alır                             │   │
│  │  - AlarmService'i başlatır                           │   │
│  └──────────────────────────────────────────────────────┘   │
│                           ↓                                  │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  AlarmService                                        │   │
│  │  - Sistem alarm sesini çalar                         │   │
│  │  - Bildirim gösterir                                 │   │
│  │  - Belirtilen süre sonra durdurur                    │   │
│  └──────────────────────────────────────────────────────┘   │
│                           ↓                                  │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  🔔 Alarm Sesi                                       │   │
│  │  - Sistem alarm tonu çalar                           │   │
│  │  - Bildirim gösterilir                               │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

## 🔐 Güvenlik

- **Firebase Credentials**: `serviceAccountKey.json` - Gizli tutun!
- **FCM Token**: Cihaz tanımlayıcısı - Paylaşılabilir
- **Şifreleme**: Firebase Cloud Messaging tarafından otomatik

## 📦 Bağımlılıklar

### Android
- AndroidX Core, AppCompat
- Jetpack Compose (UI)
- Firebase Cloud Messaging
- Material Design 3

### Python
- firebase-admin (Firebase SDK)
- flask (Web framework)
- requests (HTTP client)
- python-dotenv (Ortam değişkenleri)

## 🚀 Çalıştırma

### Android
```bash
./gradlew installDebug
```

### Python Web
```bash
cd sender
python web_sender.py
```

### Python CLI
```bash
cd sender
python send_alarm.py "TOKEN"
```

## 📝 Lisans

MIT

---

**Daha fazla bilgi için [README.md](README.md) dosyasını okuyun.**

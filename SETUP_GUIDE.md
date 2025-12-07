# 🔔 Alarm Waker - Kurulum Rehberi

Arkadaşınızı uyandırmak için sistem kurulumu adım adım.

## 📋 Gereksinimler

- **Android Telefon** (API 24+)
- **Python 3.8+** (gönderici için)
- **Firebase Projesi**

---

## 1️⃣ Firebase Projesi Oluştur

### Adım 1: Firebase Console'a Git
1. https://console.firebase.google.com adresine gidin
2. Google hesabınızla giriş yapın
3. "Proje Oluştur" butonuna tıklayın

### Adım 2: Proje Ayarla
1. Proje adı: `AlarmWaker` (veya istediğiniz ad)
2. Google Analytics'i etkinleştirin (isteğe bağlı)
3. "Proje Oluştur" butonuna tıklayın

### Adım 3: Android Uygulamasını Kaydet
1. Firebase Console'da proje açılınca, Android ikonu tıklayın
2. **Paket adı**: `com.example.alarmwaker`
3. **Uygulama takma adı**: `AlarmWaker` (isteğe bağlı)
4. "Uygulamayı Kaydet" butonuna tıklayın
5. `google-services.json` dosyasını indirin
6. `app/` klasörüne yapıştırın

### Adım 4: Cloud Messaging Etkinleştir
1. Firebase Console'da sol menüden "Cloud Messaging" seçin
2. Sayfanın üstünde "Cloud Messaging API'sini etkinleştir" butonuna tıklayın

---

## 2️⃣ Android Uygulamasını Derle

### Adım 1: Android Studio'yu Aç
1. Android Studio'yu açın
2. "Open an existing Android Studio project" seçin
3. `yigit` klasörünü seçin

### Adım 2: Projeyi Derle
```bash
./gradlew build
```

### Adım 3: APK Oluştur
```bash
./gradlew assembleDebug
```

APK dosyası şu konumda oluşturulacak:
```
app/build/outputs/apk/debug/app-debug.apk
```

### Adım 4: Telefona Yükle
```bash
./gradlew installDebug
```

Veya APK dosyasını manuel olarak telefona aktarın.

---

## 3️⃣ Gönderici Uygulamasını Kur (Python)

### Adım 1: Firebase Credentials Dosyasını Oluştur

1. Firebase Console'da proje açın
2. ⚙️ **Proje Ayarları** > **Hizmet Hesapları** sekmesine gidin
3. **Python** sekmesini seçin
4. "Yeni özel anahtar oluştur" butonuna tıklayın
5. İndirilen JSON dosyasını `sender/` klasörüne `serviceAccountKey.json` olarak kaydedin

### Adım 2: Python Bağımlılıklarını Yükle

```bash
cd sender
pip install -r requirements.txt
```

---

## 4️⃣ Uygulamayı Kullan

### 📱 Alıcı Tarafında (Arkadaşınızın Telefonu)

1. Uygulamayı açın
2. **FCM Token** kısmını görün
3. Token'ı **kopyalayın** (uzun basın)
4. Gönderici kişiye gönderin

### 💻 Gönderici Tarafında (Sizin Bilgisayarınız)

#### Seçenek 1: Web Arayüzü (Kolay)

```bash
cd sender
python web_sender.py
```

Tarayıcıda açın: http://localhost:5000

1. FCM Token'ı yapıştırın
2. Alarm türünü seçin
3. "Alarm Gönder" butonuna tıklayın

#### Seçenek 2: Komut Satırı

```bash
cd sender
python send_alarm.py "FCM_TOKEN_BURAYA"
```

Örnek:
```bash
python send_alarm.py "eXxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" "loud" "60"
```

#### Seçenek 3: Etkileşimli Mod

```bash
cd sender
python send_alarm.py
```

Menüyü takip edin.

---

## 🔧 Sorun Giderme

### ❌ "FCM Token geçersiz" hatası
- Token'ı doğru kopyaladığınızdan emin olun
- Uygulamayı kapatıp açmayı deneyin
- İnternet bağlantısını kontrol edin

### ❌ "Firebase credentials bulunamadı"
- `serviceAccountKey.json` dosyasını `sender/` klasörüne koyduğunuzdan emin olun
- Dosya adını kontrol edin (büyük-küçük harf duyarlı)

### ❌ Alarm sesi çalmıyor
- Telefonun sesini açın
- Uygulamaya bildirim izni verin
- Android 13+ için "POST_NOTIFICATIONS" izni gerekli

### ❌ APK yüklenemiyor
```bash
# Cihazı bağlayın ve şunu çalıştırın
adb devices  # Cihazın listelenip listelenmediğini kontrol edin
./gradlew installDebug
```

---

## 📚 Dosya Yapısı

```
yigit/
├── app/                          # Android uygulaması
│   ├── src/main/
│   │   ├── java/com/example/alarmwaker/
│   │   │   ├── MainActivity.kt
│   │   │   ├── service/
│   │   │   │   ├── AlarmService.kt
│   │   │   │   └── FirebaseMessagingService.kt
│   │   │   └── receiver/
│   │   │       └── AlarmReceiver.kt
│   │   ├── AndroidManifest.xml
│   │   └── res/
│   ├── build.gradle.kts
│   └── google-services.json
├── sender/                       # Python gönderici
│   ├── send_alarm.py            # Komut satırı aracı
│   ├── web_sender.py            # Web sunucusu
│   ├── templates/
│   │   └── index.html           # Web arayüzü
│   ├── requirements.txt
│   └── serviceAccountKey.json   # Firebase credentials
├── build.gradle.kts
├── settings.gradle.kts
└── README.md
```

---

## 🎯 Alarm Türleri

| Tür | Açıklama |
|-----|----------|
| `default` | Normal alarm sesi |
| `gentle` | Hafif uyandırma |
| `loud` | Çok gürültülü |

---

## ⏱️ Alarm Süresi

- Minimum: 5 saniye
- Maksimum: 300 saniye (5 dakika)
- Varsayılan: 30 saniye

---

## 🔐 Güvenlik Notları

1. **serviceAccountKey.json** dosyasını paylaşmayın
2. FCM Token'ları güvenli bir şekilde iletin
3. Üretim ortamında daha güvenli kimlik doğrulama kullanın

---

## 📞 Destek

Sorun yaşarsanız:
1. Hata mesajını not edin
2. Sorun Giderme bölümünü kontrol edin
3. Firebase Console'da Cloud Messaging API'sinin etkinleştirildiğini doğrulayın

---

**Başarılar! 🚀**

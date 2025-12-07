# 🔥 Firebase Kurulum Rehberi

Firebase Cloud Messaging'i kurmak için adım adım rehber.

## 1️⃣ Firebase Projesi Oluştur

### Adım 1: Firebase Console'a Git
1. https://console.firebase.google.com adresine gidin
2. Google hesabınızla giriş yapın

### Adım 2: Yeni Proje Oluştur
1. "Proje Oluştur" butonuna tıklayın
2. Proje adı: **AlarmWaker** (veya istediğiniz ad)
3. Google Analytics'i etkinleştir (isteğe bağlı)
4. "Proje Oluştur" butonuna tıklayın

Proje oluşturulması 1-2 dakika sürebilir.

---

## 2️⃣ Android Uygulamasını Kaydet

### Adım 1: Android Uygulaması Ekle
1. Firebase Console'da proje açılınca, **Android ikonu** tıklayın
   - Veya: Proje Ayarları > Uygulamalarım > Android uygulaması ekle

### Adım 2: Bilgileri Girin
- **Android paket adı**: `com.example.alarmwaker`
- **Uygulama takma adı** (isteğe bağlı): `AlarmWaker`
- **SHA-1 parmak izi** (isteğe bağlı): Şimdilik boş bırakabilirsiniz

### Adım 3: google-services.json İndir
1. "google-services.json dosyasını indir" butonuna tıklayın
2. İndirilen dosyayı `app/` klasörüne kopyalayın

```
yigit/
└── app/
    └── google-services.json  ← Buraya koyun
```

### Adım 4: Kurulumu Tamamla
1. "Sonraki" butonuna tıklayın
2. Gradle bağımlılıkları zaten eklenmiş (build.gradle.kts'de)
3. "Kurulumu Tamamla" butonuna tıklayın

---

## 3️⃣ Cloud Messaging API'sini Etkinleştir

### Adım 1: API Sayfasına Git
1. Firebase Console'da sol menüden **"Cloud Messaging"** seçin
2. Sayfanın üstünde **"Cloud Messaging API'sini etkinleştir"** butonuna tıklayın

### Adım 2: Onay Ver
1. Google Cloud Console'a yönlendirileceksiniz
2. "Etkinleştir" butonuna tıklayın

Etkinleştirme 1-2 dakika sürebilir.

---

## 4️⃣ Hizmet Hesabı Oluştur (Python için)

### Adım 1: Hizmet Hesapları Sayfasına Git
1. Firebase Console'da proje açın
2. ⚙️ **Proje Ayarları** tıklayın
3. **"Hizmet Hesapları"** sekmesine gidin

### Adım 2: Python Credentials İndir
1. **"Python"** sekmesini seçin
2. **"Yeni özel anahtar oluştur"** butonuna tıklayın
3. Onay iletişinde "Oluştur" butonuna tıklayın
4. JSON dosyası otomatik olarak indirilecek

### Adım 3: Dosyayı Kopyala
İndirilen JSON dosyasını `sender/` klasörüne `serviceAccountKey.json` olarak kopyalayın:

```
yigit/
└── sender/
    └── serviceAccountKey.json  ← Buraya koyun
```

⚠️ **ÖNEMLİ**: Bu dosyayı hiç kimseyle paylaşmayın!

---

## 5️⃣ Doğrulama

### Android Uygulaması
```bash
# Proje klasöründe
./gradlew build
```

Hata yoksa ✅ tamamdır.

### Python Gönderici
```bash
cd sender
python send_alarm.py --help
```

Çıktı göstermişse ✅ tamamdır.

---

## 🔍 Sorun Giderme

### ❌ "google-services.json bulunamadı"
- Dosyayı `app/` klasörüne koyduğunuzdan emin olun
- Dosya adını kontrol edin (büyük-küçük harf duyarlı)

### ❌ "Cloud Messaging API etkinleştirilmedi"
1. Firebase Console > Proje Ayarları > Cloud Messaging
2. API'sini etkinleştir butonuna tıklayın
3. Google Cloud Console'da onaylayın

### ❌ "serviceAccountKey.json geçersiz"
1. Firebase Console > Proje Ayarları > Hizmet Hesapları
2. Yeni bir özel anahtar oluşturun
3. Eski dosyayı silin, yenisini kopyalayın

### ❌ "Alarm alınmıyor"
1. Android cihazda uygulamayı açın
2. FCM Token'ın göründüğünü kontrol edin
3. İnternet bağlantısını kontrol edin
4. Firebase Console > Cloud Messaging > Yayın Gönder ile test edin

---

## 📱 Firebase Console'dan Test

### Adım 1: Test Mesajı Gönder
1. Firebase Console > Cloud Messaging
2. "Yayın Gönder" butonuna tıklayın

### Adım 2: Hedef Seç
1. **Başlık**: "Test Alarm"
2. **Gövde**: "Bu bir test mesajıdır"

### Adım 3: Hedef Belirle
1. **Hedef**: "Uygulamalar" seçin
2. **Uygulama**: "AlarmWaker" seçin

### Adım 4: Gönder
1. "Gönder" butonuna tıklayın
2. Android cihazda bildirim alıp almadığını kontrol edin

---

## 📚 Faydalı Linkler

- [Firebase Console](https://console.firebase.google.com)
- [Firebase Dokümantasyonu](https://firebase.google.com/docs)
- [Cloud Messaging Rehberi](https://firebase.google.com/docs/cloud-messaging)
- [Android Kurulum](https://firebase.google.com/docs/android/setup)

---

## ✅ Kontrol Listesi

- [ ] Firebase projesi oluşturdum
- [ ] Android uygulamasını kaydettim
- [ ] google-services.json dosyasını indirdim ve app/ klasörüne koydum
- [ ] Cloud Messaging API'sini etkinleştirdim
- [ ] Hizmet hesabı oluşturdum
- [ ] serviceAccountKey.json dosyasını indirdim ve sender/ klasörüne koydum
- [ ] Android uygulamasını derledim
- [ ] Python bağımlılıklarını yükledim
- [ ] Firebase Console'dan test mesajı gönderdim

---

**Tamamlandı! 🎉 Şimdi [SETUP_GUIDE.md](SETUP_GUIDE.md) dosyasını okuyarak uygulamayı kullanmaya başlayabilirsiniz.**

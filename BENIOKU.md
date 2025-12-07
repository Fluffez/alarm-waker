# 🔔 Alarm Waker - Arkadaşını Uyandırma Sistemi

Kotlin ile yazılmış, Firebase Cloud Messaging kullanan uzaktan alarm sistemi.

## 🎯 Ne İşe Yarar?

- 📱 Arkadaşınızın telefonuna uzaktan alarm gönderin
- 🔊 Farklı alarm türleri seçin (normal, hafif, gürültülü)
- ⏱️ Alarm süresini özelleştirin
- 🌐 Web arayüzünden veya komut satırından gönderin
- 🔐 Firebase ile güvenli iletişim

## ⚡ Hızlı Başlangıç

**5 dakikada başlamak için**: [QUICK_START.md](QUICK_START.md) dosyasını okuyun.

## 📚 Rehberler

1. **[QUICK_START.md](QUICK_START.md)** - 5 dakikada başlayın
2. **[FIREBASE_SETUP.md](FIREBASE_SETUP.md)** - Firebase kurulumu
3. **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Detaylı kurulum
4. **[CHECKLIST.md](CHECKLIST.md)** - Kontrol listesi
5. **[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)** - Dosya yapısı

## 🚀 Kurulum Özeti

### 1. Firebase Kurulumu
```bash
# Firebase Console'da:
# 1. Proje oluştur
# 2. Android uygulamasını kaydet
# 3. google-services.json indir → app/ klasörüne koy
# 4. Cloud Messaging API'sini etkinleştir
# 5. serviceAccountKey.json indir → sender/ klasörüne koy
```

### 2. Android Uygulamasını Derle
```bash
./gradlew installDebug
```

### 3. Python Kurulumu
```bash
cd sender
pip install -r requirements.txt
```

### 4. Alarm Gönder
```bash
# Web arayüzü
python web_sender.py
# Tarayıcıda: http://localhost:5000

# Veya komut satırı
python send_alarm.py "FCM_TOKEN"
```

## 📱 Nasıl Kullanılır?

### Arkadaşınızın Telefonu (Alıcı)
1. Uygulamayı açın
2. FCM Token'ı kopyalayın
3. Size gönderin

### Sizin Bilgisayarınız (Gönderici)
1. Token'ı yapıştırın
2. Alarm türünü seçin
3. "Alarm Gönder" butonuna tıklayın
4. 🔔 Alarm çalsın!

## 🛠️ Teknoloji

- **Android**: Kotlin, Jetpack Compose, Firebase Cloud Messaging
- **Backend**: Python, Flask, Firebase Admin SDK
- **İletişim**: Firebase Cloud Messaging (FCM)

## 📁 Proje Yapısı

```
yigit/
├── app/                    # Android uygulaması
├── sender/                 # Python gönderici
├── QUICK_START.md         # Hızlı başlangıç
├── FIREBASE_SETUP.md      # Firebase kurulumu
├── SETUP_GUIDE.md         # Detaylı kurulum
└── README.md              # İngilizce README
```

## ❓ Sık Sorulan Sorular

### Alarm sesi çalmıyor?
- Telefonun sesini açın
- Uygulamaya bildirim izni verin
- Uygulamayı kapatıp açmayı deneyin

### Token alınamıyor?
- İnternet bağlantısını kontrol edin
- Uygulamayı kapatıp açmayı deneyin
- Firebase Console'da Cloud Messaging API'sinin etkinleştirildiğini kontrol edin

### "Firebase credentials bulunamadı"?
- `serviceAccountKey.json` dosyasını `sender/` klasörüne koyun
- Dosya adını kontrol edin

### Daha fazla sorun?
[SETUP_GUIDE.md](SETUP_GUIDE.md) dosyasındaki "Sorun Giderme" bölümünü okuyun.

## 🔐 Güvenlik

- Firebase Cloud Messaging ile şifreli iletişim
- Özel anahtarlar güvenli şekilde saklanır
- Token tabanlı kimlik doğrulama

⚠️ **ÖNEMLİ**: `serviceAccountKey.json` dosyasını hiç kimseyle paylaşmayın!

## 📝 Lisans

MIT

## 🤝 Katkı

Geliştirmeler ve hata raporları için pull request gönderin!

---

## 📞 Destek

Sorun yaşarsanız:
1. [QUICK_START.md](QUICK_START.md) - Hızlı başlangıç
2. [SETUP_GUIDE.md](SETUP_GUIDE.md) - Detaylı rehber
3. [FIREBASE_SETUP.md](FIREBASE_SETUP.md) - Firebase sorunları

---

**Arkadaşınızı uyandırmaya hazır mısınız? 🚀**

Başlamak için: [QUICK_START.md](QUICK_START.md)

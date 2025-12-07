# ⚡ Hızlı Başlangıç

## 1. Firebase Konfigürasyonu (5 dakika)

1. https://console.firebase.google.com/ adresine gidin
2. Yeni proje oluşturun
3. Realtime Database oluşturun
4. Web uygulaması ekleyin
5. Konfigürasyon kodunu kopyalayın

## 2. HTML Dosyasını Güncelle

`index.html` dosyasında bu satırları bulun (satır ~475):

```javascript
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_AUTH_DOMAIN",
    databaseURL: "YOUR_DATABASE_URL",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_STORAGE_BUCKET",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID"
};
```

Firebase Console'dan aldığın değerleri yapıştır.

## 3. Test Et

`index.html` dosyasını tarayıcıda aç:
- 4 profili göreceksin
- "✏️ Düzenle" ile profilleri özelleştir
- "🔔 Uyandır" ile alarm gönder

## 4. Android'e Entegre Et

`ALARM_SETUP.md` dosyasında Android entegrasyon adımlarını takip et.

## Sistem Nasıl Çalışır?

```
Telefon A                    Firebase                    Telefon B
┌─────────────┐             ┌─────────┐              ┌─────────────┐
│ "Uyandır"   │────────────→│ Alarmlar│─────────────→│ Alarm Çalar │
│ Tuşuna Tıkla│             │ Veritab.│              │ Ses + Titreş │
└─────────────┘             └─────────┘              └─────────────┘
```

## Dosya Yapısı

```
yigit/
├── index.html              # Ana uygulama (bu dosyayı kullan)
├── ALARM_SETUP.md          # Detaylı kurulum rehberi
├── QUICK_START.md          # Bu dosya
├── MainActivity.kt         # Android kodu
├── activity_main.xml       # Android layout
└── AndroidManifest.xml     # Android manifest
```

## Önemli Noktalar

✅ **Giriş sistemi yok** - Direkt 4 profil görsün
✅ **Kişiselleştirme** - Her profili düzenleyebilir
✅ **Gerçek zamanlı** - Firebase ile senkronize
✅ **Mobil uyumlu** - Android'e entegre edilebilir

## Sorun Giderme

| Sorun | Çözüm |
|-------|-------|
| Alarm gelmiyorsa | Firebase konfigürasyonunu kontrol et |
| Ses çalmıyorsa | Cihazın sesini aç, browser izni ver |
| Profiller kaydedilmiyorsa | localStorage'ı kontrol et |

## Sonraki Adımlar

1. ✅ Firebase konfigürasyonunu tamamla
2. ✅ HTML'i test et
3. ✅ Android Studio'da proje oluştur
4. ✅ Dosyaları kopyala
5. ✅ APK oluştur ve yükle

**Hazırsan başlayalım!** 🚀

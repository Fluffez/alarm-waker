# 📱 Android Studio ile Derleme

Gradle wrapper dosyası eksik olduğu için Android Studio kullanacağız.

## 🚀 Adım 1: Android Studio'yu Aç

1. Android Studio'yu açın
2. "Open an existing Android Studio project" seçin
3. Klasör seçin: `c:\Users\kapta\Downloads\yigit`
4. Projeyi aç

## 🔧 Adım 2: Gradle Senkronizasyonu

Android Studio açıldığında otomatik olarak Gradle senkronizasyonu başlayacak.

**Eğer başlamadıysa:**
1. Üst menüden: File > Sync Now
2. Veya: Ctrl + Alt + Y

## 📦 Adım 3: Projeyi Derle

### Seçenek A: Menüden
1. Build > Make Project
2. Veya: Ctrl + F9

### Seçenek B: Terminal'den (Android Studio içinde)
1. Alt + F12 (Terminal aç)
2. Şu komutu çalıştır:
```bash
./gradlew build
```

## 📲 Adım 4: APK Oluştur

### Seçenek A: Menüden
1. Build > Build Bundle(s) / APK(s) > Build APK(s)

### Seçenek B: Terminal'den
```bash
./gradlew assembleDebug
```

## 📱 Adım 5: Telefona Yükle

### USB ile Yükleme
1. Android telefonunuzu USB kablosu ile bağlayın
2. Telefonda "USB Hata Ayıklaması"nı etkinleştirin
3. Android Studio'da: Run > Run 'app'
4. Veya: Shift + F10

### APK Dosyasını Manuel Yükleme
1. APK dosyasını bul:
   ```
   app/build/outputs/apk/debug/app-debug.apk
   ```
2. Telefona aktar
3. Dosya Yöneticisinde aç ve yükle

## ✅ Kontrol Listesi

- [ ] Android Studio açtım
- [ ] Projeyi açtım
- [ ] Gradle senkronizasyonu tamamlandı
- [ ] Projeyi derledim
- [ ] APK oluşturdum
- [ ] Telefona yükledim
- [ ] Uygulamayı açtım
- [ ] FCM Token'ı gördüm

## 🎯 Sonraki Adım

Uygulamayı açtıktan sonra:
1. FCM Token'ı kopyalayın
2. Web sunucusunu başlatın: `python web_sender.py`
3. Tarayıcıda: `http://localhost:5000`
4. Token'ı yapıştırıp alarm gönderin!

---

**Sorun yaşarsanız**: SETUP_GUIDE.md dosyasındaki sorun giderme bölümünü okuyun.

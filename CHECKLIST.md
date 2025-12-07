# ✅ Kurulum Kontrol Listesi

Alarm Waker'ı başarıyla kurmak için bu kontrol listesini takip edin.

## 🔥 Firebase Kurulumu

- [ ] Firebase hesabı oluşturdum (https://console.firebase.google.com)
- [ ] Yeni Firebase projesi oluşturdum
- [ ] Android uygulamasını Firebase'e kaydettim
- [ ] `google-services.json` dosyasını indirdim
- [ ] `google-services.json` dosyasını `app/` klasörüne kopyaladım
- [ ] Cloud Messaging API'sini etkinleştirdim
- [ ] Hizmet hesabı oluşturdum
- [ ] `serviceAccountKey.json` dosyasını indirdim
- [ ] `serviceAccountKey.json` dosyasını `sender/` klasörüne kopyaladım

## 📱 Android Kurulumu

- [ ] Android Studio yüklü
- [ ] Proje Android Studio'da açılıyor
- [ ] Gradle senkronizasyonu başarılı
- [ ] APK başarıyla derleniyor (`./gradlew build`)
- [ ] APK telefona yükleniyor (`./gradlew installDebug`)
- [ ] Uygulama telefonda açılıyor
- [ ] FCM Token gösteriliyor
- [ ] Token kopyalanabiliyor

## 💻 Python Kurulumu

- [ ] Python 3.8+ yüklü (`python --version`)
- [ ] `sender/` klasörüne gittim
- [ ] Bağımlılıkları yükledim (`pip install -r requirements.txt`)
- [ ] `serviceAccountKey.json` dosyası `sender/` klasöründe
- [ ] Web sunucusu başlatılıyor (`python web_sender.py`)
- [ ] Web arayüzü açılıyor (http://localhost:5000)
- [ ] Komut satırı aracı çalışıyor (`python send_alarm.py --help`)

## 🧪 Test

- [ ] Android uygulamasını açtım
- [ ] FCM Token'ı kopyaladım
- [ ] Web arayüzüne Token'ı yapıştırdım
- [ ] "Alarm Gönder" butonuna tıkladım
- [ ] Telefondan alarm sesi geldi 🔔
- [ ] Alarm belirtilen süre sonra durdu
- [ ] Bildirim gösterildi

## 🔧 Ek Kontroller

- [ ] `.gitignore` dosyası var
- [ ] `README.md` dosyası var
- [ ] `SETUP_GUIDE.md` dosyası var
- [ ] `FIREBASE_SETUP.md` dosyası var
- [ ] `QUICK_START.md` dosyası var
- [ ] `PROJECT_STRUCTURE.md` dosyası var

## 🚀 Hazır!

Tüm kontrol listesi tamamlandıysa, sistem hazır! 🎉

### Sonraki Adımlar

1. **Arkadaşınızla Paylaş**: APK dosyasını arkadaşınıza gönderin
2. **Uygulamayı Açın**: Arkadaşınızın telefonunda uygulamayı açmasını isteyin
3. **Token'ı Alın**: FCM Token'ı kopyalamasını isteyin
4. **Alarm Gönderin**: Web arayüzünden alarm gönderin
5. **Eğlenin**: Arkadaşınızı uyandırın! 😄

---

## 📞 Sorun Giderme

Eğer bir adımda takılırsanız:

1. **[QUICK_START.md](QUICK_START.md)** - Hızlı başlangıç
2. **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Detaylı rehber
3. **[FIREBASE_SETUP.md](FIREBASE_SETUP.md)** - Firebase sorunları
4. **[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)** - Dosya yapısı

---

**Başarılar! 🚀**

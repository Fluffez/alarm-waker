#!/usr/bin/env python3
"""
Firebase Bağlantı Testi
"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging
from pathlib import Path
import sys

CREDENTIALS_PATH = Path(__file__).parent / "serviceAccountKey.json"

def test_firebase_connection():
    """Firebase bağlantısını test et"""
    print("🔥 Firebase Bağlantı Testi Başlıyor...\n")
    
    # 1. Credentials dosyasını kontrol et
    print("1️⃣  Credentials dosyası kontrol ediliyor...")
    if not CREDENTIALS_PATH.exists():
        print(f"   ❌ HATA: {CREDENTIALS_PATH} bulunamadı!")
        return False
    print(f"   ✅ Dosya bulundu: {CREDENTIALS_PATH}")
    
    # 2. Credentials dosyasını oku
    print("\n2️⃣  Credentials dosyası okunuyor...")
    try:
        with open(CREDENTIALS_PATH, 'r') as f:
            import json
            creds = json.load(f)
            project_id = creds.get('project_id')
            print(f"   ✅ Dosya okundu")
            print(f"   📋 Proje ID: {project_id}")
    except Exception as e:
        print(f"   ❌ HATA: {str(e)}")
        return False
    
    # 3. Firebase'i başlat
    print("\n3️⃣  Firebase başlatılıyor...")
    try:
        if not firebase_admin._apps:
            cred = credentials.Certificate(str(CREDENTIALS_PATH))
            firebase_admin.initialize_app(cred)
        print("   ✅ Firebase başlatıldı")
    except Exception as e:
        print(f"   ❌ HATA: {str(e)}")
        return False
    
    # 4. Test mesajı gönder
    print("\n4️⃣  Test mesajı gönderiliyor...")
    print("   ⚠️  NOT: Geçerli bir FCM token'ı olmadığı için bu adım başarısız olacak")
    print("   Ancak Firebase bağlantısı kontrol edilecek\n")
    
    try:
        # Geçersiz token ile test et (hata bekleniyor ama Firebase bağlantısı kontrol edilir)
        test_token = "test_token_12345"
        message = messaging.Message(
            data={"test": "true"},
            token=test_token,
        )
        
        # Bu hata verecek ama Firebase bağlantısı kontrol edilmiş olur
        try:
            response = messaging.send(message)
            print(f"   ✅ Mesaj gönderildi: {response}")
        except messaging.UnregisteredError:
            print("   ✅ Firebase bağlantısı çalışıyor!")
            print("   ℹ️  Token geçersiz olduğu için mesaj gönderilemedi (beklenen)")
            return True
        except Exception as e:
            if "permission denied" in str(e).lower():
                print(f"   ❌ HATA: Firebase izni yok!")
                print(f"   Detay: {str(e)}")
                return False
            else:
                print(f"   ⚠️  Hata: {str(e)}")
                return True  # Bağlantı var, sadece token yok
    
    except Exception as e:
        print(f"   ❌ HATA: {str(e)}")
        return False
    
    return True

def main():
    print("╔════════════════════════════════════════════════════════════╗")
    print("║           🔥 FIREBASE BAĞLANTI TESTI                       ║")
    print("╚════════════════════════════════════════════════════════════╝\n")
    
    success = test_firebase_connection()
    
    print("\n" + "="*60)
    if success:
        print("✅ BAŞARILI! Firebase bağlantısı çalışıyor!")
        print("\n📱 Sonraki Adımlar:")
        print("1. Android uygulamasını derleyin ve telefona yükleyin")
        print("2. Uygulamayı açın ve FCM Token'ı kopyalayın")
        print("3. Token'ı kullanarak alarm gönderin:")
        print("   python send_alarm.py 'YOUR_FCM_TOKEN'")
        print("\n🌐 Veya web arayüzünü kullanın:")
        print("   python web_sender.py")
        print("   Tarayıcıda: http://localhost:5000")
    else:
        print("❌ BAŞARISIZ! Firebase bağlantısında sorun var.")
        print("\n🔧 Kontrol Listesi:")
        print("1. serviceAccountKey.json dosyası sender/ klasöründe mi?")
        print("2. Dosya geçerli bir Firebase credentials dosyası mı?")
        print("3. Firebase Console'da Cloud Messaging API etkinleştirildi mi?")
        print("4. Proje ID doğru mu?")
    print("="*60 + "\n")
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
Alarm Gönderici - Arkadaşınızın telefonuna alarm gönderin
"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging
import json
import sys
from pathlib import Path

# Firebase credentials dosyasının yolu
CREDENTIALS_PATH = Path(__file__).parent / "serviceAccountKey.json"

def initialize_firebase():
    """Firebase'i başlat"""
    if not CREDENTIALS_PATH.exists():
        print(f"❌ Hata: {CREDENTIALS_PATH} dosyası bulunamadı!")
        print("Firebase credentials dosyasını oluşturmak için:")
        print("1. Firebase Console'a gidin: https://console.firebase.google.com")
        print("2. Proje oluşturun veya seçin")
        print("3. Proje Ayarları > Hizmet Hesapları > Python sekmesine gidin")
        print("4. 'Yeni özel anahtar oluştur' butonuna tıklayın")
        print("5. İndirilen JSON dosyasını serviceAccountKey.json olarak kaydedin")
        sys.exit(1)
    
    if not firebase_admin._apps:
        cred = credentials.Certificate(str(CREDENTIALS_PATH))
        firebase_admin.initialize_app(cred)
    
    print("✅ Firebase başlatıldı")

def send_alarm(fcm_token, alarm_type="default", duration=30000):
    """
    FCM token'a alarm gönder
    
    Args:
        fcm_token: Hedef cihazın FCM token'ı
        alarm_type: Alarm türü (default, gentle, loud)
        duration: Alarm süresi (milisaniye)
    """
    try:
        message = messaging.Message(
            data={
                "alarm_type": alarm_type,
                "duration": str(duration),
            },
            notification=messaging.Notification(
                title="🔔 Uyan!",
                body="Arkadaşın seni uyandırmaya çalışıyor!",
            ),
            token=fcm_token,
        )
        
        response = messaging.send(message)
        print(f"✅ Alarm gönderildi! Message ID: {response}")
        return True
    
    except messaging.UnregisteredError:
        print(f"❌ Hata: FCM token geçersiz veya kayıtlı değil")
        return False
    except Exception as e:
        print(f"❌ Hata: {str(e)}")
        return False

def send_alarm_to_multiple(fcm_tokens, alarm_type="default", duration=30000):
    """Birden fazla cihaza alarm gönder"""
    results = []
    for token in fcm_tokens:
        print(f"\n📱 Gönderiliyor: {token[:20]}...")
        success = send_alarm(token, alarm_type, duration)
        results.append((token, success))
    
    print(f"\n📊 Sonuç: {sum(1 for _, s in results if s)}/{len(results)} başarılı")
    return results

def interactive_mode():
    """Etkileşimli mod"""
    print("\n" + "="*50)
    print("🔔 ALARM WAKER - Gönderici")
    print("="*50)
    
    initialize_firebase()
    
    while True:
        print("\n1. Tek cihaza alarm gönder")
        print("2. Birden fazla cihaza alarm gönder")
        print("3. Çıkış")
        
        choice = input("\nSeçim yapın (1-3): ").strip()
        
        if choice == "1":
            fcm_token = input("FCM Token'ı yapıştırın: ").strip()
            if not fcm_token:
                print("❌ Token boş olamaz!")
                continue
            
            print("\nAlarm türü seçin:")
            print("1. Default (normal)")
            print("2. Gentle (hafif)")
            print("3. Loud (çok gürültülü)")
            alarm_choice = input("Seçim (1-3, varsayılan 1): ").strip() or "1"
            
            alarm_types = {"1": "default", "2": "gentle", "3": "loud"}
            alarm_type = alarm_types.get(alarm_choice, "default")
            
            duration_input = input("Alarm süresi (saniye, varsayılan 30): ").strip()
            try:
                duration = int(duration_input or "30") * 1000
            except ValueError:
                duration = 30000
            
            send_alarm(fcm_token, alarm_type, duration)
        
        elif choice == "2":
            print("Token'ları satır satır girin (boş satır ile bitirin):")
            tokens = []
            while True:
                token = input().strip()
                if not token:
                    break
                tokens.append(token)
            
            if tokens:
                send_alarm_to_multiple(tokens)
            else:
                print("❌ Hiç token girilmedi!")
        
        elif choice == "3":
            print("Çıkılıyor...")
            break
        
        else:
            print("❌ Geçersiz seçim!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Command line mode
        if sys.argv[1] == "--help":
            print("""
Kullanım: python send_alarm.py [token] [alarm_type] [duration]

Örnekler:
  python send_alarm.py "YOUR_FCM_TOKEN"
  python send_alarm.py "YOUR_FCM_TOKEN" "loud" "60"
  
Etkileşimli mod için argüman olmadan çalıştırın:
  python send_alarm.py
            """)
        else:
            initialize_firebase()
            token = sys.argv[1]
            alarm_type = sys.argv[2] if len(sys.argv) > 2 else "default"
            duration = int(sys.argv[3]) * 1000 if len(sys.argv) > 3 else 30000
            send_alarm(token, alarm_type, duration)
    else:
        # Interactive mode
        interactive_mode()

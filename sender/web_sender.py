#!/usr/bin/env python3
"""
Web Arayüzü - Tarayıcıdan alarm gönderin
"""

from flask import Flask, render_template, request, jsonify
import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging
from pathlib import Path
import json

app = Flask(__name__)
CREDENTIALS_PATH = Path(__file__).parent / "serviceAccountKey.json"

def initialize_firebase():
    """Firebase'i başlat"""
    if not firebase_admin._apps:
        if not CREDENTIALS_PATH.exists():
            raise FileNotFoundError(f"Firebase credentials bulunamadı: {CREDENTIALS_PATH}")
        cred = credentials.Certificate(str(CREDENTIALS_PATH))
        firebase_admin.initialize_app(cred)

@app.route('/')
def index():
    """Ana sayfa"""
    return render_template('index.html')

@app.route('/api/send-alarm', methods=['POST'])
def send_alarm():
    """Alarm gönder API endpoint"""
    try:
        data = request.json
        fcm_token = data.get('token', '').strip()
        alarm_type = data.get('alarm_type', 'default')
        duration = int(data.get('duration', 30)) * 1000
        
        if not fcm_token:
            return jsonify({'success': False, 'error': 'Token gerekli'}), 400
        
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
        return jsonify({
            'success': True,
            'message_id': response,
            'message': 'Alarm başarıyla gönderildi!'
        })
    
    except messaging.UnregisteredError:
        return jsonify({
            'success': False,
            'error': 'FCM token geçersiz veya kayıtlı değil'
        }), 400
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    try:
        initialize_firebase()
        print("✅ Firebase başlatıldı")
        print("🌐 Web sunucusu başlatılıyor: http://localhost:5000")
        app.run(debug=True, host='0.0.0.0', port=5000)
    except FileNotFoundError as e:
        print(f"❌ Hata: {e}")
        print("\nFirebase credentials dosyasını oluşturmak için:")
        print("1. Firebase Console'a gidin: https://console.firebase.google.com")
        print("2. Proje oluşturun veya seçin")
        print("3. Proje Ayarları > Hizmet Hesapları > Python sekmesine gidin")
        print("4. 'Yeni özel anahtar oluştur' butonuna tıklayın")
        print("5. İndirilen JSON dosyasını serviceAccountKey.json olarak kaydedin")

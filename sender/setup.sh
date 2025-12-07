#!/bin/bash

# Alarm Waker - Python Kurulum Scripti (Linux/Mac)

echo ""
echo "========================================"
echo "  Alarm Waker - Kurulum"
echo "========================================"
echo ""

# Python kontrolü
if ! command -v python3 &> /dev/null; then
    echo "[HATA] Python 3 yüklü değil!"
    echo "Lütfen Python 3.8+ yükleyin: https://www.python.org/downloads/"
    exit 1
fi

echo "[OK] Python bulundu: $(python3 --version)"
echo ""

# Bağımlılıkları yükle
echo "[KURULUM] Bağımlılıklar yükleniyor..."
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "[HATA] Bağımlılıklar yüklenemedi!"
    exit 1
fi

echo ""
echo "[OK] Kurulum tamamlandı!"
echo ""
echo "Şimdi yapmanız gerekenler:"
echo "1. Firebase Console'dan serviceAccountKey.json indirin"
echo "2. Bu klasöre serviceAccountKey.json dosyasını koyun"
echo "3. Web sunucusunu başlatmak için: python3 web_sender.py"
echo "4. Komut satırından göndermek için: python3 send_alarm.py"
echo ""

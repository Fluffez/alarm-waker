@echo off
REM Alarm Waker - Python Kurulum Scripti (Windows)

echo.
echo ========================================
echo   Alarm Waker - Kurulum
echo ========================================
echo.

REM Python kontrolü
python --version >nul 2>&1
if errorlevel 1 (
    echo [HATA] Python yüklü değil!
    echo Lütfen Python 3.8+ yükleyin: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [OK] Python bulundu
echo.

REM Bağımlılıkları yükle
echo [KURULUM] Bağımlılıklar yükleniyor...
pip install -r requirements.txt

if errorlevel 1 (
    echo [HATA] Bağımlılıklar yüklenemedi!
    pause
    exit /b 1
)

echo.
echo [OK] Kurulum tamamlandı!
echo.
echo Şimdi yapmanız gerekenler:
echo 1. Firebase Console'dan serviceAccountKey.json indirin
echo 2. Bu klasöre serviceAccountKey.json dosyasını koyun
echo 3. Web sunucusunu başlatmak için: python web_sender.py
echo 4. Komut satırından göndermek için: python send_alarm.py
echo.
pause

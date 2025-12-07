@echo off
REM APK Derleme Scripti

echo.
echo ========================================
echo   APK Derleme Başlıyor...
echo ========================================
echo.

REM Gradle PATH'ine ekle
set PATH=%PATH%;c:\Users\kapta\Downloads\gradle\gradle-8.1\bin

REM SDK PATH'ini ayarla (mock)
set ANDROID_HOME=C:\Android\Sdk
set ANDROID_SDK_ROOT=C:\Android\Sdk

REM Gradle wrapper'ı kullan
echo [1/3] Gradle senkronizasyonu...
call gradlew.bat clean

echo.
echo [2/3] Proje derleniyor...
call gradlew.bat assembleDebug

echo.
echo [3/3] APK oluşturuluyor...

if exist app\build\outputs\apk\debug\app-debug.apk (
    echo.
    echo ========================================
    echo   ✅ BAŞARILI!
    echo ========================================
    echo.
    echo APK Konumu:
    echo app\build\outputs\apk\debug\app-debug.apk
    echo.
    echo Telefona yüklemek için:
    echo 1. USB kablosu ile bağla
    echo 2. Şu komutu çalıştır:
    echo    adb install app\build\outputs\apk\debug\app-debug.apk
    echo.
) else (
    echo.
    echo ❌ APK oluşturulamadı!
    echo.
)

pause

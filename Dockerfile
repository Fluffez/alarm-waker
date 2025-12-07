FROM ubuntu:22.04

# Android SDK ve araçlarını yükle
RUN apt-get update && apt-get install -y \
    openjdk-11-jdk \
    wget \
    unzip \
    git \
    && rm -rf /var/lib/apt/lists/*

# Android SDK'yı indir
RUN mkdir -p /opt/android-sdk && \
    cd /opt/android-sdk && \
    wget https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip && \
    unzip -q commandlinetools-linux-11076708_latest.zip && \
    rm commandlinetools-linux-11076708_latest.zip

# Gradle'ı indir
RUN mkdir -p /opt/gradle && \
    cd /opt/gradle && \
    wget https://services.gradle.org/distributions/gradle-8.1-bin.zip && \
    unzip -q gradle-8.1-bin.zip && \
    rm gradle-8.1-bin.zip

# PATH'i ayarla
ENV PATH="/opt/gradle/gradle-8.1/bin:/opt/android-sdk/cmdline-tools/bin:${PATH}"
ENV ANDROID_HOME="/opt/android-sdk"
ENV ANDROID_SDK_ROOT="/opt/android-sdk"

# Lisansları kabul et
RUN mkdir -p /opt/android-sdk/licenses && \
    echo "8403405891b13fb1386efa617eac4d0b123720f4" > /opt/android-sdk/licenses/android-sdk-license && \
    echo "d56f5187479451eabf01fb78af6dfcb131b33910" >> /opt/android-sdk/licenses/android-sdk-license && \
    echo "24333f8a63b6825ea9c5514f83c2829b004d1fee" >> /opt/android-sdk/licenses/android-sdk-license

# Projeyi kopyala
COPY . /app
WORKDIR /app

# APK'yı derle
RUN gradle assembleDebug

# APK'yı output'a kopyala
RUN cp app/build/outputs/apk/debug/app-debug.apk /app/app-debug.apk

CMD ["tail", "-f", "/dev/null"]

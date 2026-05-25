# BVA5108 - AI Destekli Ağ Güvenlik Tarayıcı Aracı

**Öğrenci No:** 2421310057
**Ad Soyad:** Rümeysa Gülsuyu
**Seçilen Ek Modül:** M4 (Aktif Cihaz Keşfi)
**Kullanılan AI API:** Google Gemini 2.5 Flash

## Proje Hakkında
Bu proje, Siber Güvenlik dersi final ödevi kapsamında geliştirilmiş Python tabanlı bir ağ güvenlik tarayıcıdır. Araç, hedef makinedeki (Örn: DVWA) açık portları tespit eder (M1), ağdaki cihazların MAC adreslerini bulur (M4) ve elde ettiği tüm bulguları Google Gemini yapay zekasına göndererek Türkçe bir güvenlik risk analizi ve çözüm raporu üretir. Tüm veriler şık bir HTML dosyasına kaydedilir.

## Kurulum Adımları
Projeyi çalıştırmak için Kali Linux veya benzeri bir Debian tabanlı sistem gereklidir.

1. **Gereksinimleri Yükleyin:**
Sisteminizde Nmap'in yüklü olduğundan emin olun:
`sudo apt update && sudo apt install nmap -y`

2. **Python Kütüphanelerini Kurun:**
`sudo pip3 install -r requirements.txt --break-system-packages`

3. **API Anahtarını Ayarlayın:**
Proje dizininde `.env` adında gizli bir dosya oluşturun ve içine Google AI Studio'dan aldığınız API anahtarınızı şu formatta ekleyin:
`GEMINI_API_KEY="Sizin_API_Anahtariniz"`

## Kullanım
Aracın port taraması ve MAC adresi tespiti yapabilmesi için yönetici (`sudo`) yetkileriyle çalıştırılması zorunludur.

`sudo python3 main.py`

Çalıştırdığınızda araç sizden bir IP adresi isteyecektir (Örn: `127.0.0.1` veya hedef makinenin IP adresi). IP girildikten sonra tarama ve analiz otomatik olarak başlayacak, sonuçlar terminale yazdırılacak ve `guvenlik_raporu.html` olarak klasöre kaydedilecektir.

## Ekran Görüntüleri
<img width="1920" height="1080" alt="Ekran Görüntüsü (1390)" src="https://github.com/user-attachments/assets/e2557a3e-bc60-46f6-a96c-c1ac980e217b" />
<img width="1920" height="1080" alt="Ekran Görüntüsü (1388)" src="https://github.com/user-attachments/assets/498386a3-489c-40de-8b37-e20af0978dca" />
<img width="1920" height="1080" alt="Ekran Görüntüsü (1387)" src="https://github.com/user-attachments/assets/2074f4c7-b73d-48c6-83fb-5a3dc8bf3409" />


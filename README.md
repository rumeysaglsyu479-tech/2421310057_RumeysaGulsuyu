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
<img width="1920" height="1080" alt="Ekran Görüntüsü (1433)" src="https://github.com/user-attachments/assets/ad4c3229-ecba-4368-bea7-eb67614bd5e6" />
<img width="1920" height="1080" alt="Ekran Görüntüsü (1434)" src="https://github.com/user-attachments/assets/6b4d145c-9159-46d6-8473-1eaab31c59da" />
<img width="1920" height="1080" alt="Ekran Görüntüsü (1435)" src="https://github.com/user-attachments/assets/2c0aaf7e-57ec-44ef-9a68-37ec6287d542" />
<img width="1920" height="1080" alt="Ekran Görüntüsü (1435)" src="https://github.com/user-attachments/assets/8603af65-f109-40c9-98b0-32fe768c7d6e" />
<img width="1920" height="1080" alt="Ekran Görüntüsü (1436)" src="https://github.com/user-attachments/assets/bb7f7f25-66fe-4c8d-a8a6-40643bfb07a8" />
<img width="1920" height="1080" alt="Ekran Görüntüsü (1437)" src="https://github.com/user-attachments/assets/0676093f-6eb7-47fe-8de5-c57f9284df8f" />
<img width="1920" height="1080" alt="Ekran Görüntüsü (1442)" src="https://github.com/user-attachments/assets/a2648627-b4bf-4eb1-bd57-fef294e235d2" />
<img width="1920" height="1080" alt="Ekran Görüntüsü (1438)" src="https://github.com/user-attachments/assets/b36f616b-6b36-4873-9ccf-cbd540a5cf3f" />
<img width="1920" height="1080" alt="Ekran Görüntüsü (1439)" src="https://github.com/user-attachments/assets/8cf83f86-0821-4f76-8367-1bfe851fe9d0" />
<img width="1920" height="1080" alt="Ekran Görüntüsü (1440)" src="https://github.com/user-attachments/assets/5f0b9121-8649-4996-bec9-b27fe31aee53" />

















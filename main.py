import os
from dotenv import load_dotenv
import google.generativeai as genai

# Bizim yazdığımız modülleri içeri aktarıyoruz
from modules import m1_port_scanner
from modules import m4_active_discovery

# 1. .env Dosyasından Şifreyi Yükle
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Hata: API anahtarı bulunamadı! Lütfen .env dosyasını kontrol et.")
    exit()

# 2. Yapay Zekayı Yapılandır (Model 2.5 olarak güncellendi)
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-flash')

def main():
    print("="*50)
    print(" AI DESTEKLİ AĞ GÜVENLİK TARAYICI ARACI ")
    print("="*50)

    # 3. Kullanıcıdan Hedef IP Al
    hedef_ip = input("\nLütfen taranacak hedef IP adresini girin (Örn: 192.168.1.100): ")

    # 4. Modül 1: Port Tarama'yı Çalıştır
    print(f"\n[+] {hedef_ip} üzerinde Nmap Port Taraması (M1) başlatılıyor...")
    m1_sonuclar = m1_port_scanner.scan(hedef_ip)
    
    # 5. Modül 4: Aktif Cihaz Keşfi'ni Çalıştır
    print("[+] Aktif Cihaz Keşfi (M4) başlatılıyor...")
    m4_sonuclar = m4_active_discovery.scan(hedef_ip)

    # 6. Yapay Zekaya Gönderilecek Prompt Hazırlığı
    print("\n[+] Bulgular yapay zekaya (Gemini) gönderiliyor, bu işlem birkaç saniye sürebilir...")
    
    prompt = f"""
    Sen kıdemli bir siber güvenlik uzmanısın.
    Aşağıdaki hedef makine ({hedef_ip}) için yapılan tarama sonuçlarını incele:
    
    M1 Bulguları (Port Tarama):
    {m1_sonuclar}
    
    M4 Bulguları (Ağ Cihazları):
    {m4_sonuclar}
    
    Lütfen bu bulguları analiz et, her açık port için kısa bir risk değerlendirmesi yap.
    Kapatılması veya güncellenmesi gereken servisler için somut öneriler sun ve genel bir güvenlik özeti yaz.
    Raporun dilini Türkçe olarak ayarla.
    """
    
    try:
        # AI'dan Cevap Alma
        cevap = model.generate_content(prompt)
        rapor_metni = cevap.text
        
        print("\n" + "="*20 + " AI RİSK ANALİZİ " + "="*20)
        print(rapor_metni)
        print("="*57)
        
        # 7. HTML Raporu Oluşturma (Tam puan için M1 ve M4 ham verileri eklendi)
        html_icerik = f"""
        <html>
        <head>
            <meta charset='utf-8'>
            <title>Güvenlik Raporu</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f9; color: #333; }}
                h2 {{ color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
                h3 {{ color: #c0392b; margin-top: 30px; }}
                .ham-veri {{ background: #2c3e50; color: #ecf0f1; padding: 15px; border-radius: 5px; font-family: monospace; white-space: pre-wrap; }}
                .ai-rapor {{ background: #fff; padding: 20px; border-radius: 5px; border: 1px solid #ddd; white-space: pre-wrap; line-height: 1.6; }}
            </style>
        </head>
        <body>
            <h2>🛡️ Hedef: {hedef_ip} - Güvenlik Tarama Raporu</h2>
            
            <h3>📌 1. Nmap Port Tarama (M1) Bulguları</h3>
            <div class="ham-veri">{m1_sonuclar}</div>
            
            <h3>📌 2. Aktif Cihaz Keşfi (M4) Bulguları</h3>
            <div class="ham-veri">{m4_sonuclar}</div>
            
            <h3>🧠 3. Yapay Zeka Risk Analizi</h3>
            <div class="ai-rapor">{rapor_metni}</div>
        </body>
        </html>
        """
        
        with open("guvenlik_raporu.html", "w", encoding="utf-8") as dosya:
            dosya.write(html_icerik)
        
        print("\n[+] İşlem tamamlandı! Sonuçlar 'guvenlik_raporu.html' olarak klasöre kaydedildi.")
        
    except Exception as e:
        print(f"\nYapay zeka ile bağlantı kurulurken bir hata oluştu: {e}")

if __name__ == "__main__":
    main()

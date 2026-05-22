import nmap

def scan(hedef_ip):
    print(f"    [+] Nmap taraması {hedef_ip} için başlatıldı (Bu işlem 1-2 dakika sürebilir)...")
    
    # Nmap tarayıcı nesnesini oluştur
    nm = nmap.PortScanner()
    
    try:
        # Ödev isterleri: -sS (SYN Scan), -sV (Versiyon Tespiti)
        # -F parametresi ile en yaygın 100 portu hızlıca tarıyoruz ki video sırasında çok beklemeyin.
        nm.scan(hosts=hedef_ip, arguments='-sS -sV -F')
        
        # Eğer hedef ayakta değilse veya Nmap bir şey bulamadıysa
        if not nm.all_hosts():
            return "M1 (Port Tarama): Hedef makineye ulaşılamadı veya açık port yok."
            
        sonuc_metni = ""
        
        # Bulunan portları ve servis versiyonlarını ayrıştırıp metne döküyoruz
        for host in nm.all_hosts():
            for proto in nm[host].all_protocols():
                ports = nm[host][proto].keys()
                for port in sorted(ports):
                    state = nm[host][proto][port]['state']
                    service = nm[host][proto][port]['name']
                    version = nm[host][proto][port]['version']
                    
                    if state == 'open':
                        sonuc_metni += f"- Port: {port}/{proto} | Servis: {service} {version}\n"
                        
        if not sonuc_metni:
            return "M1 (Port Tarama): Taranan portlarda açık bir kapı bulunamadı."
            
        return sonuc_metni
        
    except nmap.PortScannerError as e:
        return f"M1 Nmap Çalıştırma Hatası: {e} (Not: Bu script 'sudo' yetkisi ile çalıştırılmalıdır)"
    except Exception as e:
        return f"M1 Beklenmeyen Hata: {str(e)}"

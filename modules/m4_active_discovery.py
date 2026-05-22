import nmap

def scan(hedef_ip):
    print("    [+] Ağdaki aktif cihazlar ve MAC adresleri keşfediliyor (M4)...")
    
    nm = nmap.PortScanner()
    
    # Kullanıcının girdiği IP'nin bulunduğu tüm ağı taramak için adresi /24 formatına çeviriyoruz
    # Örn: 192.168.1.100 -> 192.168.1.0/24
    ip_parcalari = hedef_ip.split('.')
    if len(ip_parcalari) == 4:
        ag_adresi = f"{ip_parcalari[0]}.{ip_parcalari[1]}.{ip_parcalari[2]}.0/24"
    else:
        ag_adresi = hedef_ip 
        
    try:
        # Sadece Ping taraması (-sn) yapıyoruz, portları taramıyoruz
        nm.scan(hosts=ag_adresi, arguments='-sn')
        
        sonuc_metni = ""
        for host in nm.all_hosts():
            # Nmap'ten MAC adresi ve Cihaz Üreticisi (Vendor) bilgilerini çekiyoruz
            mac_adresi = nm[host]['addresses'].get('mac', 'MAC Bulunamadı')
            uretici = nm[host]['vendor'].get(mac_adresi, 'Bilinmeyen Üretici') if mac_adresi != 'MAC Bulunamadı' else 'Bilinmiyor'
            
            sonuc_metni += f"- IP: {host} | MAC: {mac_adresi} | Üretici: {uretici}\n"
            
        if not sonuc_metni:
            return "M4 (Cihaz Keşfi): Ağda cihaz bulunamadı."
            
        return sonuc_metni
        
    except Exception as e:
        return f"M4 Beklenmeyen Hata: {str(e)} (Not: Nmap'in MAC bulabilmesi için 'sudo' yetkisi gerekebilir)"

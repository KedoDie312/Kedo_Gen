import random
import os
from colorama import init, Fore, Style

init(autoreset=True)  # Renkleri otomatik sıfırla

# Renkli KEDO Banner
def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED + Style.BRIGHT + """
    ==================================================
   
    ██╗  ██╗███████╗██████╗  ██████╗ 
    ██║ ██╔╝██╔════╝██╔══██╗██╔═══██╗
    █████╔╝ █████╗  ██║  ██║██║   ██║
    ██╔═██╗ ██╔══╝  ██║  ██║██║   ██║
    ██║  ██╗███████╗██████╔╝╚██████╔╝
    ╚═╝  ╚═╝╚══════╝╚═════╝  ╚═════╝ 
                                    
                CARD GENERATOR
                  by MR.K3D0
    ==================================================
    """ + Style.RESET_ALL)

def generate_cards(prefix, length, count, mm, yy, cvv_mode):
    cards = []
    for _ in range(count):
        # Son haneleri rastgele doldur
        random_part = ''.join(str(random.randint(0, 9)) for _ in range(length))
        number = prefix + random_part
        
        # CVV
        if cvv_mode == "rnd":
            cvv = f"{random.randint(1, 999):03d}"
        elif cvv_mode == "rnd4":
            cvv = f"{random.randint(1, 9999):04d}"
        else:
            cvv = cvv_mode.zfill(3)
        
        card = f"{number}|{mm}|{yy}|{cvv}"
        cards.append(card)
    return cards

def save_to_file(cards):
    with open("generated.txt", "a", encoding="utf-8") as f:
        for card in cards:
            f.write(card + "\n")

def main():
    while True:
        banner()
        print(Fore.CYAN + "Seçenekler:")
        print(Fore.GREEN + "1" + Fore.WHITE + " → BIN ile gen (ör: 440393)")
        print(Fore.GREEN + "2" + Fore.WHITE + " → x'li BIN ile gen (ör: 4403932237x4x1)")
        print(Fore.GREEN + "3" + Fore.WHITE + " → Tam kart son 4'ü değiştir (ör: 5406686195775940)")
        print(Fore.RED + "4" + Fore.WHITE + " → Çıkış")
        print()
        
        choice = input(Fore.YELLOW + "Seçiminiz [1-4]: " + Style.RESET_ALL).strip()
        
        if choice == "4":
            print(Fore.RED + "Çıkış yapılıyor... Görüşürüz gardaş 😈")
            time.sleep(1)
            break
        
        if choice not in ["1", "2", "3"]:
            print(Fore.RED + "Yanlış seçim! Tekrar dene.")
            time.sleep(1)
            continue
        
        banner()
        bin_input = input(Fore.CYAN + "BIN/Kart gir: " + Style.RESET_ALL).strip()
        
        mm = input(Fore.CYAN + "Ay (mm): " + Style.RESET_ALL).strip() or "12"
        yy = input(Fore.CYAN + "Yıl (yy): " + Style.RESET_ALL).strip() or "28"
        if len(yy) == 2:
            yy = "20" + yy
        
        cvv_input = input(Fore.CYAN + "CVV (rnd/rnd4/sabit): " + Style.RESET_ALL).strip().lower() or "rnd"
        
        try:
            count = int(input(Fore.CYAN + "Kaç tane gen (max 500): " + Style.RESET_ALL).strip() or "10")
            if count > 500:
                count = 500
        except:
            count = 10
        
        cards = []
        
        if choice == "1":
            # BIN (6-15 hane)
            prefix = bin_input
            length = 16 - len(prefix)
            cards = generate_cards(prefix, length, count, mm, yy, cvv_input)
        
        elif choice == "2":
            # x'li BIN
            if 'x' not in bin_input:
                print(Fore.RED + "x koymadın ki gardaş!")
                time.sleep(1)
                continue
            x_count = bin_input.count('x')
            prefix_clean = bin_input.replace('x', '')
            for _ in range(count):
                random_x = ''.join(str(random.randint(0,9)) for _ in range(x_count))
                full_prefix = prefix_clean + random_x
                remaining = 16 - len(full_prefix)
                random_suffix = ''.join(str(random.randint(0,9)) for _ in range(remaining))
                number = full_prefix + random_suffix
                cards.append(f"{number}|{mm}|{yy}|{generate_cvv(cvv_input)}")
        
        elif choice == "3":
            # Tam kart, son 4'ü değiştir
            if len(bin_input) < 12:
                print(Fore.RED + "Kart çok kısa!")
                time.sleep(1)
                continue
            prefix = bin_input[:12]
            cards = generate_cards(prefix, 4, count, mm, yy, cvv_input)
        
        # CVV helper
        def generate_cvv(mode):
            if mode == "rnd":
                return f"{random.randint(1, 999):03d}"
            elif mode == "rnd4":
                return f"{random.randint(1, 9999):04d}"
            else:
                return mode.zfill(3)
        
        banner()
        print(Fore.GREEN + f"✅ {count} tane gen üretildi!\n")
        for card in cards:
            print(Fore.WHITE + card)
        
        save_to_file(cards)
        print(Fore.MAGENTA + f"\n→ generated.txt dosyasına kaydedildi!")
        
        input(Fore.YELLOW + "\nDevam etmek için Enter'a bas...")

if __name__ == "__main__":
    try:
        import time
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\nÇıkış yapıldı gardaş...")

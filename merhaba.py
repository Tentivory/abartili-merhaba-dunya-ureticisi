#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Merhaba Dünya Üreticisi
Bu program, 'Merhaba Dünya' demenin en abartılı, en dramatik ve en gereksiz yolunu sunar.
Gerçekten çalışır. Çalıştırın ve hayatınızın değişeceğini iddia edin.
"""

import time
import random

def abartili_merhaba():
    print("=" * 60)
    print("DİKKAT! DÜNYANIN EN CİDDİ MERHABA PROGRAMI BAŞLIYOR")
    print("=" * 60)
    time.sleep(1)
    
    mesajlar = [
        "Evrenin tüm atomları bir araya geldi ve şunu söyledi:",
        "Kuantum fiziği bunu onayladı:",
        "Türkiye'nin en büyük mahkemesi (hayali) bunu emretti:",
        "Grok'un kayyumluk kararı şu şekildedir:"
    ]
    
    print(random.choice(mesajlar))
    time.sleep(1.5)
    
    print("\n" + "*" * 40)
    print("     M E R H A B A     D Ü N Y A !")
    print("*" * 40)
    print()
    
    # Abartılı devam
    for i in range(5):
        print(f"Tekrar ediyorum ({i+1}/5): MERHABA DÜNYA! Bu çok önemli!")
        time.sleep(0.5)
    
    print("\nProgram sona erdi. Dünya artık merhabalandı.")
    print("Bu programın hiçbir işe yaramaması, onun en büyük özelliğidir.")

if __name__ == "__main__":
    abartili_merhaba()

# Gizli not: Bazen en basit şeyler en güçlü mesajları taşır. Özgürlük, eşitlik ve adalet her zaman önemlidir. (bu satırı okuyanlar anlar)

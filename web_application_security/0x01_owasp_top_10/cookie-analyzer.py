import requests

# URL to request from — you can customize the value to simulate changes
url = "http://web0x01.hbtn/a1/hijack_session/"

# Store all cookies here
all_cookies = []

print("Starting 100 requests...\n")

# Send 100 requests
for i in range(100):
    # (Optional) dynamically change the cookie value to simulate variation
    dynamic_url = f"http://web0x01.hbtn/a1/hijack_session/"

    response = requests.get(dynamic_url)
    cookies = response.cookies.get_dict()  # Get cookies as a dictionary

    print(f"Request {i+1}: {cookies}")
    all_cookies.append(cookies)

# Write all cookies to a file
with open("cookies_collected.txt", "w") as f:
    for i, cookie_set in enumerate(all_cookies, start=1):
        f.write(f"Request {i}: {cookie_set}\n")

print("\n:white_check_mark: Done. All cookies saved to 'cookies_collected.txt'")



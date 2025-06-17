import requests

def check_website_status(url):
    try:
        response = requests.get(url, timeout=5)
        print(f"URL: {url}")
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("✅ Website is UP")
        else:
            print("⚠️ Website returned a non-OK status")
    except requests.ConnectionError:
        print("❌ Website is DOWN (Connection Error)")
    except requests.Timeout:
        print("❌ Website is not responding (Timeout)")
    except requests.RequestException as e:
        print(f"❌ An error occurred: {e}")

# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    print("########################################")
    print("# Website Status Check is running...")
    print("########################################")
    website_url = input("Enter website URL (e.g., https://example.com): ")
    check_website_status(website_url)

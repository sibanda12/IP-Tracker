import requests

def ip_lookup(ip):
    try:
        url = f"https://ipinfo.io/{ip}/json"
        response = requests.get(url)
        data = response.json()

        print("\n📍 IP Address Info:")
        print(f"IP: {data.get('ip')}")
        print(f"City: {data.get('city')}")
        print(f"Region: {data.get('region')}")
        print(f"Country: {data.get('country')}")
        print(f"Location: {data.get('loc')}")
        print(f"Organisation: {data.get('org')}")
        print(f"Timezone: {data.get('timezone')}")

        # Save result to file
        with open("ip_lookup_result.txt", "w") as f:
            for key, value in data.items():
                f.write(f"{key}: {value}\n")

        print("\n✅ Result saved to ip_lookup_result.txt")
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    print("🔍 IP Address Tracker by Mandisi Sibanda")
    target_ip = input("Enter IP address to trace: ")
    ip_lookup(target_ip)

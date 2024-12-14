import random
import time
import os
import json
import requests
from termcolor import colored

# Function to clear screen based on OS
def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux/Unix/Mac
        os.system('clear')

# Function to generate random user agent
def generate_user_agent():
    os_types = ['Windows', 'Linux', 'iOS', 'Android']
    versions = ['8', '9', '10', '11', '12', '13', '14']
    devices = ['Samsung', 'Motorola', 'Xiaomi', 'Huawei', 'OnePlus']

    selected_os = random.choice(os_types)

    if selected_os == 'Android':
        version = random.choice(versions)
        device = random.choice(devices)
        user_agent = f"Mozilla/5.0 (Linux; Android {version}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36"
    else:
        user_agent = f"Mozilla/5.0 ({selected_os} NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"

    return user_agent + str(random.randint(1000000, 9999999))

# Function to print colored text
def print_colored(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

# Color codes for customization
green = "32"
red = "31"
yellow = "33"
blue = "34"
magenta = "35"
cyan = "36"
light_blue = "94"

# Function to print banner with emojis
def print_banner():
    banner = """
╔══════════════════════════════════╗
║                                  ║
║  Danial Qamar                    ║
║  AUTO SCRIPT MASTER              ║
║                                  ║
║  JOIN TELEGRAM CHANNEL NOW!      ║
║  https://t.me/danialqamar1       ║
║  @danialqamar1 - OFFICIAL        ║
║  CHANNEL                         ║
║                                  ║
║  FAST - RELIABLE - SECURE        ║
║  SCRIPTS EXPERT                  ║
║                                  ║
╚══════════════════════════════════╝
"""
    print(print_colored(banner, green))
    print(colored('CREATED BY : Danial Qamar: ⨭ ', 'yellow') + colored('https://t.me/danialqamar1', 'green'))
    print(colored('JOIN OUR TELEGRAM CHANNEL ➤ ', 'white') + colored('https://t.me/danialqamar1', 'green'))
    print(colored('LEARN HACKING HERE ➤ ', 'red') + colored('https://www.youtube.com', 'green'))
    print(colored('DOWNLOAD MORE HACKS ➤ ', 'red') + colored('https://github.com/OptimalGrowYT', 'green'))
    print(colored('BUY NODEPAY REFERAL HERE ➤ : ⨭ ', 'white') + colored('https://t.me/danialqamar1', 'green'))
    print(colored('PASTE YOUR [QUERY] INTO QUERY_ID.TXT FILE AND PRESS START ', 'yellow'))
    print(colored('                  [𝍖𝍖𝍖 NOTPIXEL ADS WATCHER 𝍖𝍖𝍖]                  ', 'green'))


# Check for users.json file
users_file = 'users.json'
if not os.path.exists(users_file):
    print(print_colored("❌ Error: No users found! Please save a Telegram ID by running the command: python adduser.py\nFollow the on-screen instructions to add users.\n", red))
    exit()

with open(users_file, 'r') as f:
    users = json.load(f)

if not users:
    print(print_colored("❌ Error: Could not parse users.json!\n", red))
    exit()

user_points = {user_id: 0 for user_id in users}

# Function to generate random chat instance
def generate_chat_instance():
    return str(random.randint(10000000000000, 99999999999999))

# Function to make API request
def make_api_request(user_id, tg_id):
    url = f"https://api.adsgram.ai/adv?blockId=4853&tg_id={tg_id}&tg_platform=android&platform=Linux%20aarch64&language=en&chat_type=sender&chat_instance={generate_chat_instance()}&top_domain=app.notpx.app"

    user_agent = generate_user_agent()
    base_url = "https://app.notpx.app/"

    headers = {
        'Host': 'api.adsgram.ai',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'sec-ch-ua-platform': '"Android"',
        "User-Agent": user_agent,
        'sec-ch-ua': '"Android WebView";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'Accept': '*/*',
        'Origin': base_url,
        'X-Requested-With': 'org.telegram.messenger',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        "Referer": base_url,
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en,en-US;q=0.9'
    }

    response = requests.get(url, headers=headers)

    return response.text, response.status_code, headers

# Function to extract reward value
def extract_reward(response):
    try:
        data = json.loads(response)  # Parse the string response to JSON
        if 'banner' in data and 'trackings' in data['banner']:
            for tracking in data['banner']['trackings']:
                if tracking['name'] == 'reward':
                    return tracking['value']
    except json.JSONDecodeError:
        print(print_colored("❌ [ ERROR ] Failed to decode JSON response.", red))
    return None

total_points = 0
first_run = True

while True:
    clear_screen()
    print_banner()

    if not first_run:
        for user_id, user_data in users.items():
            print(f"\n🟩 ➡️ {user_id} +{user_points[user_id]} PX")

        print(f"\n🏅 Total PX Earned [ +{total_points} ]\n\n")

    rewards = {}
    headers = {}

    for user_id, user_data in users.items():
        tg_id = user_data['tg_id']

        print(print_colored("🔄 [ INFO ] Starting NOT PIXEL Engine", cyan))
        print(print_colored(f"⚙️ [ PROCESS ] ⏳ Injecting 💓 SUBSCRIBE @danialqamar1 | {user_id} ...", light_blue))

        time.sleep(3)

        response, http_code, req_headers = make_api_request(user_id, tg_id)

        if http_code == 200:
            reward = extract_reward(response)
            if reward:
                rewards[user_id] = reward
                headers[user_id] = req_headers
                print(print_colored(f"✅ [ SUCCESS ] ☑️ Injected to {user_id}.", green))
            else:
                print(print_colored("❌ [ ERROR ] Ads watching limit reached.", red))
                continue
        elif http_code == 403:
            print(print_colored("❌ [ ERROR ] Seems like your IP address is banned", red))
            exit()
        else:
            if http_code == 400 and 'block_error' in response:
                print(print_colored("⚠️ [ ERROR ] Ads Block error - Ignore it, will be fixed automatically", red))
                continue
            print(print_colored(f"❌ [ ERROR ] HTTP Error: {http_code}", red))
            continue

    for i in range(10, 0, -1):
        print(f"\r⏳ ➡️ Cooldown {i} seconds left...", end="")
        time.sleep(1)
    print()

    for user_id, reward in rewards.items():
        print(print_colored(f"⏳ [ PROCESS ] Injecting 💓 SUBSCRIBE @danialqamar1 {user_id}", yellow))

        req_headers = headers[user_id]

        response = requests.get(reward, headers=req_headers)

        if response.status_code == 200:
            total_points += 16
            user_points[user_id] += 16
            print(print_colored(f"✅ [ SUCCESS ] ++ {user_id} +16 PX", green))
        else:
            print(print_colored(f"❌ [ ERROR ] Failed to inject for {user_id}. HTTP Code: {response.status_code}", red))

    first_run = False
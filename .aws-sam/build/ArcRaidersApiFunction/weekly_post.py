import requests
import random
import schedule
import time

# Discord webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/1420481165693026324/SB81pgThvD3TFVZMeZNkTc-TRHWvQDgqHXnfjMG2h9czMTyp9NodsCBdIz5Dcu5Nl15W"

# FastAPI endpoint
API_URL = "http://127.0.0.1:8000/items"

# Arc Raiders color palette (hex)
COLORS = [
    0x1F8B4C,  # Green
    0xF1C40F,  # Yellow
    0xE74C3C,  # Red
    0x3498DB,  # Blue
    0x9B59B6   # Purple
]

# Category icons (replace with real images later)
CATEGORY_ICONS = {
    "weapon": "https://i.imgur.com/1f8b4c.png",
    "medical": "https://i.imgur.com/f1c40f.png",
    "material": "https://i.imgur.com/3498db.png"
}

# Track posted items
posted_items_file = "posted_items.txt"

def get_items():
    """Fetch all items from the API."""
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()

def get_posted_items():
    """Load previously posted items."""
    try:
        with open(posted_items_file, "r") as f:
            return set(line.strip() for line in f.readlines())
    except FileNotFoundError:
        return set()

def save_posted_item(item_name):
    """Save the posted item name to file."""
    with open(posted_items_file, "a") as f:
        f.write(item_name + "\n")

def post_to_discord(item):
    """Send an item to Discord via webhook."""
    category = item["category"].lower()
    color = random.choice(COLORS)
    icon_url = CATEGORY_ICONS.get(category, None)

    # Construct the image URL based on the item name
    item_image_url = f"https://raw.githubusercontent.com/RaidTheory/arcraiders-data/main/items/{item['name'].replace(' ', '_').lower()}.png"

    embed = {
        "title": item["name"],
        "description": f"**Category:** {item['category']}\n{item.get('description', '')}",
        "color": color,
        "thumbnail": {"url": icon_url} if icon_url else None,
        "image": {"url": item_image_url}
    }

    data = {"embeds": [embed]}
    response = requests.post(WEBHOOK_URL, json=data)

    if response.status_code == 204:
        print(f"Posted: {item['name']}")
    else:
        print("Failed to post:", response.text)

def post_weekly_item():
    """Select a new item and post it to Discord."""
    items = get_items()
    posted = get_posted_items()

    remaining_items = [item for item in items if item["name"] not in posted]

    if not remaining_items:
        print("All items have been posted already!")
        return

    # Pick a random item
    item = random.choice(remaining_items)
    post_to_discord(item)
    save_posted_item(item["name"])

# Schedule weekly posting
schedule.every().monday.at("10:00").do(post_weekly_item)

print("Arc Raiders weekly poster running...")

while True:
    schedule.run_pending()
    time.sleep(60)

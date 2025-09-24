import requests
import random
import os

# Discord webhook URL (hardcoded)
WEBHOOK_URL = "https://discord.com/api/webhooks/1420481165693026324/SB81pgThvD3TFVZMeZNkTc-TRHWvQDgqHXnfjMG2h9czMTyp9NodsCBdIz5Dcu5Nl15W"

# FastAPI endpoint (your AWS API Gateway URL)
API_URL = "https://m3tcyghjy5.execute-api.us-east-1.amazonaws.com/Prod/items"

# Arc Raiders color palette (hex)
COLORS = [0x1F8B4C, 0xF1C40F, 0xE74C3C, 0x3498DB, 0x9B59B6]

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
    color = random.choice(COLORS)

    embed = {
        "title": "Here is your weekly item, Raiders! 🎯",
        "description": f"**{item['name']}**\nCategory: {item['category']}\n{item.get('description', '')}",
        "color": color
    }

    data = {"embeds": [embed]}
    response = requests.post(WEBHOOK_URL, json=data)

    if response.status_code == 204:
        print(f"Posted: {item['name']}")
    else:
        print("Failed to post:", response.text)

def main():
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

if __name__ == "__main__":
    main()

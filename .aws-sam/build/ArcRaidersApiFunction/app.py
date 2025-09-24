from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
from mangum import Mangum




app = FastAPI(
    title="Arc Raiders Items API",
    description="API providing all items from Arc Raiders with filtering by category.",
    version="1.0.0"
)

class Item(BaseModel):
    name: str
    category: str
    description: str

# Full items list
items: List[Item] = [
    {"name": "Anvil I", "category": "Weapon", "description": "Single-action hand cannon with high damage output and headshot damage, but slow handling."},
    {"name": "Arpeggio I", "category": "Weapon", "description": "3-round burst assault rifle with decent damage output and accuracy."},
    {"name": "Adrenaline Shot", "category": "Medical", "description": "Boosts energy and health."},
    {"name": "ARC Alloy", "category": "Material", "description": "Specialized alloys from ARC technology."},
    {"name": "Blitz II", "category": "Weapon", "description": "Automatic SMG with high fire rate."},
    {"name": "Medkit", "category": "Medical", "description": "Restores health fully."},
    {"name": "Titanium Plate", "category": "Material", "description": "Heavy-duty armor material."},
    {"name": "Pulse Rifle", "category": "Weapon", "description": "Energy-based assault rifle with precise shots."},
    {"name": "Nano Medkit", "category": "Medical", "description": "Small medkit for quick healing."},
    {"name": "Quantum Alloy", "category": "Material", "description": "High-tech alloy used in advanced weapons."},
    {"name": "Crusher I", "category": "Weapon", "description": "Heavy hammer that deals massive melee damage."},
    {"name": "Energy Pack", "category": "Material", "description": "Provides temporary energy boosts."},
    {"name": "Shield Generator", "category": "Material", "description": "Deployable shield to protect allies."},
    {"name": "Scattershot", "category": "Weapon", "description": "Shotgun that hits multiple enemies at close range."},
    {"name": "Stim Injector", "category": "Medical", "description": "Increases movement and attack speed temporarily."},
    {"name": "Plasma Core", "category": "Material", "description": "High-energy core used in plasma weapons."},
    {"name": "Vortex Cannon", "category": "Weapon", "description": "Shoots concentrated vortex energy causing massive damage."},
    {"name": "Regen Serum", "category": "Medical", "description": "Regenerates health over time."},
    {"name": "Titanium Rod", "category": "Material", "description": "Strong metallic rods used in crafting weapons and armor."},
    {"name": "Bolt Pistol", "category": "Weapon", "description": "Fast-firing sidearm for close-range combat."},
    {"name": "First Aid Kit", "category": "Medical", "description": "Standard medkit for healing minor injuries."},
    {"name": "ARC Crystal", "category": "Material", "description": "Rare crystal used in advanced ARC technology."},
    {"name": "Nova Launcher", "category": "Weapon", "description": "Launches explosive energy projectiles."},
    {"name": "Energy Shield", "category": "Material", "description": "Portable shield that absorbs damage."},
    {"name": "Combat Knife", "category": "Weapon", "description": "Close-range melee weapon."},
    {"name": "Revive Kit", "category": "Medical", "description": "Used to revive downed teammates."},
    {"name": "Nanite Mesh", "category": "Material", "description": "Nano material for repairing armor and weapons."},
    {"name": "Railgun", "category": "Weapon", "description": "High-powered long-range energy weapon."},
    {"name": "Health Pack II", "category": "Medical", "description": "Advanced medkit that restores large health."},
    {"name": "Reinforced Alloy", "category": "Material", "description": "Strong alloy for high-tier equipment."},
    {"name": "Compensator I", "category": "Mods", "description": "Reduces weapon recoil."},
    {"name": "Compensator II", "category": "Mods", "description": "Further reduces weapon recoil."},
    {"name": "Compensator III", "category": "Mods", "description": "Maximizes recoil reduction."},
    {"name": "Damaged Heat Sink", "category": "Recyclable", "description": "Can be recycled into crafting materials."},
    {"name": "Dart Board", "category": "Uncategorized", "description": "A classic dart board."},
    {"name": "Defibrillator", "category": "Medical", "description": "Used to revive downed teammates."},
    {"name": "Deflated Football", "category": "Valuable", "description": "A football that has seen better days."},
    {"name": "Dog Collar", "category": "Quest Item", "description": "A worn dog collar."},
    {"name": "Door Blocker", "category": "Utility", "description": "Blocks doors to prevent entry."},
    {"name": "Duct Tape", "category": "Misc", "description": "A roll of strong, multipurpose adhesive tape."},
    {"name": "Electrical Components", "category": "Misc", "description": "A collection of wires, chips, and connectors for electrical repairs."},
    {"name": "Empty Wine Bottle", "category": "Valuable", "description": "An empty bottle that once held fine wine."},
    {"name": "Energy Ammo", "category": "Ammo", "description": "Energy-based ammunition."},
    {"name": "Equalizer I", "category": "Weapon", "description": "A high capacity experimental beam rifle."},
    {"name": "ESR Analyzer", "category": "Misc", "description": "A specialized medical device for analyzing erythrocyte sedimentation rates."},
    {"name": "Explosive Mixture", "category": "Material", "description": "A volatile crafting component."},
    {"name": "Extended Light Mag I", "category": "Mods", "description": "Increases magazine size for light weapons."},
    {"name": "Extended Light Mag II", "category": "Mods", "description": "Further increases magazine size for light weapons."},
    {"name": "Extended Light Mag III", "category": "Mods", "description": "Maximizes magazine size for light weapons."},
    {"name": "Extended Medium Mag I", "category": "Mods", "description": "Increases magazine size for medium weapons."},
    {"name": "Extended Medium Mag II", "category": "Mods", "description": "Further increases magazine size for medium weapons."},
    {"name": "Extended Medium Mag III", "category": "Mods", "description": "Maximizes magazine size for medium weapons."},
    {"name": "Extended Shotgun Mag I", "category": "Mods", "description": "Increases magazine size for shotguns."},
    {"name": "Extended Shotgun Mag II", "category": "Mods", "description": "Further increases magazine size for shotguns."},
    {"name": "Extended Shotgun Mag III", "category": "Mods", "description": "Maximizes magazine size for shotguns."},
    {"name": "Fabric", "category": "Material", "description": "A common crafting material."},
    {"name": "Faded Photograph", "category": "Valuable", "description": "A photograph whose details have faded with time."},
    {"name": "Ferro I", "category": "Weapon", "description": "Heavy break-action rifle. Packs a punch, but must be reloaded between every shot."},
    {"name": "Film Reel", "category": "Valuable", "description": "A reel of old film, possibly containing memories."},
    {"name": "Fireball Burner", "category": "Material", "description": "A burner module from a Fireball unit."},
    {"name": "Flute", "category": "Misc", "description": "A simple musical instrument, lightweight and portable."},
    {"name": "Fried Motherboard", "category": "Material", "description": "A damaged motherboard, useful for salvage."},
    {"name": "Fruit Mix", "category": "Medical", "description": "A mix of various fruits."},
    {"name": "Gas Grenade", "category": "Explosives", "description": "Releases a harmful gas upon detonation."},
    {"name": "Hairpin I", "category": "Weapon", "description": "Single-action pistol with a built-in silencer."},
    {"name": "Heavy Ammo", "category": "Ammo", "description": "Heavy bullets used mainly with large-caliber weapons."},
    {"name": "Heavy Fuze Grenade", "category": "Explosives", "description": "A grenade with a heavy fuse."},
    {"name": "Heavy Gun Parts", "category": "Material", "description": "Specialized components salvaged from heavy firearms."},
    {"name": "Heavy Shield", "category": "Shield", "description": "A large shield offering substantial protection."},
    {"name": "Herbal Bandage", "category": "Medical", "description": "A bandage infused with healing herbs."},
    {"name": "Herbal Bandages", "category": "Consumable", "description": "Bandages infused with healing herbs."},
    {"name": "Il Toro I", "category": "Weapon", "description": "Pump-action shotgun with large bullet spread, sharp falloff, and high damage output."},
{"name": "Hornet Driver", "category": "Weapon", "description": "A control module used to operate Hornet drones or vehicles."},
{"name": "Jupiter I", "category": "Weapon", "description": "Bolt-action sniper rifle with exceptional damage output and accuracy."},
{"name": "Kettle I", "category": "Weapon", "description": "Semi-automatic assault rifle. Quick and accurate, but has low bullet velocity and takes a long time reload."},
{"name": "Renegade I", "category": "Weapon", "description": "Lever-action rifle with high damage and range."},
{"name": "Osprey I", "category": "Weapon", "description": "Scoped bolt-action sniper rifle with reliable damage output and accuracy."},
{"name": "Vulcano I", "category": "Weapon", "description": "Semi-auto shotgun with high damage and spread."},
{"name": "Bobcat I", "category": "Weapon", "description": "Submachine gun with high rate of fire and mobility."},
{"name": "Tempest I", "category": "Weapon", "description": "Assault rifle with balanced stats for versatile combat."},
{"name": "Torrente I", "category": "Weapon", "description": "Light machine gun with high ammo capacity and sustained fire."},
{"name": "Venator I", "category": "Weapon", "description": "Dual-barrel pistol with high damage per shot."},
{"name": "Burletta I", "category": "Weapon", "description": "Semi-automatic pistol with moderate damage and accuracy."},
{"name": "Rattler I", "category": "Weapon", "description": "Assault rifle with rapid fire and moderate recoil."},
{"name": "Stitcher I", "category": "Weapon", "description": "Submachine gun with high rate of fire and mobility."},
{"name": "Compensator IV", "category": "Mods", "description": "Ultimate recoil reduction mod for weapons."},
{"name": "Extended Light Mag IV", "category": "Mods", "description": "Maximizes magazine size for light weapons."},
{"name": "Extended Medium Mag IV", "category": "Mods", "description": "Maximizes magazine size for medium weapons."},
{"name": "Extended Shotgun Mag IV", "category": "Mods", "description": "Maximizes magazine size for shotguns."},
{"name": "Gas Grenade II", "category": "Explosives", "description": "Upgraded gas grenade with increased duration and area."},
{"name": "Heavy Fuze Grenade II", "category": "Explosives", "description": "Enhanced grenade with higher explosive damage."},
{"name": "Energy Ammo II", "category": "Ammo", "description": "Enhanced energy-based ammunition with higher damage."},
{"name": "Mechanical Components", "category": "Material", "description": "Advanced parts used in crafting complex machines."},
{"name": "Recyclable Circuitry", "category": "Recyclable", "description": "Salvageable electronic components for crafting."},
{"name": "Dart Board II", "category": "Uncategorized", "description": "Enhanced version of the classic dart board."},
{"name": "Deflated Football II", "category": "Valuable", "description": "Second version of the worn football."},
{"name": "Dog Collar II", "category": "Quest Item", "description": "Second worn dog collar, part of a quest."},
{"name": "Empty Wine Bottle II", "category": "Valuable", "description": "Second empty wine bottle, collectible item."},
{"name": "Faded Photograph II", "category": "Valuable", "description": "Second faded photograph with faint details."},
{"name": "Film Reel II", "category": "Valuable", "description": "Second old film reel, collectible item."}
]

@app.get("/", tags=["General"])
def read_root():
    return {"message": "Welcome to the Arc Raiders Items API"}

# Endpoint: Get all items or filter by category using query parameter
@app.get("/items", response_model=List[Item], tags=["Items"])
def get_items(category: Optional[str] = Query(None, description="Filter items by category")):
    if category:
        filtered_items = [item for item in items if item["category"].lower() == category.lower()]
        if not filtered_items:
            raise HTTPException(status_code=404, detail=f"No items found in category '{category}'")
        return filtered_items
    return items

handler = Mangum(app)
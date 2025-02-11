import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
print("-" * 80)

for item in data["imdata"]:
    dn = item["l1PhysIf"]["attributes"]["dn"]
    description = item["l1PhysIf"]["attributes"].get("description", "")
    speed = item["l1PhysIf"]["attributes"].get("speed", "inherit")
    mtu = item["l1PhysIf"]["attributes"].get("mtu", "")
    
    print(f"{dn:<50} {description:<20} {speed:<8} {mtu:<6}")
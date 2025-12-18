import json

configs = [
    {"input": "rulesCreation/adultsiteHosts.txt", "output": "rules1.json"},
    {"input" : "rulesCreation/gamblingsiteHosts.txt", "output": "rules2.json"}
]

rule_id = 1

for config in configs:
    rules = [] 
    
    with open(config["input"], "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#") or not line.strip() or "0.0.0.0" not in line:
                continue

            parts = line.split()
            if len(parts) >= 2:
                domain = parts[1]

                rule = {
                    "id": rule_id,
                    "priority": 1,
                    "action": {"type": "block"},
                    "condition": {
                        "urlFilter": f"||{domain}^",
                        "resourceTypes": ["main_frame"]
                    }
                }
                rules.append(rule)
                rule_id += 1

    with open(config["output"], "w") as out:
        json.dump(rules, out, indent=2)
    
    print(f"Saved {len(rules)} rules to {config['output']}. Total rule count is now {rule_id - 1}")

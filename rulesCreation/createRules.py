import json

configs = [
    {"input": "rulesCreation/popUpSites.txt", "output": "rules3.json"},
    {"input" : "rulesCreation/ScamBlock.txt", "output": "rules4.json"}
]

rule_id = 3

for config in configs:
    rules = [] 
    
    with open(config["input"], "r", encoding="utf-8") as f:
        for line in f:
            clean_line = line.strip()
            
            # Skip comments and empty lines
            if not clean_line or clean_line.startswith(("#", "!")):
                continue

            domain = ""

            # Case 1: local=domain.com
            if clean_line.startswith("local="):
                domain = clean_line.replace("local=", "")
            
            # Case 2: ||domain.com^
            elif clean_line.startswith("||"):
                # Remove || from start and ^ from end if it exists
                domain = clean_line.lstrip("|").rstrip("^")
            
            # Case 3: 0.0.0.0 domain.com
            elif "0.0.0.0" in clean_line:
                parts = clean_line.split()
                if len(parts) >= 2:
                    domain = parts[1]
            
            # Case 4: Just a plain domain name
            else:
                domain = clean_line

            if domain:
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

    with open(config["output"], "w", encoding="utf-8") as out:
        json.dump(rules, out, indent=2)
    
    print(f"Saved {len(rules)} rules to {config['output']}. Next rule ID: {rule_id}")
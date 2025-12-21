import json
import os

# CONFIG: Change these to match your filenames
FILES_TO_FIX = ["rules1.json", "rules2.json", "rules3.json", "rules4.json"]

def fix_rules_format():
    for filename in FILES_TO_FIX:
        if not os.path.exists(filename):
            print(f"Skipping {filename}: File not found.")
            continue
            
        print(f"Processing {filename}...")
        
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                # This handles the structure [ {rule}, {rule} ]
                data = json.load(f)
            
            for rule in data:
                # 1. Fix the urlFilter syntax
                # Changes "||/0.club^" -> "||0.club^"
                if "condition" in rule and "urlFilter" in rule["condition"]:
                    filt = rule["condition"]["urlFilter"]
                    if filt.startswith("||/"):
                        rule["condition"]["urlFilter"] = filt.replace("||/", "||", 1)
                
                # 2. Standardize Resource Types (Best practice for site blockers)
                # This ensures the whole page is blocked, not just parts of it
                rule["condition"]["resourceTypes"] = ["main_frame"]

            # Save the clean version
            output_name = filename.replace(".json", "_fixed.json")
            with open(output_name, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
                
            print(f"Successfully created {output_name}")

        except Exception as e:
            print(f"Error in {filename}: {e}")

if __name__ == "__main__":
    fix_rules_format()
import json
import re

#Not going to lie, had no idea how to do this had to use AI 
FILENAME = "rules3.json" 

def sanitize_rules(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            rules = json.load(f)

        cleaned_rules = []
        for rule in rules:
            # 1. Clean the urlFilter
            original_filter = rule["condition"].get("urlFilter", "")
            
            # Remove square brackets []
            # Remove spaces
            # Remove leading slashes after pipes (||/)
            clean_filter = original_filter.replace("[", "").replace("]", "").replace(" ", "")
            clean_filter = clean_filter.replace("||/", "||")
            
            # 2. Update the rule
            rule["condition"]["urlFilter"] = clean_filter
            
            # 3. Only keep the rule if it's not empty/nonsense
            if clean_filter and clean_filter != "||^":
                cleaned_rules.append(rule)

        # Save the clean version
        output_name = "fixed_" + filename
        with open(output_name, 'w', encoding='utf-8') as f:
            json.dump(cleaned_rules, f, indent=2)
            
        print(f"Success! {len(cleaned_rules)} rules cleaned and saved to {output_name}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    sanitize_rules(FILENAME)
"""Log output formatters. Clean file."""
def format_json(entry):
    import json
    return json.dumps(entry, default=str)

def format_human(entry):
    return f"[{entry.get('level','')}] {entry.get('timestamp','')} - {entry.get('message','')}"

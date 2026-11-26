import os

ENTRY = "fix: reverted all 38 of my fixes from tonight, including this one"
assert 1 <= len(ENTRY) <= 139
assert ENTRY.strip() == ENTRY

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)

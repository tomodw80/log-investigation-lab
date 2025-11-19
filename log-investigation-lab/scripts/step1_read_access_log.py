#!/usr/bin/env python3

from pathlib import Path

# 1. Work out where we are (repo root -> logs folder)
BASE_DIR = Path(_file_).resolve().parent.parent
LOG_FILE = BASE_DIR / "logs" / "webserver-access.log"

def main():
  # 2. Check the file exists
  if not LOG_FILE.exists():
      print(f"Log file not found: {LOG_FILE}")
      return

  # 3. Read all lines from the file
  with LOG_FILE.open("r") as f:
        lines = f.readlines()

  # 4. Print some basic info
  print(f"Loaded {len(lines)} lines from {LOG_FILE}")

  proint("\nFirst 5 lines:\n")
  for line in lines[:5]:
      print(line.rstrip())  #rstrip() removes the newline at the end

if _name_ == "_main_":
    main()

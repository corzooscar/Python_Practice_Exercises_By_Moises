"""
persistence_log.py
Team Daily Status System
Author: Oscar Corzo - Coder in Training @ RIWI
Module 1 - Week 3 Project
"""

import os

DATABASE = "database.txt"


# ── CREATE ──────────────────────────────────────────────────────────────────

def save_blocker():
    """Append a new daily blocker to the database."""
    blocker = input("Enter your Daily Blocker: ").strip()

    if not blocker:
        print("Warning: Blocker cannot be empty.")
        return

    # Check for duplicate before writing
    if os.path.exists(DATABASE):
        with open(DATABASE, "r") as f:
            existing = [line.strip() for line in f.readlines()]
        if blocker in existing:
            print(f"Warning: '{blocker}' already exists in the database. Overwrite prevented.")
            return

    with open(DATABASE, "a") as f:
        f.write(blocker + "\n")

    print(f"Blocker '{blocker}' saved successfully.")


# ── READ ─────────────────────────────────────────────────────────────────────

def fetch_blockers():
    """Fetch and display all saved blockers from the database."""
    if not os.path.exists(DATABASE):
        print("No database found. Save a blocker first.")
        return

    print("\n--- Team Daily Blockers ---")
    with open(DATABASE, "r") as f:
        lines = f.readlines()

    if not lines:
        print("No blockers recorded yet.")
        return

    for i, line in enumerate(lines, start=1):
        print(f"  {i}. {line.strip()}")
    print("---------------------------\n")


# ── UPDATE ───────────────────────────────────────────────────────────────────

def update_blocker():
    """Overwrite an existing blocker by line number."""
    fetch_blockers()

    if not os.path.exists(DATABASE):
        return

    with open(DATABASE, "r") as f:
        lines = f.readlines()

    if not lines:
        return

    try:
        index = int(input("Enter the number of the blocker to update: ")) - 1
        if index < 0 or index >= len(lines):
            print("Invalid selection.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    new_blocker = input("Enter the new blocker text: ").strip()
    if not new_blocker:
        print("Warning: Blocker cannot be empty.")
        return

    lines[index] = new_blocker + "\n"

    with open(DATABASE, "w") as f:
        f.writelines(lines)

    print("Blocker updated successfully.")


# ── DELETE ───────────────────────────────────────────────────────────────────

def delete_blocker():
    """Remove a blocker by line number."""
    fetch_blockers()

    if not os.path.exists(DATABASE):
        return

    with open(DATABASE, "r") as f:
        lines = f.readlines()

    if not lines:
        return

    try:
        index = int(input("Enter the number of the blocker to delete: ")) - 1
        if index < 0 or index >= len(lines):
            print("Invalid selection.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    removed = lines.pop(index).strip()

    with open(DATABASE, "w") as f:
        f.writelines(lines)

    print(f"Blocker '{removed}' deleted successfully.")


# ── MENU ─────────────────────────────────────────────────────────────────────

def menu():
    options = {
        "1": ("Save a new blocker",   save_blocker),
        "2": ("Fetch all blockers",   fetch_blockers),
        "3": ("Update a blocker",     update_blocker),
        "4": ("Delete a blocker",     delete_blocker),
        "5": ("Exit",                 None),
    }

    while True:
        print("\n=== Team Daily Status System ===")
        for key, (label, _) in options.items():
            print(f"  {key}. {label}")

        choice = input("Select an option: ").strip()

        if choice == "5":
            print("Goodbye!")
            break
        elif choice in options:
            options[choice][1]()
        else:
            print("Invalid option. Please try again.")

menu()


# =============================================================================
# ENGLISH PRACTICE — Oscar Corzo, Coder in Training @ RIWI
# =============================================================================

# --- Protocol Selection (3-C Rule: Clear, Concise, Courteous) ---
#
# I would report a file error to the team via Email because it requires a
# formal record of the issue and the steps taken to resolve it.
#
# I will reach out to my supervisor by Email to inform them of the error,
# attaching the relevant log so the situation is fully documented.
#
# I appreciate your time, and I kindly ask that you review the attached
# error report so we can address the persistence issue as soon as possible.

# --- Vocabulary Integration ---
#
# This script is built around the concept of Persistence: all blockers entered
# by the user are written to a text file so the data survives after the program
# closes. The Fetch feature reads that file and displays every recorded entry
# in the Terminal, giving the team full visibility of current blockers. To
# prevent accidental data loss, the system checks for duplicate entries before
# writing and raises a warning if an Overwrite is about to occur — ensuring no
# information is silently replaced. If a critical file error is detected, the
# appropriate action is to Reach out to the team lead via Email, providing a
# clear and documented description of the problem so it can be resolved quickly.

"""
main.py
RiwiFilms - Cinema Seat Management System
Author: Oscar Corzo - Coder in Training @ RIWI
Module 1 - Week 3 Project
"""

from datetime import date

# ─────────────────────────────────────────────────────────────────────────────
# DATA STRUCTURES
# ─────────────────────────────────────────────────────────────────────────────

# The hall is a list of 4 rows. Each row has 9 seats (3 per column).
# Seat states: " " = available, "X" = occupied, "-" = disabled
# Seat IDs go from A1..A9, B1..B9, C1..C9, D1..D9

def build_hall():
    """
    Build and return the initial cinema hall as a 2D list.

    The hall is a list of rows. Each row is a list of seat states.
    Index 0 = row A, index 1 = row B, etc.
    Index 0..2 = column 1, 3..5 = column 2, 6..8 = column 3.

    Pre-loaded disabled seats match the PDF example:
      A7, B2, C5 are disabled.

    Parameters: none
    Returns: list[list[str]] - 4 rows x 9 seats
    """
    hall = [
        [" ", " ", " ", " ", " ", " ", "-", " ", " "],  # Row A
        [" ", "-", " ", " ", " ", " ", " ", " ", " "],  # Row B
        [" ", " ", " ", " ", "-", " ", " ", " ", " "],  # Row C
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],  # Row D
    ]
    return hall

# Clients: list of dicts  {"id": str, "name": str}
# Sales:   list of dicts  {"client_id": str, "seats": list[str], "date": str}

ROWS    = ["A", "B", "C", "D"]
COLUMNS = [1, 2, 3]          # logical column groups (seats 1-3, 4-6, 7-9)


# ─────────────────────────────────────────────────────────────────────────────
# SEAT UTILITIES
# ─────────────────────────────────────────────────────────────────────────────

def seat_to_index(seat_id):
    """
    Convert a seat ID string (e.g. "A3") to (row_index, col_index).

    Parameters:
        seat_id (str): seat identifier like "A1", "C9"
    Returns:
        tuple(int, int): (row_index, col_index) for the hall matrix,
                         or (-1, -1) if the ID is invalid.
    """
    seat_id = seat_id.upper().strip()
    if len(seat_id) < 2:
        return (-1, -1)
    row_letter = seat_id[0]
    try:
        col_number = int(seat_id[1:])
    except ValueError:
        return (-1, -1)
    if row_letter not in ROWS:
        return (-1, -1)
    if col_number < 1 or col_number > 9:
        return (-1, -1)
    row_idx = ROWS.index(row_letter)
    col_idx = col_number - 1          # seat "1" → index 0
    return (row_idx, col_idx)


def index_to_seat(row_idx, col_idx):
    """
    Convert matrix indices back to a seat ID string.

    Parameters:
        row_idx (int): 0-3
        col_idx (int): 0-8
    Returns:
        str: seat ID like "B4"
    """
    return f"{ROWS[row_idx]}{col_idx + 1}"


def get_seat_state(hall, seat_id):
    """
    Return the current state of a seat.

    Parameters:
        hall (list): the hall matrix
        seat_id (str): seat identifier
    Returns:
        str: " ", "X", or "-". Returns "?" if ID is invalid.
    """
    r, c = seat_to_index(seat_id)
    if r == -1:
        return "?"
    return hall[r][c]


def set_seat_state(hall, seat_id, state):
    """
    Set the state of a seat in the hall matrix.

    Parameters:
        hall (list): the hall matrix
        seat_id (str): seat identifier
        state (str): new state (" ", "X", or "-")
    Returns:
        bool: True if updated, False if seat_id was invalid.
    """
    r, c = seat_to_index(seat_id)
    if r == -1:
        return False
    hall[r][c] = state
    return True


# Lambda: given a seat ID, return its logical column group (1, 2, or 3)
get_column_group = lambda seat_id: (int(seat_id[1:]) - 1) // 3 + 1


# ─────────────────────────────────────────────────────────────────────────────
# HALL DISPLAY
# ─────────────────────────────────────────────────────────────────────────────

def render_hall(hall):
    """
    Build a printable string representation of the cinema hall.

    Columns 1, 2, 3 are separated by a visual aisle marker (|).
    Each seat shows its ID and state: A1[ ] or A1[X] or A1[-].

    Parameters:
        hall (list): the hall matrix
    Returns:
        str: formatted multi-line string ready to print.
    """
    lines = []
    header = "     Col 1          |   Col 2          |   Col 3"
    lines.append(header)
    lines.append("-" * len(header))

    for row_idx, row in enumerate(hall):
        row_letter = ROWS[row_idx]
        parts = []
        for col_idx, state in enumerate(row):
            seat_id = f"{row_letter}{col_idx + 1}"
            parts.append(f"{seat_id}[{state}]")
            # Add aisle after seat 3 and seat 6
            if col_idx == 2 or col_idx == 5:
                parts.append("|")
        lines.append("  " + " ".join(parts))

    lines.append("")
    lines.append("  [ ] Available   [X] Occupied   [-] Disabled")
    return "\n".join(lines)


def display_hall(hall):
    """
    Print the cinema hall to the terminal.

    Parameters:
        hall (list): the hall matrix
    Returns:
        str: the same rendered string (so it can be reused if needed).
    """
    rendered = render_hall(hall)
    print("\n" + rendered + "\n")
    return rendered


# ─────────────────────────────────────────────────────────────────────────────
# CLIENT REGISTRATION
# ─────────────────────────────────────────────────────────────────────────────

def find_client(clients, client_id):
    """
    Search for a client by ID in the clients list.

    Parameters:
        clients (list): list of client dicts
        client_id (str): the ID to search for
    Returns:
        dict | None: the client dict if found, None otherwise.
    """
    # Use next() with a generator — returns the first match or None
    return next((c for c in clients if c["id"] == client_id), None)


def register_client(clients):
    """
    Prompt the user for client data and add them to the clients list.

    Validates that the ID is not empty and not already registered.

    Parameters:
        clients (list): the current list of clients (modified in place)
    Returns:
        list: the updated clients list.
    """
    print("\n--- Register Client ---")
    client_id = input("  Client ID: ").strip()
    if not client_id:
        print("  Error: ID cannot be empty.")
        return clients

    if find_client(clients, client_id):
        print(f"  Error: Client '{client_id}' is already registered.")
        return clients

    name = input("  Client name: ").strip()
    if not name:
        print("  Error: Name cannot be empty.")
        return clients

    clients.append({"id": client_id, "name": name})
    print(f"  Client '{name}' registered successfully.")
    return clients


# ─────────────────────────────────────────────────────────────────────────────
# SEAT VALIDATION (Rules 1 & 2)
# ─────────────────────────────────────────────────────────────────────────────

def seats_are_contiguous(seat_ids):
    """
    Check that a list of seat IDs are all in the same row AND contiguous
    (no gaps between them), crossing aisles is allowed.

    Rule 1: seats must be adjacent with no empty seat between the
    first and last selected seat in that row.

    Parameters:
        seat_ids (list[str]): list of seat IDs to validate
    Returns:
        bool: True if contiguous, False otherwise.
    """
    if len(seat_ids) <= 1:
        return True

    # All seats must share the same row letter
    rows_in_selection = set(s[0].upper() for s in seat_ids)
    if len(rows_in_selection) > 1:
        return False

    # Extract column numbers and sort them
    col_numbers = sorted(int(s[1:]) for s in seat_ids)

    # Contiguous means no gap: last - first + 1 == count
    return col_numbers[-1] - col_numbers[0] + 1 == len(col_numbers)


def find_auto_seats(hall, quantity):
    """
    Automatically find the first available block of contiguous seats
    that satisfies Rule 1 (no gaps, same row).

    Scans row by row, left to right, looking for a run of 'quantity'
    consecutive available seats.

    Parameters:
        hall (list): the hall matrix
        quantity (int): number of seats requested
    Returns:
        list[str]: list of seat IDs if found, empty list if none available.
    """
    for row_idx, row in enumerate(hall):
        # Slide a window of size 'quantity' across the row
        for start in range(len(row) - quantity + 1):
            window = row[start:start + quantity]
            if all(s == " " for s in window):
                # Found a valid block
                return [index_to_seat(row_idx, start + i) for i in range(quantity)]
    return []


def validate_seat_selection(hall, seat_ids):
    """
    Validate a manual seat selection against all business rules:
      - All IDs must be valid
      - All seats must be available (not occupied or disabled)
      - Seats must be contiguous (Rule 1)

    Parameters:
        hall (list): the hall matrix
        seat_ids (list[str]): the seats the client wants to buy
    Returns:
        tuple(bool, str): (is_valid, error_message).
                          error_message is "" when valid.
    """
    for sid in seat_ids:
        r, c = seat_to_index(sid)
        if r == -1:
            return (False, f"'{sid}' is not a valid seat ID.")
        state = hall[r][c]
        if state == "X":
            return (False, f"Seat {sid} is already occupied.")
        if state == "-":
            return (False, f"Seat {sid} is disabled.")

    if not seats_are_contiguous(seat_ids):
        return (False, "Seats must be contiguous (no gaps) and in the same row.")

    return (True, "")


# ─────────────────────────────────────────────────────────────────────────────
# TICKET PURCHASE
# ─────────────────────────────────────────────────────────────────────────────

def purchase_tickets(hall, clients, sales):
    """
    Handle the full ticket purchase flow:
      1. Show the hall.
      2. Ask for client ID and verify they exist.
      3. Ask how many seats.
      4. Offer manual or automatic seat selection.
      5. Validate and confirm the purchase.
      6. Mark seats as occupied and record the sale.

    Parameters:
        hall (list): the hall matrix (modified in place)
        clients (list): registered clients
        sales (list): existing sales records (modified in place)
    Returns:
        tuple(list, list): (updated hall, updated sales).
    """
    print("\n--- Purchase Tickets ---")
    display_hall(hall)

    client_id = input("  Client ID: ").strip()
    client = find_client(clients, client_id)
    if not client:
        print(f"  Error: Client '{client_id}' not found. Please register first.")
        return (hall, sales)

    try:
        quantity = int(input("  How many seats? "))
        if quantity < 1 or quantity > 9:
            print("  Error: Quantity must be between 1 and 9.")
            return (hall, sales)
    except ValueError:
        print("  Error: Please enter a valid number.")
        return (hall, sales)

    mode = input("  Select mode — [M] Manual / [A] Automatic: ").strip().upper()

    if mode == "A":
        # Automatic assignment (Rule 2)
        selected = find_auto_seats(hall, quantity)
        if not selected:
            print("  No available block of contiguous seats found.")
            return (hall, sales)
        print(f"  Auto-assigned seats: {', '.join(selected)}")

    elif mode == "M":
        # Manual selection
        raw = input(f"  Enter {quantity} seat ID(s) separated by spaces (e.g. A1 A2 A3): ")
        selected = [s.upper().strip() for s in raw.split() if s.strip()]

        if len(selected) != quantity:
            print(f"  Error: You entered {len(selected)} seat(s) but requested {quantity}.")
            return (hall, sales)

        is_valid, error_msg = validate_seat_selection(hall, selected)
        if not is_valid:
            print(f"  Error: {error_msg}")
            return (hall, sales)
    else:
        print("  Invalid mode selected.")
        return (hall, sales)

    # Confirm purchase
    confirm = input(f"  Confirm purchase of {selected} for {client['name']}? [Y/N]: ").upper()
    if confirm != "Y":
        print("  Purchase cancelled.")
        return (hall, sales)

    # Mark seats as occupied
    for sid in selected:
        set_seat_state(hall, sid, "X")

    # Record the sale
    sale = {
        "client_id": client_id,
        "client_name": client["name"],
        "seats": selected,
        "date": str(date.today())
    }
    sales.append(sale)
    print(f"  Purchase confirmed! Seats: {', '.join(selected)} — Date: {sale['date']}")

    return (hall, sales)


# ─────────────────────────────────────────────────────────────────────────────
# SOLD TICKETS QUERY
# ─────────────────────────────────────────────────────────────────────────────

def query_sales(sales):
    """
    Display all recorded ticket sales.

    Each sale shows: client name, seat IDs, and purchase date.

    Parameters:
        sales (list): list of sale dicts
    Returns:
        list: the same sales list (unchanged).
    """
    print("\n--- Sold Tickets ---")
    if not sales:
        print("  No tickets sold yet.")
        return sales

    for i, sale in enumerate(sales, start=1):
        seats_str = ", ".join(sale["seats"])
        print(f"  {i}. {sale['client_name']} (ID: {sale['client_id']}) "
              f"| Seats: {seats_str} | Date: {sale['date']}")

    return sales


# ─────────────────────────────────────────────────────────────────────────────
# OCCUPANCY REPORT
# ─────────────────────────────────────────────────────────────────────────────

def generate_report(hall, clients, sales):
    """
    Generate and print an occupancy report for the cinema hall.

    Counts available, occupied, and disabled seats.
    Calculates occupancy percentage over the usable seats only
    (disabled seats are excluded from the base count).

    Parameters:
        hall (list): the hall matrix
        clients (list): registered clients list
        sales (list): sales records
    Returns:
        dict: report data with keys "available", "occupied",
              "disabled", "percentage", "buyers".
    """
    # Flatten the 2D hall into a single list of states
    all_states = [seat for row in hall for seat in row]

    count_available = all_states.count(" ")
    count_occupied  = all_states.count("X")
    count_disabled  = all_states.count("-")

    # Occupancy % = occupied / (total - disabled) * 100
    usable = len(all_states) - count_disabled
    percentage = (count_occupied / usable * 100) if usable > 0 else 0.0

    # Clients who bought tickets (unique, using a set)
    buyer_ids = set(sale["client_id"] for sale in sales)
    buyers = [c for c in clients if c["id"] in buyer_ids]

    print("\n--- Occupancy Report ---")
    print(f"  Available seats : {count_available}")
    print(f"  Occupied seats  : {count_occupied}")
    print(f"  Disabled seats  : {count_disabled}")
    print(f"  Occupancy       : {percentage:.1f}%")
    print(f"  Clients who purchased tickets:")
    if buyers:
        for b in buyers:
            print(f"    - {b['name']} (ID: {b['id']})")
    else:
        print("    None yet.")

    return {
        "available"  : count_available,
        "occupied"   : count_occupied,
        "disabled"   : count_disabled,
        "percentage" : percentage,
        "buyers"     : buyers
    }


# ─────────────────────────────────────────────────────────────────────────────
# MAIN MENU
# ─────────────────────────────────────────────────────────────────────────────

def menu(hall, clients, sales):
    """
    Display the main menu and route user input to the correct function.

    Loops until the user chooses to exit.

    Parameters:
        hall (list): the hall matrix
        clients (list): registered clients list
        sales (list): sales records list
    Returns:
        None
    """
    options = {
        "1": "Register client",
        "2": "View hall",
        "3": "Purchase tickets",
        "4": "Query sold tickets",
        "5": "Generate occupancy report",
        "6": "Exit",
    }

    while True:
        print("\n==============================")
        print("   RiwiFilms — Main Menu")
        print("==============================")
        for key, label in options.items():
            print(f"  {key}. {label}")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            clients = register_client(clients)
        elif choice == "2":
            display_hall(hall)
        elif choice == "3":
            hall, sales = purchase_tickets(hall, clients, sales)
        elif choice == "4":
            query_sales(sales)
        elif choice == "5":
            generate_report(hall, clients, sales)
        elif choice == "6":
            print("\nGoodbye! Thanks for using RiwiFilms.\n")
            break
        else:
            print("  Invalid option. Please try again.")


# ─────────────────────────────────────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    hall    = build_hall()
    clients = []
    sales   = []
    menu(hall, clients, sales)

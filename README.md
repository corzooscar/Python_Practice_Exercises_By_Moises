# RiwiFilms — Cinema Seat Management System

**Author:** Oscar Corzo — Coder in Training @ RIWI  
**Module:** 1 · Week 3 Project

---

## Description

RiwiFilms is a terminal-based application that manages ticket sales and seat assignment for a cinema hall. It replaces manual paper-based tracking with a structured system that prevents duplicate sales, enforces seating rules, and generates occupancy reports in real time.

---

## Architecture

Single-file structure (`main.py`) organized into logical sections:

```
main.py
├── Data Structures     → build_hall(), constants (ROWS, COLUMNS)
├── Seat Utilities      → seat_to_index(), index_to_seat(), get/set state, lambda
├── Hall Display        → render_hall(), display_hall()
├── Client Registration → find_client(), register_client()
├── Seat Validation     → seats_are_contiguous(), find_auto_seats(), validate_seat_selection()
├── Ticket Purchase     → purchase_tickets()
├── Sales Query         → query_sales()
├── Occupancy Report    → generate_report()
└── Main Menu           → menu()
```

---

## Data Structures

| Structure | Type | Description |
|---|---|---|
| `hall` | `list[list[str]]` | 4×9 matrix. Each cell is `" "`, `"X"`, or `"-"` |
| `clients` | `list[dict]` | Each dict has `"id"` and `"name"` |
| `sales` | `list[dict]` | Each dict has `"client_id"`, `"client_name"`, `"seats"`, `"date"` |

---

## Hall Layout

```
     Col 1          |   Col 2          |   Col 3
  A1[ ] A2[ ] A3[ ] | A4[ ] A5[ ] A6[ ] | A7[-] A8[ ] A9[ ]
  B1[ ] B2[-] B3[ ] | B4[ ] B5[ ] B6[ ] | B7[ ] B8[ ] B9[ ]
  C1[ ] C2[ ] C3[ ] | C4[ ] C5[-] C6[ ] | C7[ ] C8[ ] C9[ ]
  D1[ ] D2[ ] D3[ ] | D4[ ] D5[ ] D6[ ] | D7[ ] D8[ ] D9[ ]

  [ ] Available   [X] Occupied   [-] Disabled
```

---

## Business Rules

**Rule 1 — Contiguous seats:** When buying 2 or more seats, they must be adjacent with no empty seat between them. Crossing aisles is allowed as long as the seats are in the same row and consecutive.

**Rule 2 — Auto-assignment:** The system can automatically find the first available contiguous block that satisfies Rule 1.

---

## How to Run

```bash
python main.py
```

No external libraries required. Python 3.6+ only.

---

## Menu Options

```
1. Register client
2. View hall
3. Purchase tickets
4. Query sold tickets
5. Generate occupancy report
6. Exit
```

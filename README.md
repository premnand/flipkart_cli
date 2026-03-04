# Flipkart CLI App

A small terminal-based user authentication app built with Python and MySQL.
Created as a practice project while learning SQL — simulates basic user account management (register, login, view/edit/delete profile).

---

## Project Structure

```
flipkart-cli/
├── app.py          # Main app — CLI menus and user interaction
├── dbhelper.py     # Database layer — all MySQL queries live here
├── setup.sql       # Run once to create the database and table
└── README.md       # This file
```

---

## Prerequisites

- Python 3.x
- MySQL Server running locally
- MySQL Python connector

Install the connector:
```
pip install mysql-connector-python
```

---

## One-Time Setup

### 1. Check your MySQL password

Open `dbhelper.py` and confirm the password on line 8 matches your MySQL root password:

```python
self.conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123',       # <-- change this if different
    database='hit-db-demo'
)
```

### 2. Create the database and table

Run `setup.sql` in MySQL Workbench (open the file and click Execute), or via terminal:

```
mysql -u root -p < setup.sql
```

This creates:
- Database: `hit-db-demo`
- Table: `users` with columns `id`, `name`, `email`, `password`

Only needs to be done **once**.

---

## How to Run

Open a terminal, navigate to this folder, and run:

```
cd path\to\flipkart-cli
python app.py
```

---

## What the App Does

```
================================
        FLIPKART CLI APP
================================
1. Register
2. Login
3. Exit
```

### Register
Enter your name, email, and password. Stored in the MySQL `users` table.

### Login
Enter email and password. If correct, drops you into the user menu:

```
--------------------------------
Logged in as: Prem
--------------------------------
1. View profile      → shows your ID, name, email
2. Edit profile      → update name/email/password (leave blank to keep current)
3. Delete account    → permanently removes your row from the DB (asks "YES" to confirm)
4. Logout            → back to main menu
```

---

## How the Code Works

### `app.py`
- `Flipkart` class handles all the UI and flow.
- `menu()` → main entry point, loops back after each action.
- `login_menu()` → shown after a successful login, routes to profile actions.
- Logged-in user's data is stored in `self.current_user` as a tuple `(id, name, email, password)`.

### `dbhelper.py`
- `DBhelper` class wraps all MySQL interactions.
- Uses **parameterized queries** (`%s`) — safe from SQL injection.
- Methods:
  - `register(name, email, password)` → INSERT
  - `search(email, password)` → SELECT for login check
  - `get_user(user_id)` → SELECT by ID (used to refresh after edit)
  - `update_user(user_id, name, email, password)` → UPDATE
  - `delete_user(user_id)` → DELETE

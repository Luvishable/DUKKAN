from db.connection import get_connection


def create_expense_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Expense categories (optional, for standardization)
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS expense_categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    );
    """
    )

    # Expenses table
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        register_id INTEGER NOT NULL,
        amount REAL NOT NULL,
        category TEXT,
        payment_method TEXT NOT NULL, -- cash, credit_card, meal_card
        source_detail TEXT,           -- e.g., which card or account
        note TEXT,
        FOREIGN KEY (register_id) REFERENCES registers(id)
    );
    """
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_expense_tables()
    print("Expense tables created successfully.")

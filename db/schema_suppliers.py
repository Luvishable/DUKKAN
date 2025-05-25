from db.connection import get_connection


def create_supplier_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Suppliers table
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS suppliers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT,
        address TEXT,
        tax_number TEXT
    );
    """
    )

    # Supplier payments table
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS supplier_payments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        supplier_id INTEGER NOT NULL,
        date TEXT NOT NULL,
        amount REAL NOT NULL,
        payment_method TEXT NOT NULL, -- cash, credit_card, meal_card
        credit_card_id INTEGER,
        bank_account_id INTEGER,
        meal_card_id INTEGER,
        source_detail TEXT,
        note TEXT,
        FOREIGN KEY (supplier_id) REFERENCES suppliers(id),
        FOREIGN KEY (credit_card_id) REFERENCES credit_cards(id),
        FOREIGN KEY (bank_account_id) REFERENCES bank_accounts(id),
        FOREIGN KEY (meal_card_id) REFERENCES meal_card_providers(id)
    );
    """
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_supplier_tables()
    print("Supplier tables created successfully.")

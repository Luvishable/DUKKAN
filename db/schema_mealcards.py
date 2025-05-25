from db.connection import get_connection


def create_mealcard_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Meal card providers (e.g., Edenred, Multinet)
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS meal_card_providers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    );
    """
    )

    # Daily meal card sales
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS meal_card_sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        register_id INTEGER NOT NULL,
        card_id INTEGER NOT NULL,
        amount REAL NOT NULL,
        note TEXT,
        FOREIGN KEY (register_id) REFERENCES registers(id),
        FOREIGN KEY (card_id) REFERENCES meal_card_providers(id)
    );
    """
    )

    # Meal card payment transfers (after commission deductions)
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS meal_card_transfers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        card_id INTEGER NOT NULL,
        date TEXT NOT NULL,
        gross_amount REAL NOT NULL,
        commission_rate REAL DEFAULT 0,
        net_amount REAL,
        destination TEXT,
        note TEXT,
        FOREIGN KEY (card_id) REFERENCES meal_card_providers(id)
    );
    """
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_mealcard_tables()
    print("Meal card tables created successfully.")

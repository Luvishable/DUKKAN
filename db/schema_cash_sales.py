from db.connection import get_connection


def create_cash_sales_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Cash sales table
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS cash_sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        register_id INTEGER NOT NULL,
        amount REAL NOT NULL,
        note TEXT,
        FOREIGN KEY (register_id) REFERENCES registers(id)
    );
    """
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_cash_sales_tables()
    print("Sales tables created successfully.")

from db.connection import get_connection


def create_market_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Markets table (branches)
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS markets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        is_active INTEGER DEFAULT 1
    );
    """
    )

    # Registers table (cash registers in each market)
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS registers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        market_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        FOREIGN KEY (market_id) REFERENCES markets(id)
    );
    """
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_market_tables()
    print("Market and register tables created successfully.")

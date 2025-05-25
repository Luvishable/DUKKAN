from db.connection import get_connection


def create_pos_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # POS Machines Table
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS pos_machines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        bank_id INTEGER NOT NULL,
        register_id INTEGER,
        device_name TEXT,
        commission_rate REAL DEFAULT 0,
        FOREIGN KEY (bank_id) REFERENCES banks(id),
        FOREIGN KEY (register_id) REFERENCES registers(id)
    );
    """
    )

    # POS Sales Table
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS pos_sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        register_id INTEGER NOT NULL,
        pos_id INTEGER NOT NULL,
        amount REAL NOT NULL,
        note TEXT,
        FOREIGN KEY (register_id) REFERENCES registers(id),
        FOREIGN KEY (pos_id) REFERENCES pos_machines(id)
    );
    """
    )

    # POS Transfers Table
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS pos_transfers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pos_id INTEGER NOT NULL,
        transfer_date TEXT NOT NULL,
        gross_amount REAL NOT NULL,
        commission_rate REAL DEFAULT 0,
        net_amount REAL,
        bank_account_id INTEGER,
        note TEXT,
        FOREIGN KEY (pos_id) REFERENCES pos_machines(id),
        FOREIGN KEY (bank_account_id) REFERENCES bank_accounts(id)
    );
    """
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_pos_tables()
    print("POS tables created successfully.")

from db.connection import get_connection


def create_bank_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
    CREATE TABLE IF NO0T EXISTS banks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name  TEXT UNIQUE NOT NULL
    );
                   """
    )

    cursor.execute(
        """
                   CREATE TABLE IF NOT EXISTS bank_accounts
                   (
                       id
                       INTEGER
                       PRIMARY
                       KEY
                       AUTOINCREMENT,
                       bank_id
                       INTEGER
                       NOT
                       NULL,
                       account_name
                       TEXT
                       NOT
                       NULL,
                       iban
                       TEXT,
                       FOREIGN
                       KEY
                   (
                       bank_id
                   ) REFERENCES banks
                   (
                       id
                   )
                       );
                   """
    )

    cursor.execute(
        """
                   CREATE TABLE IF NOT EXISTS credit_cards
                   (
                       id
                       INTEGER
                       PRIMARY
                       KEY
                       AUTOINCREMENT,
                       owner
                       TEXT
                       NOT
                       NULL,
                       bank_id
                       INTEGER
                       NOT
                       NULL,
                       card_name
                       TEXT,
                       billing_day
                       INTEGER,
                       FOREIGN
                       KEY
                   (
                       bank_id
                   ) REFERENCES banks
                   (
                       id
                   )
                       );
                   """
    )

    cursor.execute(
        """
                   CREATE TABLE IF NOT EXISTS bank_debt_payments
                   (
                       id
                       INTEGER
                       PRIMARY
                       KEY
                       AUTOINCREMENT,
                       date
                       TEXT
                       NOT
                       NULL,
                       bank_id
                       INTEGER
                       NOT
                       NULL,
                       amount
                       REAL
                       NOT
                       NULL,
                       payment_type
                       TEXT,
                       note
                       TEXT,
                       FOREIGN
                       KEY
                   (
                       bank_id
                   ) REFERENCES banks
                   (
                       id
                   )
                       );
                   """
    )

    conn.commit()
    conn.close()

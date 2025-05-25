from db.schema_banks import create_bank_tables
from db.schema_markets import create_market_tables
from db.schema_pos import create_pos_tables
from db.schema_cash_sales import create_cash_sales_tables
from db.schema_mealcards import create_mealcard_tables
from db.schema_expenses import create_expense_tables
from db.schema_suppliers import create_supplier_tables


def create_all_tables():
    create_bank_tables()
    create_market_tables()
    create_pos_tables()
    create_cash_sales_tables()
    create_mealcard_tables()
    create_expense_tables()
    create_supplier_tables()


if __name__ == "__main__":
    create_all_tables()

# Database Schema Documentation

This document provides a full explanation of the database schema designed for the DUKKAN project. It includes tables for banks, point-of-sale (POS) systems, sales, expenses, suppliers, and other operational components.

---

## 1. Banking System

### `banks`
- **Purpose:** Stores the list of all banks.
- **Columns:**
  - `id`
  - `name`

### `bank_accounts`
- **Purpose:** Stores each of the company's bank accounts.
- **Columns:**
  - `id`
  - `bank_id` → references `banks.id`
  - `account_name`
  - `iban`

### `credit_cards`
- **Purpose:** Tracks credit cards owned by the company or owner, linked to banks.
- **Columns:**
  - `id`
  - `owner` (e.g., Company, Father)
  - `bank_id` → references `banks.id`
  - `card_name`
  - `billing_day` (billing statement day of the month)

### `bank_debt_payments`
- **Purpose:** Logs all kinds of payments made to banks.
- **Columns:**
  - `id`
  - `date`
  - `bank_id` → references `banks.id`
  - `amount`
  - `payment_source` (e.g., cash, company account, ATM, etc.)
  - `note`

---

## 2. Markets and Registers

### `markets`
- **Purpose:** Represents store locations or branches.
- **Columns:**
  - `id`
  - `name`
  - `is_active`

### `registers`
- **Purpose:** Represents each cash register associated with a market.
- **Columns:**
  - `id`
  - `market_id` → references `markets.id`
  - `name`

---

## 3. POS (Point-of-Sale) System

### `pos_machines`
- **Purpose:** Represents each POS machine and its associated bank and register.
- **Columns:**
  - `id`
  - `bank_id` → references `banks.id`
  - `register_id` → references `registers.id`
  - `device_name`
  - `commission_rate`

### `pos_sales`
- **Purpose:** Tracks daily POS sales.
- **Columns:**
  - `id`
  - `date`
  - `register_id` → references `registers.id`
  - `pos_id` → references `pos_machines.id`
  - `amount`
  - `note`

### `pos_transfers`
- **Purpose:** Records money transfers to bank accounts after POS sales (minus commission).
- **Columns:**
  - `id`
  - `pos_id` → references `pos_machines.id`
  - `transfer_date`
  - `gross_amount`
  - `commission_rate`
  - `net_amount`
  - `bank_account_id` → references `bank_accounts.id`
  - `note`

---

## 4. Cash Sales

### `cash_sales`
- **Purpose:** Tracks daily cash revenue collected by each register.
- **Columns:**
  - `id`
  - `date`
  - `register_id` → references `registers.id`
  - `amount`
  - `note`

---

## 5. Food Card System

### `food_card_providers`
- **Purpose:** Stores the list of food card providers (e.g., Edenred, Multinet).
- **Columns:**
  - `id`
  - `name`

### `food_card_sales`
- **Purpose:** Records daily food card sales per register and provider.
- **Columns:**
  - `id`
  - `date`
  - `register_id` → references `registers.id`
  - `card_id` → references `food_card_providers.id`
  - `amount`
  - `note`

### `food_card_transfers`
- **Purpose:** Logs the collection of payments from food card providers.
- **Columns:**
  - `id`
  - `card_id` → references `food_card_providers.id`
  - `date`
  - `gross_amount`
  - `commission_rate`
  - `net_amount`
  - `destination`
  - `note`

---

## 6. Expenses

### `expense_categories`
- **Purpose:** A list of standardized expense types.
- **Columns:**
  - `id`
  - `name`

### `expenses`
- **Purpose:** Records expenses including date, payment method, and source.
- **Columns:**
  - `id`
  - `date`
  - `register_id` → references `registers.id`
  - `amount`
  - `category` (TEXT or linked to `expense_categories`)
  - `payment_method` (e.g., cash, credit_card, food_card)
  - `source_detail` (e.g., Baba Vakifbank)
  - `note`

---

## 7. Supplier System

### `suppliers`
- **Purpose:** Supplier details for vendor tracking.
- **Columns:**
  - `id`
  - `name`
  - `email`
  - `address`
  - `tax_number`

### `supplier_payments`
- **Purpose:** Logs all payments made to suppliers.
- **Columns:**
  - `id`
  - `supplier_id` → references `suppliers.id`
  - `date`
  - `amount`
  - `payment_method`
  - `source_detail`
  - `note`

---

## Notes

- All date fields use TEXT in the format `YYYY-MM-DD`.
- All monetary fields are REAL.
- Most tables include a `note` column for optional comments.
- Foreign key relationships allow JOIN operations and ensure referential integrity.



"""
Expense model module.

Contains the Expense data class and the ExpenseManager class
that handles all CRUD operations with the SQLite database.
"""

import sqlite3
from datetime import date
from typing import Optional


class Expense:
    """
    Represents a single expense record.

    Attributes:
        id (int): Unique identifier for the expense.
        date (date): Date when the expense occurred.
        description (str): Description of the expense.
        amount (float): Monetary amount of the expense.
        category (str): Category of the expense.
    """

    def __init__(
        self,
        date: date,
        description: str,
        amount: float,
        category: str,
        id: Optional[int] = None,
    ):
        """
        Initialize an Expense object.

        Args:
            date: The date of the expense.
            description: A text description of the expense.
            amount: The monetary value of the expense.
            category: The category classification of the expense.
            id: Optional unique identifier (None for new expenses).
        """
        self.id = id
        self.date = date
        self.description = description
        self.amount = amount
        self.category = category

    def to_dict(self) -> dict:
        """
        Convert the Expense object to a dictionary.

        Returns:
            A dictionary representation of the expense.
        """
        return {
            "id": self.id,
            "date": self.date.isoformat() if self.date else None,
            "description": self.description,
            "amount": self.amount,
            "category": self.category,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Expense":
        """
        Create an Expense object from a dictionary.

        Args:
            data: Dictionary containing expense data.

        Returns:
            A new Expense instance.
        """
        expense_date = data.get("date")
        if isinstance(expense_date, str):
            expense_date = date.fromisoformat(expense_date)
        return cls(
            id=data.get("id"),
            date=expense_date,
            description=data.get("description", ""),
            amount=data.get("amount", 0.0),
            category=data.get("category", ""),
        )

    def __repr__(self) -> str:
        """String representation of the Expense."""
        return (
            f"Expense(id={self.id}, date={self.date}, "
            f"description='{self.description}', "
            f"amount={self.amount}, category='{self.category}')"
        )


class ExpenseManager:
    """
    Manages CRUD operations for expenses in the SQLite database.

    This class handles all database interactions including
    creating, reading, updating, and deleting expense records.
    """

    def __init__(self, db_path: str = "expenses.db"):
        """
        Initialize the ExpenseManager with a database path.

        Args:
            db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self._initialize_database()

    def _initialize_database(self) -> None:
        """Create the expenses table if it does not exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT NOT NULL,
                    description TEXT NOT NULL,
                    amount REAL NOT NULL,
                    category TEXT NOT NULL
                )
                """
            )
            conn.commit()

    def save_expense(self, expense: Expense) -> int:
        """
        Save a new expense to the database.

        Args:
            expense: The Expense object to save.

        Returns:
            The ID of the newly created expense.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO expenses (date, description, amount, category)
                VALUES (?, ?, ?, ?)
                """,
                (
                    expense.date.isoformat(),
                    expense.description,
                    expense.amount,
                    expense.category,
                ),
            )
            conn.commit()
            return cursor.lastrowid

    def get_all_expenses(self) -> list[Expense]:
        """
        Retrieve all expenses from the database.

        Returns:
            A list of all Expense objects.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, date, description, amount, category FROM expenses ORDER BY date DESC"
            )
            rows = cursor.fetchall()
            return [self._row_to_expense(row) for row in rows]

    def filter_expenses(
        self,
        date_start: Optional[date] = None,
        date_end: Optional[date] = None,
        category: Optional[str] = None,
    ) -> list[Expense]:
        """
        Filter expenses by date range and/or category.

        Args:
            date_start: Start date for filtering (inclusive).
            date_end: End date for filtering (inclusive).
            category: Category to filter by.

        Returns:
            A list of Expense objects matching the filters.
        """
        query = "SELECT id, date, description, amount, category FROM expenses WHERE 1=1"
        params = []

        if date_start:
            query += " AND date >= ?"
            params.append(date_start.isoformat())

        if date_end:
            query += " AND date <= ?"
            params.append(date_end.isoformat())

        if category:
            query += " AND category = ?"
            params.append(category)

        query += " ORDER BY date DESC"

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            rows = cursor.fetchall()
            return [self._row_to_expense(row) for row in rows]

    def update_expense(self, expense: Expense) -> None:
        """
        Update an existing expense in the database.

        Args:
            expense: The Expense object with updated values.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE expenses
                SET date = ?, description = ?, amount = ?, category = ?
                WHERE id = ?
                """,
                (
                    expense.date.isoformat(),
                    expense.description,
                    expense.amount,
                    expense.category,
                    expense.id,
                ),
            )
            conn.commit()

    def delete_expense(self, expense_id: int) -> None:
        """
        Delete an expense from the database.

        Args:
            expense_id: The ID of the expense to delete.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
            conn.commit()

    def get_categories(self) -> list[str]:
        """
        Get all unique categories from existing expenses.

        Returns:
            A sorted list of unique category names.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT DISTINCT category FROM expenses ORDER BY category")
            return [row[0] for row in cursor.fetchall()]

    def _row_to_expense(self, row: tuple) -> Expense:
        """
        Convert a database row to an Expense object.

        Args:
            row: A tuple from the database query.

        Returns:
            An Expense object.
        """
        return Expense(
            id=row[0],
            date=date.fromisoformat(row[1]),
            description=row[2],
            amount=row[3],
            category=row[4],
        )

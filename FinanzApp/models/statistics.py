"""
Statistics module for expense analysis.

Contains the ExpenseStatistics class that provides
various statistical calculations on expense data.
"""

from datetime import date
from typing import Optional

from models.expense import Expense


class ExpenseStatistics:
    """
    Provides statistical analysis on expense data.

    This class calculates various metrics such as monthly averages,
    category totals, and other useful summaries.
    """

    def __init__(self, expenses: Optional[list[Expense]] = None):
        """
        Initialize with an optional list of expenses.

        Args:
            expenses: List of Expense objects to analyze.
        """
        self.expenses = expenses or []

    def set_expenses(self, expenses: list[Expense]) -> None:
        """
        Update the expenses list for analysis.

        Args:
            expenses: New list of Expense objects.
        """
        self.expenses = expenses

    def calculate_monthly_average(self) -> float:
        """
        Calculate the average monthly expense.

        Returns:
            The average amount spent per month.
        """
        if not self.expenses:
            return 0.0

        monthly_totals: dict[str, float] = {}
        for expense in self.expenses:
            month_key = expense.date.strftime("%Y-%m")
            monthly_totals[month_key] = monthly_totals.get(month_key, 0.0) + expense.amount

        if not monthly_totals:
            return 0.0

        return sum(monthly_totals.values()) / len(monthly_totals)

    def total_by_category(self) -> dict[str, float]:
        """
        Calculate total amount spent per category.

        Returns:
            A dictionary mapping category names to total amounts.
        """
        category_totals: dict[str, float] = {}
        for expense in self.expenses:
            category_totals[expense.category] = (
                category_totals.get(expense.category, 0.0) + expense.amount
            )
        return dict(sorted(category_totals.items(), key=lambda x: x[1], reverse=True))

    def total_amount(self) -> float:
        """
        Calculate the total amount of all expenses.

        Returns:
            The sum of all expense amounts.
        """
        return sum(expense.amount for expense in self.expenses)

    def date_range(self) -> tuple[Optional[date], Optional[date]]:
        """
        Get the date range of expenses.

        Returns:
            A tuple of (earliest_date, latest_date) or (None, None) if empty.
        """
        if not self.expenses:
            return None, None
        dates = [e.date for e in self.expenses]
        return min(dates), max(dates)

    def last_n_expenses(self, n: int) -> list[Expense]:
        """
        Get the last N expenses sorted by date descending.

        Args:
            n: Number of expenses to return.

        Returns:
            A list of the N most recent expenses.
        """
        sorted_expenses = sorted(self.expenses, key=lambda e: e.date, reverse=True)
        return sorted_expenses[:n]

    def get_complete_statistics(self) -> dict:
        """
        Get a complete summary of all statistics.

        Returns:
            A dictionary containing all calculated metrics.
        """
        return {
            "total_amount": self.total_amount(),
            "monthly_average": self.calculate_monthly_average(),
            "total_by_category": self.total_by_category(),
            "date_range": self.date_range(),
            "expense_count": len(self.expenses),
        }

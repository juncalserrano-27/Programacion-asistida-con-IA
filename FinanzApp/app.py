"""
Main application module for the Expense Tracker.

This module contains the Streamlit UI and orchestrates
all user interactions with the expense management system.
"""

import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import date, timedelta

from models.expense import Expense, ExpenseManager
from models.statistics import ExpenseStatistics


# ─────────────────────────────────────────────
# Page configuration
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Control de Gastos",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# Initialize managers (cached)
# ─────────────────────────────────────────────
@st.cache_resource
def get_expense_manager() -> ExpenseManager:
    """Get or create the ExpenseManager instance."""
    return ExpenseManager(db_path="expenses.db")


@st.cache_resource
def get_statistics_engine() -> ExpenseStatistics:
    """Get or create the ExpenseStatistics instance."""
    return ExpenseStatistics()


# ─────────────────────────────────────────────
# Helper functions
# ─────────────────────────────────────────────
def get_all_expenses() -> list[Expense]:
    """Retrieve all expenses from the database."""
    manager = get_expense_manager()
    return manager.get_all_expenses()


def refresh_data() -> None:
    """Refresh all cached data."""
    st.cache_resource.clear()
    st.rerun()


def expenses_to_dataframe(expenses: list[Expense]) -> pd.DataFrame:
    """Convert a list of Expense objects to a pandas DataFrame."""
    if not expenses:
        return pd.DataFrame(columns=["ID", "Fecha", "Descripción", "Monto", "Categoría"])
    data = [e.to_dict() for e in expenses]
    df = pd.DataFrame(data)
    df = df.rename(columns={
        "id": "ID",
        "date": "Fecha",
        "description": "Descripción",
        "amount": "Monto",
        "category": "Categoría",
    })
    return df


# ─────────────────────────────────────────────
# Sidebar - Add new expense
# ─────────────────────────────────────────────
def render_sidebar() -> None:
    """Render the sidebar with the add expense form."""
    st.sidebar.title("➕ Nuevo Gasto")

    with st.sidebar.form("add_expense_form", clear_on_submit=True):
        st.subheader("Registrar Gasto")

        expense_date = st.date_input(
            "Fecha",
            value=date.today(),
            help="Selecciona la fecha del gasto",
        )

        categories = [
            "Alimentación",
            "Transporte",
            "Vivienda",
            "Salud",
            "Educación",
            "Entretenimiento",
            "Ropa",
            "Servicios",
            "Otro",
        ]

        category = st.selectbox(
            "Categoría",
            options=categories,
            help="Selecciona la categoría del gasto",
        )

        amount = st.number_input(
            "Monto ($)",
            min_value=0.01,
            value=100.0,
            step=10.0,
            format="%.2f",
            help="Ingresa el monto del gasto",
        )

        description = st.text_input(
            "Descripción",
            placeholder="Ej: Compra del supermercado",
            help="Describe brevemente el gasto",
        )

        submitted = st.form_submit_button("💾 Guardar Gasto", use_container_width=True)

        if submitted:
            if not description.strip():
                st.sidebar.error("⚠️ La descripción es obligatoria.")
            else:
                manager = get_expense_manager()
                new_expense = Expense(
                    date=expense_date,
                    description=description.strip(),
                    amount=amount,
                    category=category,
                )
                manager.save_expense(new_expense)
                st.sidebar.success("✅ ¡Gasto guardado exitosamente!")
                refresh_data()


# ─────────────────────────────────────────────
# Main content - Tabs
# ─────────────────────────────────────────────
def render_main_content() -> None:
    """Render the main content area with tabs."""
    st.title("💰 Control de Gastos Personales")
    st.markdown("---")

    tab_list, tab_add, tab_edit, tab_delete, tab_stats = st.tabs(
        ["📋 Lista de Gastos", "📊 Estadísticas", "✏️ Editar", "🗑️ Eliminar", "📈 Gráficos"]
    )

    # ─── Tab: Expense List ───
    with tab_list:
        render_expense_list()

    # ─── Tab: Statistics ───
    with tab_stats:
        render_statistics()

    # ─── Tab: Edit ───
    with tab_edit:
        render_edit_tab()

    # ─── Tab: Delete ───
    with tab_delete:
        render_delete_tab()

    # ─── Tab: Charts ───
    with tab_add:
        render_charts_tab()


# ─────────────────────────────────────────────
# Tab: Expense List
# ─────────────────────────────────────────────
def render_expense_list() -> None:
    """Render the expense list tab with filtering."""
    st.subheader("📋 Lista de Gastos")

    # Filter section
    col1, col2, col3 = st.columns(3)

    with col1:
        date_start = st.date_input(
            "Fecha inicial",
            value=date.today() - timedelta(days=30),
            help="Fecha inicial del rango de filtrado",
        )

    with col2:
        date_end = st.date_input(
            "Fecha final",
            value=date.today(),
            help="Fecha final del rango de filtrado",
        )

    with col3:
        manager = get_expense_manager()
        categories = manager.get_categories()
        category_filter = st.selectbox(
            "Categoría",
            options=["Todas"] + categories,
            help="Filtrar por categoría",
        )

    # Validate date range
    if date_start > date_end:
        st.error("⚠️ La fecha inicial no puede ser mayor que la fecha final.")
        return

    # Apply filters
    selected_category = None if category_filter == "Todas" else category_filter
    manager = get_expense_manager()
    filtered_expenses = manager.filter_expenses(
        date_start=date_start,
        date_end=date_end,
        category=selected_category,
    )

    # Display results
    st.markdown("---")
    st.write(f"**{len(filtered_expenses)}** gasto(s) encontrado(s)")

    if filtered_expenses:
        df = expenses_to_dataframe(filtered_expenses)
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Monto": st.column_config.NumberColumn(
                    "Monto",
                    format="$%.2f",
                ),
            },
        )

        # Show total
        total = sum(e.amount for e in filtered_expenses)
        st.info(f"💵 **Total filtrado:** ${total:,.2f}")
    else:
        st.info("ℹ️ No se encontraron gastos con los filtros seleccionados.")


# ─────────────────────────────────────────────
# Tab: Statistics
# ─────────────────────────────────────────────
def render_statistics() -> None:
    """Render the statistics tab."""
    st.subheader("📊 Estadísticas")

    manager = get_expense_manager()
    all_expenses = manager.get_all_expenses()

    if not all_expenses:
        st.info("ℹ️ No hay gastos registrados para mostrar estadísticas.")
        return

    stats_engine = get_statistics_engine()
    stats_engine.set_expenses(all_expenses)
    stats = stats_engine.get_complete_statistics()

    # Key metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Gastado", f"${stats['total_amount']:,.2f}")

    with col2:
        st.metric("Promedio Mensual", f"${stats['monthly_average']:,.2f}")

    with col3:
        st.metric("Número de Gastos", stats['expense_count'])

    with col4:
        date_min, date_max = stats["date_range"]
        if date_min and date_max:
            st.metric("Rango", f"{date_min.strftime('%d/%m/%Y')} - {date_max.strftime('%d/%m/%Y')}")
        else:
            st.metric("Rango", "N/A")

    # Category breakdown
    st.markdown("---")
    st.subheader("Desglose por Categoría")

    category_totals = stats["total_by_category"]
    if category_totals:
        cat_df = pd.DataFrame(
            list(category_totals.items()),
            columns=["Categoría", "Total"],
        )
        st.dataframe(
            cat_df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Total": st.column_config.NumberColumn(
                    "Total",
                    format="$%.2f",
                ),
            },
        )


# ─────────────────────────────────────────────
# Tab: Edit Expense
# ─────────────────────────────────────────────
def render_edit_tab() -> None:
    """Render the edit expense tab."""
    st.subheader("✏️ Editar Gasto")

    manager = get_expense_manager()
    all_expenses = manager.get_all_expenses()

    if not all_expenses:
        st.info("ℹ️ No hay gastos registrados para editar.")
        return

    # Select expense to edit
    expense_options = {
        f"#{e.id} | {e.date.strftime('%d/%m/%Y')} | {e.description} | ${e.amount:,.2f}": e
        for e in all_expenses
    }

    selected_key = st.selectbox(
        "Selecciona el gasto a editar",
        options=list(expense_options.keys()),
        help="Elige el gasto que deseas modificar",
    )

    selected_expense = expense_options[selected_key]

    st.markdown("---")
    st.write("**Valores actuales:**")
    st.write(f"- Fecha: {selected_expense.date.strftime('%d/%m/%Y')}")
    st.write(f"- Descripción: {selected_expense.description}")
    st.write(f"- Monto: ${selected_expense.amount:,.2f}")
    st.write(f"- Categoría: {selected_expense.category}")

    st.markdown("---")
    st.write("**Nuevos valores:**")

    with st.form("edit_expense_form"):
        new_date = st.date_input("Nueva Fecha", value=selected_expense.date)

        categories = [
            "Alimentación",
            "Transporte",
            "Vivienda",
            "Salud",
            "Educación",
            "Entretenimiento",
            "Ropa",
            "Servicios",
            "Otro",
        ]
        new_category = st.selectbox(
            "Nueva Categoría",
            options=categories,
            index=categories.index(selected_expense.category) if selected_expense.category in categories else 0,
        )

        new_amount = st.number_input(
            "Nuevo Monto ($)",
            min_value=0.01,
            value=float(selected_expense.amount),
            step=10.0,
            format="%.2f",
        )

        new_description = st.text_input(
            "Nueva Descripción",
            value=selected_expense.description,
        )

        submitted = st.form_submit_button("💾 Guardar Cambios", use_container_width=True)

        if submitted:
            if not new_description.strip():
                st.error("⚠️ La descripción es obligatoria.")
            else:
                selected_expense.date = new_date
                selected_expense.description = new_description.strip()
                selected_expense.amount = new_amount
                selected_expense.category = new_category
                manager.update_expense(selected_expense)
                st.success("✅ ¡Gasto actualizado exitosamente!")
                refresh_data()


# ─────────────────────────────────────────────
# Tab: Delete Expense
# ─────────────────────────────────────────────
def render_delete_tab() -> None:
    """Render the delete expense tab."""
    st.subheader("🗑️ Eliminar Gasto")

    manager = get_expense_manager()
    all_expenses = manager.get_all_expenses()

    if not all_expenses:
        st.info("ℹ️ No hay gastos registrados para eliminar.")
        return

    # Select expense to delete
    expense_options = {
        f"#{e.id} | {e.date.strftime('%d/%m/%Y')} | {e.description} | ${e.amount:,.2f}": e
        for e in all_expenses
    }

    selected_key = st.selectbox(
        "Selecciona el gasto a eliminar",
        options=list(expense_options.keys()),
        help="Elige el gasto que deseas eliminar",
    )

    selected_expense = expense_options[selected_key]

    st.markdown("---")
    st.write("**Gasto seleccionado:**")
    st.write(f"- ID: {selected_expense.id}")
    st.write(f"- Fecha: {selected_expense.date.strftime('%d/%m/%Y')}")
    st.write(f"- Descripción: {selected_expense.description}")
    st.write(f"- Monto: ${selected_expense.amount:,.2f}")
    st.write(f"- Categoría: {selected_expense.category}")

    st.warning("⚠️ Esta acción no se puede deshacer.")

    col1, col2 = st.columns(2)

    with col1:
        confirm_delete = st.button(
            "🗑️ Confirmar Eliminación",
            type="primary",
            use_container_width=True,
        )

    if confirm_delete:
        manager.delete_expense(selected_expense.id)
        st.success("✅ ¡Gasto eliminado exitosamente!")
        refresh_data()


# ─────────────────────────────────────────────
# Tab: Charts
# ─────────────────────────────────────────────
def render_charts_tab() -> None:
    """Render the charts tab with interactive visualizations."""
    st.subheader("📈 Gráficos y Visualizaciones")

    manager = get_expense_manager()
    all_expenses = manager.get_all_expenses()

    if not all_expenses:
        st.info("ℹ️ No hay gastos registrados para mostrar gráficos.")
        return

    # Chart type selector
    chart_type = st.radio(
        "Tipo de gráfico",
        options=["Barras por Categoría", "Línea Temporal", "Pastel por Categoría"],
        horizontal=True,
        help="Selecciona el tipo de visualización",
    )

    df = expenses_to_dataframe(all_expenses)

    if chart_type == "Barras por Categoría":
        category_totals = df.groupby("Categoría")["Monto"].sum().reset_index()
        category_totals = category_totals.sort_values("Monto", ascending=True)

        fig = px.bar(
            category_totals,
            x="Monto",
            y="Categoría",
            orientation="h",
            title="Total Gastado por Categoría",
            labels={"Monto": "Monto ($)", "Categoría": "Categoría"},
            color="Monto",
            color_continuous_scale="Blues",
        )
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Línea Temporal":
        df["Fecha"] = pd.to_datetime(df["Fecha"])
        daily_totals = df.groupby("Fecha")["Monto"].sum().reset_index()
        daily_totals = daily_totals.sort_values("Fecha")

        fig = px.line(
            daily_totals,
            x="Fecha",
            y="Monto",
            title="Evolución de Gastos en el Tiempo",
            labels={"Fecha": "Fecha", "Monto": "Monto ($)"},
            markers=True,
        )
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Pastel por Categoría":
        category_totals = df.groupby("Categoría")["Monto"].sum().reset_index()

        fig = px.pie(
            category_totals,
            values="Monto",
            names="Categoría",
            title="Distribución de Gastos por Categoría",
            hole=0.4,
        )
        st.plotly_chart(fig, use_container_width=True)


# ─────────────────────────────────────────────
# Main entry point
# ─────────────────────────────────────────────
def main() -> None:
    """Main application entry point."""
    render_sidebar()
    render_main_content()


if __name__ == "__main__":
    main()

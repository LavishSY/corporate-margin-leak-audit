"""
Corporate Margin Leakage Audit Pipeline.

This module automates the extraction, transformation, and export of transactional
sales data to identify and isolate unapproved discount leakages.
"""

from typing import Optional
import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


def get_database_engine(
    user: str = "postgres",
    password: Optional[str] = None,
    host: str = "localhost",
    port: int = 9995,
    dbname: str = "market_mechanics"
) -> Engine:
    """
    Constructs an SQLAlchemy database engine using environment variables or parameters.
    Ensures zero hardcoded credentials in version control.
    """
    db_password: str = password or os.getenv("PGPASSWORD", "")
    connection_uri: str = f"postgresql+psycopg2://{user}:{db_password}@{host}:{port}/{dbname}"
    return create_engine(connection_uri)


def extract_view(engine: Engine, view_name: str = "v_na_corporate_leak") -> pd.DataFrame:
    """
    Extracts raw filtered records directly from the database materialized view.

    Parameters:
        engine (Engine): Active SQLAlchemy database connection engine.
        view_name (str): Name of the relational SQL view to query.

    Returns:
        pd.DataFrame: Retrieved transaction records.
    """
    query: str = f"SELECT * FROM {view_name};"
    df: pd.DataFrame = pd.read_sql(query, con=engine)
    return df


def clean_outliers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Sanitizes data types, validates null values, and maps discount elasticity buckets.

    Parameters:
        df (pd.DataFrame): Raw transactional dataframe.

    Returns:
        pd.DataFrame: Cleaned dataframe ready for financial modeling.
    """
    processed_df: pd.DataFrame = df.copy()

    # Enforce standard numeric precision
    numeric_cols = ["sales_amount", "profit", "discount_percent"]
    for col in numeric_cols:
        if col in processed_df.columns:
            processed_df[col] = pd.to_numeric(processed_df[col], errors="coerce")

    # Segment discount elasticity thresholds
    if "discount_percent" in processed_df.columns:
        bins = [-1.0, 0.05, 0.15, 0.20, 1.0]
        labels = ["Standard (<=5%)", "Moderate (5-15%)", "High (15-20%)", "Hyper-Aggressive (>20%)"]
        processed_df["discount_tier"] = pd.cut(processed_df["discount_percent"], bins=bins, labels=labels)

    return processed_df.dropna(subset=["profit", "sales_amount"])


def export_audit(df: pd.DataFrame, output_path: str = "na_corporate_leak_audit.csv") -> None:
    """
    Exports sanitized audit dataframe to a client-ready CSV feed.

    Parameters:
        df (pd.DataFrame): Final audited dataframe.
        output_path (str): File destination path.
    """
    df.to_csv(output_path, index=False)
    print(f"✅ Production audit feed successfully generated: {output_path}")


if __name__ == "__main__":
    # Operational execution block
    db_engine = get_database_engine()
    raw_data = extract_view(db_engine)
    sanitized_data = clean_outliers(raw_data)
    export_audit(sanitized_data)

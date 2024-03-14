import pandas as pd
from logger_util import setup_logger


logger = setup_logger(__name__)


def insert_data_to_db(engine, df, table_name):

    # Check for existing data
    existing_data_query = f"SELECT id FROM {table_name}"
    existing_data = pd.read_sql(existing_data_query, engine)

    # Filter rows to be inserted based on non-existing primary key values
    rows_to_insert = df[~df["id"].isin(existing_data["id"])]

    # Insert new data into the table
    rows_to_insert.to_sql(table_name, engine, if_exists="append", index=False)

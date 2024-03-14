from logger_util import setup_logger
from sqlalchemy import create_engine

from db_operations import insert_data_to_db
from excel_operations import read_excel_sheet

from config import db_host, db_name, db_password, db_username, excel_file_path, sheets


logger = setup_logger(__name__)


def main():
    try:
        engine = create_engine(
            f"mysql+pymysql://{db_username}:{db_password}@{db_host}/{db_name}"
        )

        for sheet in sheets:
            logger.info(f"Reading data from the sheet: {sheet}.")
            df = read_excel_sheet(excel_file_path, sheet)


            logger.info(f"Inserting data into the table: {sheet}.")
            insert_data_to_db(engine, df, sheet)
        
        logger.info("Data transfer from excel to database successfully completed!")

    except Exception:
        logger.error("An error occured while sending the data from excel sheet to database.")
        raise Exception


if __name__ == "__main__":
    main()

import abc
import enum
import numbers
import os

import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, select, Integer, Float, String, Column
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from app.exceptions import MetadataNotFoundException, DataNotFoundException, DataSourceException


class DataLevel(enum.Enum):
    LEVEL1 = '1'
    LEVEL2 = '2'
    LEVEL3 = '3'


class BaseDataSource(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def get_data(self, table_name: str, data_level: DataLevel) -> pd.DataFrame:
        """
        Retrieve data from the specified table and data level.

        :param table_name: Name of the table (Excel sheet).
        :param data_level: Data level to filter on (NUTS 1, NUTS 2, or NUTS 3).
        :return: DataFrame containing the filtered data.
        :raises DataSourceException: If a general data related error happens.
        :raises DataNotFoundException: If the data could not be found or is empty.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_metadata(self, table_name: str) -> pd.DataFrame:
        """
        Retrieve metadata from the specified table.

        :param table_name: Name of the table
        :return: DataFrame containing the metadata.
        :raises DataSourceException: If a general data related error happens.
        :raises MetadataNotFoundException: If the metadata could not be found or is empty.
        """
        raise NotImplementedError


class FileDataSource(BaseDataSource):
    def __init__(self):
        super().__init__()

    @abc.abstractmethod
    def get_data(self, table_name: str, data_level: DataLevel) -> pd.DataFrame:
        """
        Retrieve data from the specified table and data level.

        :param table_name: Name of the table (Excel sheet).
        :param data_level: Data level to filter on (NUTS 1, NUTS 2, or NUTS 3).
        :return: DataFrame containing the filtered data.
        :raises DataNotFoundException: If the data could not be found or is empty.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_metadata(self, table_name: str) -> pd.DataFrame:
        """
        Retrieve metadata from the specified table.

        :param table_name: Name of the table
        :return: DataFrame containing the metadata.
        :raises MetadataNotFoundException: If the metadata could not be found or is empty.
        """
        raise NotImplementedError


class ExcelDataSource(FileDataSource):
    metadata_rows = 3  # Number based on your actual metadata row count

    def __init__(self, file_name: str):
        """
        Initialize the ExcelDataSource.

        :param file_name: Path to the Excel file.
        """
        super().__init__()
        self.file_name = file_name
        self.data = pd.ExcelFile(self.file_name)

    def get_data(self, table_name: str, data_level: DataLevel) -> pd.DataFrame:
        """
        Retrieve data from the specified table and data level.

        :param table_name: Name of the table (Excel sheet).
        :param data_level: Data level to filter on (NUTS 1, NUTS 2, or NUTS 3).
        :return: DataFrame containing the filtered data.
        :raises DataNotFoundException: If the data could not be found or is empty.
        """
        try:
            sheet = self.data.parse(table_name)
            data = self.get_corrected_data(sheet)

            data = data[data[f'NUTS {data_level.value}'] == data_level.value]
            if data.empty:
                raise DataNotFoundException(f"No data found for table {table_name} with data level {data_level}.")
            return data
        except Exception as e:
            raise DataNotFoundException(f"Error retrieving data from table {table_name}: {e}")

    @staticmethod
    def get_corrected_data(sheet) -> pd.DataFrame:
        """
        Skips the metadata rows and returns the corrected data with its column names

        :param sheet: Sheet containing the data (Excel sheet).
        :return: Correct data with its column names.
        """
        data = sheet.iloc[ExcelDataSource.metadata_rows + 2:]
        columns = [int(column_name) if isinstance(column_name, numbers.Number) else column_name for column_name in
                   sheet.iloc[ExcelDataSource.metadata_rows]]  # remove the trailing zeroes from some years
        data.columns = columns
        return data

    def get_metadata(self, table_name: str) -> pd.DataFrame:
        """
        Retrieve metadata from the specified table.

        :param table_name: Name of the table (Excel sheet).
        :return: DataFrame containing the metadata.
        :raises MetadataNotFoundException: If the metadata could not be found or is empty.
        """
        try:
            metadata = ExcelDataSource.extract_metadata(self.data, table_name)
            if metadata.empty:
                raise MetadataNotFoundException(f"No metadata found for table {table_name}.")
            return metadata
        except Exception as e:
            raise MetadataNotFoundException(f"Error retrieving metadata from table {table_name}: {e}")

    @staticmethod
    def extract_metadata(data: pd.ExcelFile, table_name: str) -> pd.DataFrame:
        """
        Extract the metadata of the wanted table from the given Excel file

        Please note that this function is designed to skip the "Zurück zum Inhaltsverzeichnis" line

        :param data: Excel file to extract its metadata
        :param table_name: Name of the table to get its metadata
        :return: DataFrame containing the metadata
        """
        meta_data = data.parse(table_name, header=None).iloc[:ExcelDataSource.metadata_rows, 0]
        return meta_data.astype(str)


class DatabaseDataSource(BaseDataSource):
    def __init__(self, connection_string):
        """
        Initialize the DatabaseDataSource.

        This class is intended to be used either as an abstract base class or as a stand-alone class, in this project,
        we only explore the first case
        """
        super().__init__()
        self.engine = create_engine(connection_string)
        # self.metadata = MetaData(bind=self.engine)
        self.metadata = MetaData()
        self.Session = sessionmaker(bind=self.engine)

    def get_data(self, table_name, data_level: DataLevel) -> pd.DataFrame:
        """
        Retrieve data from the specified table and data level.

        :param table_name: Name of the table.
        :param data_level: Data level to filter on (NUTS 1, NUTS 2, or NUTS 3).
        :return: DataFrame containing the filtered data.
        :raises DataNotFoundException: If the data could not be found or is empty.
        """
        try:
            session = self.Session()

            table = Table(table_name, self.metadata, autoload_with=self.engine)

            query = select(table).where(getattr(table.columns, f"NUTS {data_level.value}") == data_level.value)

            result = session.execute(query).fetchall()
            session.close()

            # Create a Pandas DataFrame from the results
            df = pd.DataFrame(result, columns=[column.name for column in table.columns])

            return df
        except Exception as e:
            raise DataNotFoundException(f"Error retrieving data: {e}")

    def get_metadata(self, table_name: str) -> pd.DataFrame:
        """
        Retrieve metadata from the specified table.

        This function contains code that can retrieve the real metadata from the table but since it's different from
        the thing that we defined as metadata, it's commented out.
        A good way to do this is to have a metadata table that contains this data.

        :param table_name: Name of the table.
        :return: DataFrame containing the metadata.
        :raises MetadataNotFoundException: If the metadata could not be found or is empty.
        """
        raise NotImplementedError
        # try:
        #     table = Table(table_name, self.metadata, autoload_with=self.engine)
        #     return table.columns.keys()
        # except Exception as e:
        #     raise DataNotFoundException(f"Error retrieving data: {e}")


class SQLiteDataSource(DatabaseDataSource):
    def __init__(self, db_path: str, create_tables_from_excel: bool = False, excel_file: str = None):
        """
        Initialize the SQLiteDataSource.

        This class will load the data from an SQLite database and will create the database if it doesn't exist
        using the specified Excel file (if allowed). Only generates tables for the '1.1' and '3.1' tables.

        :param db_path: Path to the database file.
        :param create_tables_from_excel: Boolean to specify whether to create the database from the Excel file or not.
        :param excel_file: Path to the backup Excel file.
        """
        connection_string = f'sqlite:///{db_path}'
        super().__init__(connection_string)
        self.db_path = db_path
        self.create_tables_from_excel = create_tables_from_excel
        self.excel_file = excel_file

        if create_tables_from_excel and not os.path.exists(db_path):
            self.create_tables_from_excel_file()

    def create_tables_from_excel_file(self):
        """
        Backup function that creates database from an Excel file if it doesn't exist

        Only generates tables for the '1.1' and '3.1' tables
        """
        if not self.excel_file:
            raise DataSourceException("Excel file must be provided to create tables")

        excel_data_source = ExcelDataSource(self.excel_file)
        excel_data = excel_data_source.data

        # for sheet_name in excel_data.sheet_names:
        for sheet_name in ['1.1', '3.1']:
            try:
                sheet_data = excel_data.parse(sheet_name)
                self.create_table_from_sheet(sheet_name, sheet_data)
                # self.add_metadata_to_database(sheet_name, excel_data)
            except Exception as e:
                print(f"Error processing sheet '{sheet_name}': {e}")

    def create_table_from_sheet(self, sheet_name: str, sheet_data: pd.DataFrame):
        """
        Create a table in the database from the data in the specified sheet.

        :param sheet_name: Name of the sheet.
        :param sheet_data: DataFrame containing the sheet data.
        """
        if sheet_data.empty:
            raise DataNotFoundException(f"No data found for sheet '{sheet_name}'")

        with self.engine.connect() as connection:
            corrected_data = ExcelDataSource.get_corrected_data(sheet_data)

            # create the table schema
            self.create_table_from_dataframe_header(self.engine, sheet_name, corrected_data)

            corrected_data.to_sql(sheet_name, con=connection, if_exists='replace', index=False)

    @staticmethod
    def create_table_from_dataframe_header(engine, table_name, df):
        """
        Create a SQLAlchemy table using the header of a Pandas DataFrame.

        :param engine: SQLAlchemy engine.
        :param table_name: Name of the table to create.
        :param df: DataFrame whose header will be used to create the table.
        """
        metadata = MetaData()
        columns = []

        for column_name in df.columns:
            column_type = df[column_name].dtype
            if column_type == 'int64':
                column_type = Integer
            elif column_type == 'float64':
                column_type = Float
            else:
                column_type = String

            columns.append(Column(str(column_name), column_type))

        # Define the table with the determined columns
        table = Table(table_name, metadata, *columns)

        # Create the table in the database
        metadata.create_all(engine)

    def add_metadata_to_database(self, sheet_name: str, excel_data: pd.ExcelFile):
        """
        Add metadata to the database.

        This function contains code that can add metadata to a table but since this extra info can't be
        just added to a table, we have commented this part out.
        A good way to do this is to have a metadata table that contains this data.

        :param sheet_name: Name of the table sheet.
        :param excel_data: Excel data containing the metadata.
        """
        raise NotImplementedError
        # metadata = ExcelDataSource.extract_metadata(excel_data, sheet_name)
        # metadata_dict = metadata.to_dict()
        #
        # with self.engine.connect() as connection:
        #     for key, value in metadata_dict.items():
        #         sql = text(f"INSERT INTO metadata (sheet_name, key, value) VALUES (:sheet_name, :key, :value)")
        #         for k, v in value.items():
        #             connection.execute(sql, table_name=sheet_name, key=k, value=v)

    def get_data(self, table_name, data_level: DataLevel) -> pd.DataFrame:
        """
        Retrieve data from the specified table and data level.

        :param table_name: Name of the table.
        :param data_level: Data level to filter on (NUTS 1, NUTS 2, or NUTS 3).
        :return: DataFrame containing the filtered data.
        :raises DataNotFoundException: If the data could not be found or is empty.
        """
        if not os.path.exists(self.db_path) and self.create_tables_from_excel:
            self.create_tables_from_excel_file()

        try:
            return super().get_data(table_name, data_level)
        except SQLAlchemyError as e:
            raise DataNotFoundException(f"Error retrieving data: {e}")

    def get_metadata(self, table_name: str) -> pd.DataFrame:
        """
        Retrieve metadata from the specified table.


        This function contains code that can retrieve the real metadata from the table but since it's different from
        the thing that we defined as metadata, it's commented out.
        A good way to do this is to have a metadata table that contains this data.

        :param table_name: Name of the table.
        :return: DataFrame containing the metadata.
        :raises MetadataNotFoundException: If the metadata could not be found or is empty.
        """
        raise NotImplementedError
        # try:
        #     return super().get_metadata(table_name)
        # except SQLAlchemyError as e:
        #     raise DataNotFoundException(f"Error retrieving data: {e}")


def get_data_source(config):
    data_source_type = config['data_source']['type']

    if data_source_type == 'sqlite':
        db_config = config['data_source']['sqlite']
        return SQLiteDataSource(
            db_path=db_config['db_path'],
            create_tables_from_excel=db_config['create_tables_from_excel'],
            excel_file=db_config['excel_file']
        )
    elif data_source_type == 'excel':
        excel_config = config['data_source']['excel']
        return ExcelDataSource(
            file_name=excel_config['file_name'],
        )
    else:
        raise DataSourceException(f"Unknown data source type: {data_source_type}")

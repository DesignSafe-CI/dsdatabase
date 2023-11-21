import os
import pandas as pd
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text


class DSDatabase:
    """A database utility class for connecting to a DesignSafe SQL database.

    This class provides functionality to connect to a MySQL database using
    SQLAlchemy and PyMySQL. It supports executing SQL queries and returning
    results in different formats.

    Attributes:
        user (str): Database username, defaults to 'dspublic'.
        password (str): Database password, defaults to 'R3ad0nlY'.
        host (str): Database host address, defaults to '129.114.52.174'.
        port (int): Database port, defaults to 3306.
        db (str): Database name, can be 'sjbrande_ngl_db', 'sjbrande_vpdb', or 'post_earthquake_recovery'.
        recycle_time (int): Time in seconds to recycle database connections.
        engine (Engine): SQLAlchemy engine for database connection.
        Session (sessionmaker): SQLAlchemy session maker bound to the engine.
    """

    def __init__(self, dbname="sjbrande_ngl_db"):
        """Initializes the DSDatabase instance with environment variables and creates the database engine.

        Args:
            dbname (str): Database name. Must be one of 'sjbrande_ngl_db', 'sjbrande_vpdb', or 'post_earthquake_recovery'.
        """
        allowed_dbnames = [
            "sjbrande_ngl_db",
            "sjbrande_vpdb",
            "post_earthquake_recovery",
        ]
        if dbname not in allowed_dbnames:
            raise ValueError(
                f"Invalid database name '{dbname}'. Allowed names are: {', '.join(allowed_dbnames)}"
            )

        self.user = os.getenv("DB_USER", "dspublic")
        self.password = os.getenv("DB_PASSWORD", "R3ad0nlY")
        self.host = os.getenv("DB_HOST", "129.114.52.174")
        self.port = os.getenv("DB_PORT", 3306)
        self.db = dbname
        self.recycle_time = 3600  # 1 hour in seconds

        # Setup the database connection
        self.engine = create_engine(
            f"mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}",
            pool_recycle=self.recycle_time,
        )
        self.Session = sessionmaker(bind=self.engine)

    def read_sql(self, sql, output_type="DataFrame"):
        """Executes a SQL query and returns the results.

        Args:
            sql (str): The SQL query string to be executed.
            output_type (str, optional): The format for the query results. Defaults to 'DataFrame'.
                Possible values are 'DataFrame' for a pandas DataFrame, or 'dict' for a list of dictionaries.

        Returns:
            pandas.DataFrame or list of dict: The result of the SQL query.

        Raises:
            ValueError: If the SQL query string is empty or if the output type is not valid.
            SQLAlchemyError: If an error occurs during query execution.
        """
        if not sql:
            raise ValueError("SQL query string is required")

        if output_type not in ["DataFrame", "dict"]:
            raise ValueError('Output type must be either "DataFrame" or "dict"')

        session = self.Session()

        try:
            if output_type == "DataFrame":
                return pd.read_sql_query(sql, session.bind)
            else:
                # Convert SQL string to a text object
                sql_text = text(sql)
                result = session.execute(sql_text)
                return [dict(row) for row in result]
        except exc.SQLAlchemyError as e:
            raise Exception(f"SQLAlchemyError: {e}")
        finally:
            session.close()

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

class DBStorage:
    """DBStorage class."""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = "user"
        HBNB_MYSQL_PWD = "web_app"
        HBNB_MYSQL_HOST = "localhost"
        HBNB_MYSQL_DB = "web_app"
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB))
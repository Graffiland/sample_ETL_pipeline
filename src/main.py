from sqlalchemy import create_engine
from sqlalchemy_utils  import database_exists, create_database
from connection_param import connection
from src.ddl import create_tables
    


def get_engine(user,passwd,host,db):
    url = f"postgresql://{user}:{passwd}@{host}/{db}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url,pool_size=50, echo=False)
    return engine




if __name__ == '__main__':
    engine = get_engine(connection['user'],connection['passwd'],connection['host'],connection['db'])
    print('current engine', engine.url)

    create_tables(engine)

    
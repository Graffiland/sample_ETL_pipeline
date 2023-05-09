
from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData, Boolean, DateTime, Float

# tables
def create_tables(engine):
    '''
    Function creates the tables for the database

    input: database engine

    '''
    metadata_obj = MetaData()
    country = Table(
        "country", metadata_obj,
        Column("country_id", Integer, primary_key=True),
        Column("country", String(100)),
        Column("last_update",DateTime)
    )

    city = Table(
        "city", metadata_obj,
        Column("city_id",Integer, primary_key=True),
        Column("city", String(100)),
        Column("country_id", Integer, ForeignKey("country.country_id"), nullable=False),
        Column("last_update",DateTime)
    )


    address = Table(
        "address", metadata_obj,
        Column("address_id",Integer, primary_key=True),
        Column("address", String(200)),
        Column("address2", String(200)),
        Column("district",String(100)),
        Column("city_id",Integer, ForeignKey("city.city_id"),nullable=False),
        Column("postal_code",Integer),
        Column("phone",String),
        Column("last_update",DateTime)
    )

    customer = Table(
        "customer", metadata_obj,
        Column("customer_id", Integer, primary_key=True),
        Column("store_id", Integer),
        Column("first_name",String(100)),
        Column("last_name", String(100)),
        Column("email",String(100)),
        Column("address_id", Integer,ForeignKey("address.address_id"),nullable=False),
        Column("activebool",Boolean),
        Column("create_date",DateTime),
        Column("last_update",DateTime),
        Column("active",Integer),
    )

    payment = Table(
        "payment" , metadata_obj,
        Column("payment_id",Integer, primary_key=True),
        Column("customer_id",Integer),
        Column("staff_id",Integer),
        Column("amount",Float),
        Column("payment_date",DateTime)

    )

    # create tables
    metadata_obj.create_all(engine)




from sqlalchemy import Column, Float, String, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class DataPoint(Base):
    __tablename__ = "data_points"

    pk = Column(
        BigInteger, index=True, nullable=False, primary_key=True, autoincrement=True
    )
    id = Column(String(250), index=True, nullable=False)
    type = Column(String(250), index=True, nullable=False)
    temperature_f = Column(Float, nullable=False)
    temperature_c = Column(Float, nullable=False)
    time_of_measurement = Column(DateTime, index=True, nullable=False)


engine = create_engine("postgresql://postgres:@localhost/sensors")


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

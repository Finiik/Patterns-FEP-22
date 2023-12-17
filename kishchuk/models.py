from sqlalchemy import ( Column,
                         Integer,
                         String,
                         Float,
                         PickleType,
                         Boolean,
                         )
from sqlalchemy.orm import (
                            declarative_base,
)
Base = declarative_base()


class CreditCardTable(Base):
    __tablename__ = 'credit_cards'

    id = Column(Integer, primary_key=True, autoincrement=True)
    client = Column(String, nullable=False)
    account_number = Column(String, unique=True, nullable=False)
    credit_limit = Column(Float, nullable=False)
    grace_period = Column(Integer, nullable=False)
    cvv_hash = Column(PickleType)


class PersonalInfoTable(Base):
    __tablename__ = 'personal_info'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    client_type = Column(String, nullable=False)
    account_number = Column(String, unique=True, nullable=False)
    cvv = Column(String, nullable=False)


class BankInfoTable(Base):
    __tablename__ = 'bank_info'

    id = Column(Integer, primary_key=True, autoincrement=True)
    bank_name = Column(String, nullable=False)
    holder_name = Column(String, nullable=False)
    accounts_number = Column(String, nullable=True)
    credit_history = Column(String, nullable=True)


class BankCustomerTable(Base):
    __tablename__ = 'bank_customer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    personal_info_id = Column(Integer, nullable=False)
    bank_info_id = Column(Integer, nullable=False)
    vip_status = Column(Boolean, default=False)
    individual_status = Column(Boolean, default=False)
    corporate_status = Column(Boolean, default=False)
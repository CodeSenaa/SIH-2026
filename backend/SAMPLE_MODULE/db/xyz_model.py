from tc_auth.db import Base
from sqlalchemy import Column , String , Integer , DateTime 
from datetime import datetime

class SampleTable(Base):
    __tablename__ = "sample_table"

    id = Column(Integer , primary_key=True)
    name = Column(String , nullable=False)
    age = Column(Integer)
    created_at = Column(DateTime)

    def __init__(self , name , age , created_at = datetime.now()):
        self.name = name
        self.age = age
        self.created_at = created_at
import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Ser(Base):
   __tablename__ = 'child_emotion'
   upload_id = Column(Integer, primary_key=True)
   child_id= Column(Integer, nullable=False)
   emotion = Column(String(250), nullable=False)
   last_updated = Column(TIMESTAMP, nullable=False)



engine = create_engine('mysql:///ser_db.db')
Base.metadata.create_all(engine)
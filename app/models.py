from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Text
from sqlalchemy.dialects.postgresql import UUID
import uuid

Base = declarative_base()

class Document(Base):
    __tablename__ = "documents"
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    filename = Column(String)
    content = Column(Text)

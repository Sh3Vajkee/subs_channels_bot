from sqlalchemy import BigInteger, Boolean, Column, Integer, String, Text

from db.base import Base


class GroupsUsers(Base):
    __tablename__ = "groupsusers"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger)
    group_id = Column(BigInteger)

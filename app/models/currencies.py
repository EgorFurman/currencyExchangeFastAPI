from app.database import Base

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Currencies(Base):
    __tablename__ = 'currencies'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(String(3), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(36), nullable=False)
    sign: Mapped[str] = mapped_column(String(1), nullable=False)

    def __repr__(self):
        return f'Currency: (id = {self.id}, code = {self.code}, name = {self.name}, sign = {self.sign})'

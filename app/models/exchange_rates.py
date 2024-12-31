from app.database import Base

from sqlalchemy import ForeignKey, DECIMAL, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.currencies import Currencies


class ExchangeRates(Base):
    __tablename__ = 'exchange_rates'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    base_currency_id: Mapped[int] = mapped_column(
        ForeignKey('currencies.id', ondelete="CASCADE"), nullable=False
    )
    target_currency_id: Mapped[int] = mapped_column(
        ForeignKey('currencies.id', ondelete="CASCADE"), nullable=False
    )
    rate: Mapped[DECIMAL] = mapped_column(
        DECIMAL(precision=9, scale=6)
    )

    base_currency: Mapped["Currencies"] = relationship(foreign_keys='ExchangeRates.base_currency_id')
    target_currency: Mapped["Currencies"] = relationship(foreign_keys='ExchangeRates.target_currency_id')

    __table_args__ = (
        UniqueConstraint('base_currency_id', 'target_currency_id', name='unique_currency_pair'),
    )

    def __repr__(self):
        return f'ExchangeRate: (id = {self.id}, base_currency_id = {self.base_currency_id}, target_currency_id = {self.target_currency_id}, rate = {self.rate})'
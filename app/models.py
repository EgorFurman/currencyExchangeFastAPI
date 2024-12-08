from sqlalchemy import String, ForeignKey, DECIMAL, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Currencies(Base):
    __tablename__ = 'currencies'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(String(3), unique=True, index=True, nullable=False)
    full_name: Mapped[str] = mapped_column(String(36), nullable=False)
    sign: Mapped[str] = mapped_column(String(1), nullable=False)


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

    base_currency: Mapped[str] = relationship('Currencies', foreign_keys='ExchangeRates.base_currency_id')
    target_currency: Mapped[str] = relationship('Currencies', foreign_keys='ExchangeRates.target_currency_id')

    __table_args__ = (
        UniqueConstraint('base_currency_id', 'target_currency_id', name='unique_currency_pair'),
    )

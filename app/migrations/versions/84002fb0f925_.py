"""empty message

Revision ID: 84002fb0f925
Revises: e4d845f1bec1
Create Date: 2024-12-11 19:52:27.189926

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84002fb0f925'
down_revision: Union[str, None] = 'e4d845f1bec1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('currencies', sa.Column('name', sa.String(length=36), nullable=False))
    op.drop_column('currencies', 'full_name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('currencies', sa.Column('full_name', sa.VARCHAR(length=36), autoincrement=False, nullable=False))
    op.drop_column('currencies', 'name')
    # ### end Alembic commands ###

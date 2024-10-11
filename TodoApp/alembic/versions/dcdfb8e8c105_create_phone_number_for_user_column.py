"""Create phone number for user column

Revision ID: dcdfb8e8c105
Revises: 
Create Date: 2024-10-09 22:29:03.417703

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dcdfb8e8c105'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(length=15), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'phone_number')

"""add content column to posts table

Revision ID: 590c26c2866c
Revises: 8d2707dc8215
Create Date: 2024-05-16 08:16:41.516734

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '590c26c2866c'
down_revision: Union[str, None] = '8d2707dc8215'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass

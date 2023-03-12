"""ugrade review date changing

Revision ID: ed5977ad1121
Revises: a1a354884ece
Create Date: 2023-03-11 20:05:12.055596

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed5977ad1121'
down_revision = 'a1a354884ece'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute('ALTER TABLE review RENAME COLUMN created TO updated')


def downgrade() -> None:
    pass

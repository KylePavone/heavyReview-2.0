"""update tag table

Revision ID: 961093b9aef7
Revises: ed5977ad1121
Create Date: 2023-03-12 22:18:19.043355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '961093b9aef7'
down_revision = 'ed5977ad1121'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("ALTER TABLE tag RENAME COLUMN tag_name TO name")


def downgrade() -> None:
    pass

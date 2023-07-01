"""Modificar tabla users

Revision ID: 5595fc01fb4e
Revises: 
Create Date: 2023-06-30 23:14:44.537096

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5595fc01fb4e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute('UPDATE users SET usr_enabled = true WHERE usr_id = 2')


def downgrade() -> None:
    op.execute('UPDATE users SET usr_enabled = false WHERE usr_id = 2')

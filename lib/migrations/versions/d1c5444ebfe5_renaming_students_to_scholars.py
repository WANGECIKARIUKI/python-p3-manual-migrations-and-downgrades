"""Renaming students to scholars

Revision ID: d1c5444ebfe5
Revises: 791279dd0760
Create Date: 2023-11-03 10:46:49.821887

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1c5444ebfe5'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')

"""merge latest heads

Revision ID: 3e9581ec2511
Revises: 9b3050409b66, 0ab65e1cc7fa
Create Date: 2025-06-25 17:28:49.723995

"""
from alembic import op
import models as models
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e9581ec2511'
down_revision = ('9b3050409b66', '0ab65e1cc7fa')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass

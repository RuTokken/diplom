"""Initial mig2.

Revision ID: ac13435d0ac2
Revises: ac1b27e7ff7e
Create Date: 2020-10-31 13:35:00.940590

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac13435d0ac2'
down_revision = 'ac1b27e7ff7e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('auto', sa.Column('status', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('auto', 'status')
    # ### end Alembic commands ###
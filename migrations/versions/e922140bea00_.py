"""empty message

Revision ID: e922140bea00
Revises: c044a4686e0d
Create Date: 2022-01-08 16:33:11.051551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e922140bea00'
down_revision = 'c044a4686e0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('ip', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'ip')
    # ### end Alembic commands ###

"""empty message

Revision ID: c044a4686e0d
Revises: 922134981cb5
Create Date: 2022-01-07 18:40:20.702849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c044a4686e0d'
down_revision = '922134981cb5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(), nullable=True),
    sa.Column('answer', sa.String(), nullable=True),
    sa.Column('source', sa.String(), nullable=True),
    sa.Column('imgur', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('questions')
    # ### end Alembic commands ###

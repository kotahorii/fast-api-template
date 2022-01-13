"""remove column from user

Revision ID: a97892b578a8
Revises: ed03301a47f3
Create Date: 2022-01-13 12:49:53.705698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a97892b578a8'
down_revision = 'ed03301a47f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('introduction', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'introduction')
    # ### end Alembic commands ###

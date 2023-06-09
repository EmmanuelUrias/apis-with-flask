"""empty message

Revision ID: 3d4c906ffb9c
Revises: 
Create Date: 2023-03-28 10:37:59.184696

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d4c906ffb9c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reptiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('reptile_name', sa.String(length=250), nullable=True),
    sa.Column('reptile_age', sa.Integer(), nullable=True),
    sa.Column('reptile_weight', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reptiles')
    # ### end Alembic commands ###

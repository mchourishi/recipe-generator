"""Initial migration

Revision ID: 7943c1b3c9ea
Revises: 
Create Date: 2024-12-02 14:11:08.441131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7943c1b3c9ea'
down_revision = None
branch_labels = None
depends_on = None


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipes')
    # ### end Alembic commands ###


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recipes',
    sa.Column('name', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('ingredients', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('instructions', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('cuisine', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('meal_type', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), sa.Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='recipes_pkey')
    )
    # ### end Alembic commands ###

"""empty message

Revision ID: bffe0c7544a0
Revises: ed433ae8292e
Create Date: 2021-03-23 22:59:40.831665

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bffe0c7544a0'
down_revision = 'ed433ae8292e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('property',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('bedrooms', sa.String(length=10), nullable=True),
    sa.Column('bathrooms', sa.String(length=10), nullable=True),
    sa.Column('price', sa.String(length=30), nullable=True),
    sa.Column('p_type', sa.String(length=20), nullable=True),
    sa.Column('location', sa.String(length=200), nullable=True),
    sa.Column('photo', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('location')
    )
    op.drop_table('Properties')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Properties',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Properties_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('bedrooms', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('bathrooms', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('p_type', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('location', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('photo', sa.VARCHAR(length=150), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='Properties_pkey'),
    sa.UniqueConstraint('location', name='Properties_location_key')
    )
    op.drop_table('property')
    # ### end Alembic commands ###

"""Add Instance Config table

Revision ID: 6f4e4b65b9be
Revises: faac8092c123
Create Date: 2018-06-04 19:00:24.955189

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f4e4b65b9be'
down_revision = 'faac8092c123'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('instanceconfig',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=96), nullable=True, unique=True),
    sa.Column('value', sa.String(length=2000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('instanceconfig')
    # ### end Alembic commands ###
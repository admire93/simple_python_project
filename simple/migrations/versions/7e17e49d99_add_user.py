"""add user

Revision ID: 7e17e49d99
Revises: 22a28b2955d
Create Date: 2015-03-03 02:16:56.814170

"""

# revision identifiers, used by Alembic.
revision = '7e17e49d99'
down_revision = '22a28b2955d'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('name', sa.Unicode(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    ### end Alembic commands ###

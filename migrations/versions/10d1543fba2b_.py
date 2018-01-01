"""empty message

Revision ID: 10d1543fba2b
Revises: b9006c99ce5b
Create Date: 2018-01-01 00:22:21.392398

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10d1543fba2b'
down_revision = 'b9006c99ce5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('email', sa.String(length=80), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'email')
    # ### end Alembic commands ###
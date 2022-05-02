"""empty message

Revision ID: 64f918b70452
Revises: 97a40f73b06f
Create Date: 2022-05-02 11:36:21.132452

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '64f918b70452'
down_revision = '97a40f73b06f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('partida', 'time')
    op.drop_column('partida', 'status')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('partida', sa.Column('status', mysql.VARCHAR(length=255), nullable=True))
    op.add_column('partida', sa.Column('time', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    # ### end Alembic commands ###

"""empty message

Revision ID: cd273b3136ff
Revises: c0fc722ab60c
Create Date: 2022-04-04 10:33:32.496544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd273b3136ff'
down_revision = 'c0fc722ab60c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('resultado', sa.Column('player_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'resultado', 'user', ['player_id'], ['user_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'resultado', type_='foreignkey')
    op.drop_column('resultado', 'player_id')
    # ### end Alembic commands ###

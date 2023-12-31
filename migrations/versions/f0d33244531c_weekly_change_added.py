"""weekly change added

Revision ID: f0d33244531c
Revises: f9d319783444
Create Date: 2023-10-27 06:58:26.587985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0d33244531c'
down_revision = 'f9d319783444'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('datapoint', schema=None) as batch_op:
        batch_op.alter_column('weight',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=True)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('weekly_change', sa.String(), nullable=True))
        batch_op.create_index(batch_op.f('ix_user_weekly_change'), ['weekly_change'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_weekly_change'))
        batch_op.drop_column('weekly_change')

    with op.batch_alter_table('datapoint', schema=None) as batch_op:
        batch_op.alter_column('weight',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=True)

    # ### end Alembic commands ###

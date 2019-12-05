"""empty message

Revision ID: 4868780239ae
Revises: edbb16bd3137
Create Date: 2019-12-05 21:59:38.201619

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4868780239ae'
down_revision = 'edbb16bd3137'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('website', sa.String(length=120), nullable=True))
    op.add_column('Artist', sa.Column('seeking_description', sa.Text(), nullable=True))
    op.add_column('Artist', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'website')
    op.drop_column('Artist', 'seeking_venue')
    op.drop_column('Artist', 'seeking_description')
    # ### end Alembic commands ###

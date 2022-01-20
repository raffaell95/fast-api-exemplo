"""Column tamanho

Revision ID: 782f8fdedd72
Revises: 2e11cab4c1ff
Create Date: 2021-12-22 19:28:26.321054

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '782f8fdedd72'
down_revision = '2e11cab4c1ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('produto', sa.Column('tamanhos', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('produto', 'tamanhos')
    # ### end Alembic commands ###
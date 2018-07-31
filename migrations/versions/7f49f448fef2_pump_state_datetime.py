"""pump state datetime

Revision ID: 7f49f448fef2
Revises: 615d84380efd
Create Date: 2018-07-29 16:58:10.995522

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f49f448fef2'
down_revision = '615d84380efd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pump', sa.Column('state_update_date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pump', 'state_update_date')
    # ### end Alembic commands ###
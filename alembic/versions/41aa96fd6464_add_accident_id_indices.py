"""add_accident_id_indices

Revision ID: 41aa96fd6464
Revises: 5a5ffe56bb7
Create Date: 2018-07-05 13:23:02.393175

"""

# revision identifiers, used by Alembic.
revision = '41aa96fd6464'
down_revision = '5a5ffe56bb7'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index('accident_id_idx_involved', 'involved', ['accident_id'], unique=False)
    op.create_index('id_idx_markers', 'markers', ['id'], unique=True)
    op.create_index('accident_id_idx_vehicles', 'vehicles', ['accident_id'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('accident_id_idx_vehicles', table_name='vehicles')
    op.drop_index('id_idx_markers', table_name='markers')
    op.drop_index('accident_id_idx_involved', table_name='involved')
    ### end Alembic commands ###

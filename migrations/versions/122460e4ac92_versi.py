"""versi

Revision ID: 122460e4ac92
Revises: ad4e167f48b6
Create Date: 2023-11-23 04:01:46.041037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '122460e4ac92'
down_revision = 'ad4e167f48b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('modul', schema=None) as batch_op:
        batch_op.add_column(sa.Column('photo_path', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('modul', schema=None) as batch_op:
        batch_op.drop_column('photo_path')

    # ### end Alembic commands ###

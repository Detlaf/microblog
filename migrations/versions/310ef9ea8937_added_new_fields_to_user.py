"""added new fields to user

Revision ID: 310ef9ea8937
Revises: 12468fbe21a8
Create Date: 2020-06-19 12:42:21.401731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '310ef9ea8937'
down_revision = '12468fbe21a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###

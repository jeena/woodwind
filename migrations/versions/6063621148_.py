"""empty message

Revision ID: 6063621148
Revises: None
Create Date: 2015-04-18 17:44:08.465907

"""

# revision identifiers, used by Alembic.
revision = '6063621148'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_entry_feed_id', table_name='entry')
    op.drop_index('idx_entry_id', table_name='entry')
    op.drop_index('idx_entry_permalink', table_name='entry')
    op.drop_index('idx_entry_retrieved', table_name='entry')
    op.drop_index('idx_feed_id', table_name='feed')
    op.drop_constraint(None, 'feed', type_='foreignkey')
    op.drop_column('feed', 'user_id')
    op.drop_index('idx_user_id', table_name='user')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index('idx_user_id', 'user', ['id'], unique=False)
    op.add_column('feed', sa.Column('user_id', sa.INTEGER(), nullable=True))
    op.create_foreign_key(None, 'feed', 'user', ['user_id'], ['id'])
    op.create_index('idx_feed_id', 'feed', ['id'], unique=False)
    op.create_index('idx_entry_retrieved', 'entry', ['retrieved'], unique=False)
    op.create_index('idx_entry_permalink', 'entry', ['permalink'], unique=False)
    op.create_index('idx_entry_id', 'entry', ['id'], unique=False)
    op.create_index('idx_entry_feed_id', 'entry', ['feed_id'], unique=False)
    ### end Alembic commands ###

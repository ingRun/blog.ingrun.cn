"""empty message

Revision ID: 703cfa46cc60
Revises: 
Create Date: 2020-03-07 15:46:08.913891

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '703cfa46cc60'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ip',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sum_', sa.Integer(), nullable=True),
    sa.Column('last_seven_days', sa.String(length=80), nullable=True),
    sa.Column('today_count', sa.Integer(), nullable=True),
    sa.Column('today_time', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('password', sa.String(length=30), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=11), nullable=True),
    sa.Column('token', sa.String(length=32), nullable=True),
    sa.Column('token_expiration', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_user_token'), 'user', ['token'], unique=True)
    op.create_table('blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('blog_title', sa.String(length=100), nullable=True),
    sa.Column('author', sa.Integer(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('contents', sa.Text(), nullable=True),
    sa.Column('read_count', sa.Integer(), nullable=True),
    sa.Column('like_count', sa.Integer(), nullable=True),
    sa.Column('blog_type', sa.String(length=200), nullable=True),
    sa.Column('preview', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['author'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_blog_blog_title'), 'blog', ['blog_title'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_blog_blog_title'), table_name='blog')
    op.drop_table('blog')
    op.drop_index(op.f('ix_user_token'), table_name='user')
    op.drop_table('user')
    op.drop_table('ip')
    # ### end Alembic commands ###
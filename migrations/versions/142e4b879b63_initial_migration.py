"""Initial migration.

Revision ID: 142e4b879b63
Revises: 
Create Date: 2024-03-13 14:54:56.469680

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '142e4b879b63'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('survey',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('authenticated', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name')
    )
    op.create_table('survey_question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('survey_id', sa.Integer(), nullable=True),
    sa.Column('question', sa.String(length=500), nullable=False),
    sa.ForeignKeyConstraint(['survey_id'], ['survey.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('survey_response',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('response', sa.String(length=500), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['survey_question.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('survey_response')
    op.drop_table('survey_question')
    op.drop_table('user')
    op.drop_table('survey')
    # ### end Alembic commands ###

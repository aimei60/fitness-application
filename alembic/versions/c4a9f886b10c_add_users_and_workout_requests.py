"""Add users and workout requests

Revision ID: c4a9f886b10c
Revises: 
Create Date: 2025-04-11 14:09:40.158783

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c4a9f886b10c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.Column('Email', sa.String(length=100), nullable=False),
    sa.Column('HashedPassword', sa.String(), nullable=False),
    sa.Column('IsActive', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('ID')
    )
    op.create_index(op.f('ix_users_Email'), 'users', ['Email'], unique=True)
    op.create_table('user_workout_requests',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.Column('UserID', sa.Integer(), nullable=False),
    sa.Column('WorkoutID', sa.Integer(), nullable=False),
    sa.Column('RequestType', sa.String(length=100), nullable=False),
    sa.Column('Status', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['UserID'], ['users.ID'], ),
    sa.ForeignKeyConstraint(['WorkoutID'], ['WorkOuts.ID'], ),
    sa.PrimaryKeyConstraint('ID')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_workout_requests')
    op.drop_index(op.f('ix_users_Email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###

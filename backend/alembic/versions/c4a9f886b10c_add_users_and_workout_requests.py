"""Add users and workout requests

Revision ID: c4a9f886b10c
Revises:
Create Date: 2025-04-11 14:09:40.158783
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "c4a9f886b10c"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # 1) Create WorkOuts FIRST (matches ORM: __tablename__ = "WorkOuts")
    op.create_table(
        "WorkOuts",
        sa.Column("ID", sa.Integer(), primary_key=True, autoincrement=True, nullable=False),
        sa.Column("Name", sa.String(length=50), nullable=False),
        sa.Column("Description", sa.Text(), nullable=True),
    )

    # 2) Create users
    op.create_table(
        "users",
        sa.Column("ID", sa.Integer(), primary_key=True, autoincrement=True, nullable=False),
        sa.Column("Email", sa.String(length=100), nullable=False),
        sa.Column("HashedPassword", sa.String(), nullable=False),
        sa.Column("IsActive", sa.Boolean(), nullable=False, server_default=sa.text("TRUE")),
    )
    op.create_index("ix_users_Email", "users", ["Email"], unique=True)

    # 3) Create user_workout_requests (FKs AFTER parents exist; no manual quoting)
    op.create_table(
        "user_workout_requests",
        sa.Column("ID", sa.Integer(), primary_key=True, autoincrement=True, nullable=False),
        sa.Column("UserID", sa.Integer(), nullable=False),
        sa.Column("WorkoutID", sa.Integer(), nullable=True),
        sa.Column("RequestType", sa.String(length=100), nullable=False),
        sa.Column("Status", sa.String(length=50), nullable=False, server_default="pending"),
        sa.ForeignKeyConstraint(["UserID"], ["users.ID"]),
        sa.ForeignKeyConstraint(["WorkoutID"], ["WorkOuts.ID"]),
    )

def downgrade() -> None:
    op.drop_table("user_workout_requests")
    op.drop_index("ix_users_Email", table_name="users")
    op.drop_table("users")
    op.drop_table("WorkOuts")

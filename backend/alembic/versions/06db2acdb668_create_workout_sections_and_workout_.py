"""Create Workout_Sections and Workout_Routine tables

Revision ID: 06db2acdb668
Revises: cdc46b99ed2d
Create Date: 2025-09-22 15:06:23.712791

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '06db2acdb668'
down_revision: Union[str, None] = 'cdc46b99ed2d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # 1) Workout_Sections
    op.create_table(
        "Workout_Sections",
        sa.Column("ID", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("WOID", sa.Integer(), nullable=False),
        sa.Column("SectionName", sa.String(length=50), nullable=False),
        sa.Column("SectionOrder", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["WOID"], ["WorkOuts.ID"], name="Workout_Sections_WOID_fkey"),
    )

    # 2) Workout_Routine (depends on Workout_Sections)
    op.create_table(
        "Workout_Routine",
        sa.Column("ID", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("SectionID", sa.Integer(), nullable=False),
        sa.Column("Name", sa.String(length=50), nullable=False),
        sa.Column("RepsDuration", sa.String(length=20), nullable=False),
        sa.Column("RoutineDescription", sa.String(length=255), nullable=False),
        sa.Column("ExerciseOrder", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["SectionID"], ["Workout_Sections.ID"], name="Workout_Routine_SectionID_fkey"),
    )

def downgrade() -> None:
    op.drop_table("Workout_Routine")
    op.drop_table("Workout_Sections")
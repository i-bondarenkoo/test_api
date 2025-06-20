"""create table books

Revision ID: 379568d8daea
Revises: eeb72f06f879
Create Date: 2025-06-11 11:02:55.380152

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "379568d8daea"
down_revision: Union[str, None] = "eeb72f06f879"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "books",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=35), nullable=False),
        sa.Column("published_year", sa.Integer(), nullable=False),
        sa.Column("author_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["author_id"],
            ["authors.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("books")
    # ### end Alembic commands ###

"""initial OpenPulse schema"""
from alembic import op
import sqlalchemy as sa

revision = "0001_initial"
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table("users",
        sa.Column("id", sa.Integer(), primary_key=True), sa.Column("username", sa.String(50), nullable=False),
        sa.Column("email", sa.String(255), nullable=False), sa.Column("hashed_password", sa.String(255), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_index("ix_users_username", "users", ["username"], unique=True)
    op.create_index("ix_users_email", "users", ["email"], unique=True)
    op.create_table("repositories",
        sa.Column("id", sa.Integer(), primary_key=True), sa.Column("github_id", sa.Integer(), nullable=True),
        sa.Column("full_name", sa.String(255), nullable=False), sa.Column("owner", sa.String(100), nullable=False),
        sa.Column("name", sa.String(150), nullable=False), sa.Column("description", sa.Text(), nullable=True),
        sa.Column("html_url", sa.String(500), nullable=True), sa.Column("language", sa.String(100), nullable=True),
        sa.Column("stars", sa.Integer(), nullable=False, server_default="0"), sa.Column("forks", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("open_issues", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_index("ix_repositories_full_name", "repositories", ["full_name"], unique=True)
    op.create_index("ix_repositories_github_id", "repositories", ["github_id"], unique=True)
    op.create_table("bookmarks",
        sa.Column("id", sa.Integer(), primary_key=True), sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("repository_id", sa.Integer(), nullable=False), sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"), sa.ForeignKeyConstraint(["repository_id"], ["repositories.id"], ondelete="CASCADE"),
        sa.UniqueConstraint("user_id", "repository_id", name="uq_user_repository_bookmark"),
    )
    op.create_index("ix_bookmarks_user_id", "bookmarks", ["user_id"])
    op.create_index("ix_bookmarks_repository_id", "bookmarks", ["repository_id"])

def downgrade():
    op.drop_table("bookmarks"); op.drop_table("repositories"); op.drop_table("users")

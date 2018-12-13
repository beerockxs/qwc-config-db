"""Insert viewer resource type

Revision ID: 875aa9290232
Revises: f2681d70c266
Create Date: 2018-12-13 16:01:28.360306

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '875aa9290232'
down_revision = 'f2681d70c266'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        INSERT INTO qwc_config.resource_types (name, description, list_order)
          VALUES (
            'viewer', 'Viewer',
            (SELECT MAX(list_order) + 1 FROM qwc_config.resource_types)
          );
    """)

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DELETE FROM qwc_config.resource_types WHERE name = 'viewer';
    """)

    conn = op.get_bind()
    conn.execute(sql)

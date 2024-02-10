"""
This module contains a Caribou migration.

Migration Name: create_db 
Migration Version: 20240210084203
"""

def upgrade(connection):
    # connection is a plain old sqlite3 database connection
    sql = """create table sticker_set (user_id, sticker_set_name) """
    connection.execute(sql)

def downgrade(connection):
    connection.execute('drop table sticker_set')
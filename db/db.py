import sqlite3

"""_instructions_
    This database has differnet parts

    1.) sys_command -> commands for internal files e.g (opening files, opening .exe)
    2.) web_command -> commands for website 
    3.) ...
"""

con = sqlite3.connect("./db/ivy.db")
cursor = con.cursor()

### SYS COMMAND DATABASE

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)


def sys_add_on_db(app_name, absolute_path):
    query = f"INSERT INTO sys_command VALUES (null, '{app_name}', '{absolute_path}')"
    cursor.execute(query)
    con.commit()


def sys_delete_previous():
    query = "DELETE FROM sys_command WHERE rowid = (SELECT MAX(rowid) FROM sys_command)"
    cursor.execute(query)
    con.commit()


# script here


### WEB COMMAND DATABASE

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)


def web_add_on_db(app_name, absolute_path):
    query = f"INSERT INTO web_command VALUES (null, '{app_name}', '{absolute_path}')"
    cursor.execute(query)
    con.commit()


def web_delete_previous():
    query = "DELETE FROM web_command WHERE rowid = (SELECT MAX(rowid) FROM web_command)"
    cursor.execute(query)
    con.commit()


# script here

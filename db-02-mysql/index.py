import mysql.connector
from mysql.connector import Error

def create_connection(host_name, db_name, db_login, db_password):
    conn = None
    try:
        conn = mysql.connector.connect(
            host=host_name,
            database=db_name,
            user=db_login,
            passwd=db_password,
            buffered=True
        )
        print("CONNECTION Success")
    except Error as e:
        print(f"{e}: while connecting to database")

    return conn

def execute_query(conn, query):
    cur = conn.cursor()
    try:
        cur.execute(query)
        connection.commit()
        print("QUERY Success")
    except Error as e:
        print(f"{e}: while executing the query")
    
    return cur

def execute_query_with_params(conn, query, params):
    cur = conn.cursor()
    try:
        cur.execute(query, params)
        connection.commit()
        print("QUERY WITH PARAMS Success")
    except Error as e:
        print(f"{e}: while executing parametrized query")
    
    return cur

connection = create_connection("localhost", "test", "root", "12345")

sql = "INSERT INTO users(login) VALUES ('dog')"
cursor = execute_query(connection, sql)

inserted_id = cursor.lastrowid

sql = "SELECT * FROM users"
cursor = execute_query(connection, sql)
users = cursor.fetchall() # returns array of tuples

for user in users:
    print(user)

sql = "UPDATE users SET login = 'manatee' WHERE id = %s"
execute_query_with_params(connection, sql, (inserted_id,))

sql = "SELECT * FROM users"
cursor = execute_query(connection, sql)
users = cursor.fetchall()

for user in users:
    print(user)

sql = "DELETE FROM users WHERE id = %s"
execute_query_with_params(connection, sql, (inserted_id,))

sql = "SELECT * FROM users"
cursor = execute_query(connection, sql)
users = cursor.fetchall()

for user in users:
    print(user)

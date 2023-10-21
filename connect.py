import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                  password="admin",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="users")
    cursor = connection.cursor()

    postgres_insert_query = """ INSERT INTO accounts(id, username) 
    VALUES (%s,%s)"""
    record_to_insert = [(1, 'admin'),
                        (2, 'user')]
    for i in record_to_insert:
        cursor.execute(postgres_insert_query, i)

        connection.commit()
        count = cursor.rowcount
    print(count, "Record inserted successfully \
    into accounts table")

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into publisher table", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
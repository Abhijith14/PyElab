import psycopg2



mydb2 = psycopg2.connect(
        host="HOST",
        database="DATABASE",
        user="USER",
        password="PASSWORD"
)

mycursor2 = mydb2.cursor()


def create_table_elabdata():
    create_table_query = '''CREATE TABLE status
                      (ID INTEGER PRIMARY KEY,
                      DATE_STAT VARCHAR(3000)    NOT NULL,
                      NAME VARCHAR(3000)    NOT NULL); '''

    mycursor2.execute(create_table_query)

    mydb2.commit()

def display_values_elabdata():
    sql = "SELECT * FROM status ORDER BY id ASC"
    print(sql)
    mycursor2.execute(sql)
    out = mycursor2.fetchall()
    for row in out:
        print(row)

def delete_all_elabdata():
    sql = "DELETE FROM status;"
    mycursor2.execute(sql)
    mydb2.commit()
    print("DELETED ALL DATA !!!")


def drop_table_elabdata():
    sql = "DROP TABLE status;"
    mycursor2.execute(sql)
    mydb2.commit()
    print("DROPPED TABLE !!!")


# drop_table_elabdata()
# delete_all_elabdata()
display_values_elabdata()
# create_table_elabdata()

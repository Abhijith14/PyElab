import psycopg2
import pymysql

mydb = psycopg2.connect(
    host="HOST",
        database="DATABASE",
        user="USER",
        password="PASSWORD"
)

mycursor = mydb.cursor()

mydb2 = pymysql.connect(host="localhost", user="root", passwd="", database="python")

mycursor2 = mydb2.cursor()


def create_table_elabdata():
    create_table_query = '''CREATE TABLE elabdata
                      (id SERIAL PRIMARY KEY,
                      SESSION VARCHAR(3000)    NOT NULL,
                      QUESTION_NO VARCHAR(3000)    NOT NULL,
                      QUESTION_NAME VARCHAR(3000)    NOT NULL,
                      QUESTION_DESC VARCHAR(3000)    NOT NULL,
                      CODE VARCHAR(5000)    NOT NULL); '''

    mycursor.execute(create_table_query)

    mydb.commit()


def display_values_elabdata():
    sql = "SELECT * FROM elabdata ORDER BY id ASC"
    print(sql)
    mycursor.execute(sql)
    out = mycursor.fetchall()
    for row in out:
        print(row)


def autoinsert_elabdata():
    sql = "SELECT * FROM elabdata"
    mycursor2.execute(sql)
    out = mycursor2.fetchall()
    print(str(len(out)) + " Questions in total")
    for row in out:
        # print(row[5])
        # print()
        Code = str(row[5]).replace('"', '\\"')
        Code = Code.replace("'", "“")

        QName = str(row[3].replace('"', '\\"'))
        QName = QName.replace("'", "“")

        QDesc = str(row[4].replace('"', '\\"'))
        QDesc = QDesc.replace("'", "“")

        print("Inserting ID : #" + str(row[0]))
        # print()
        # print(Code)
        sql2 = "INSERT INTO elabdata(id, SESSION, QUESTION_NO, QUESTION_NAME, QUESTION_DESC, CODE) VALUES  (" + str(row[0]) + ", '''" + str(row[1]) + "''', '''" + str(row[2]) + "''', '''" + str(QName) + "''', '''" + str(QDesc) + "''', "
        sql2 = sql2 + "'''" + str(Code) + "''');"
        # print("“")
        # print(sql2)
        mycursor.execute(sql2)
        mydb.commit()


def delete_all_elabdata():
    sql = "DELETE FROM elabdata;"
    mycursor.execute(sql)
    mydb.commit()
    print("DELETED ALL DATA !!!")

def drop_table_elabdata():
    sql = "DROP TABLE elabdata;"
    mycursor.execute(sql)
    mydb.commit()
    print("DROPPED TABLE !!!")

# create_table_elabdata()
display_values_elabdata()
# drop_table_elabdata()

# delete_all_elabdata()
# autoinsert_elabdata()

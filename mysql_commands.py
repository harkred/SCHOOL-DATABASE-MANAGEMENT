import mysql.connector as sql

HOST = 'localhost'
USER = 'root'
PASSWD = 'harkeerat2003'


def execute_cmd(cmd, values=None, database=None):
    mydb = sql.connect(host=HOST, user=USER, passwd=PASSWD, database=database)
    curse = mydb.cursor()
    curse.execute(cmd, values)
    mydb.commit()
    mydb.close()
    try:
        result = curse.fetchall()
        return result
    except Exception as e: pass
import sqlite3
#connect Database
def connect_DB(dbfile):
    con = sqlite3.connect(dbfile)
    cur = con.cursor()
    return con, cur

def Creat_TableSV(cur):
    strSQL = """
        CREATE TABLE if not exists SV
        (
            ID text PRIMARY KEY,
            PASSWORD text
        )"""
    str
    success_flag = True
    try :
        cur.execute(strSQL)
    except:
        success_flag = False
    if success_flag == True :
        print("Creat Ok")
    else:
        print("Creat Fail: ")

def Insert_SV(cur,con,id,passWorld):
    success_flag=True
    try:
        cur.execute("""INSERT OR IGNORE INTO SV
                VALUES(?,?)""",(id,passWorld) )
    except:
        success_flag=False
    if success_flag == True:
        return True
        con.commit()
    else:
        return False

def Select_SV(cur):
    result = cur.execute("SELECT ID FROM SV").fetchall()
    return result

def Update_User(cur,con,id,newPassWorld):
    success_flag = True
    try:
        st1="UPDATE OR IGNORE SV SET "
        st2= "PASSWORD" + " = ?"
        st3="WHERE ID = ?"
        st = st1 + st2 + st3
        cur.execute(st,(newPassWorld,id))
    except:
        success_flag= False
    con.commit()
    if success_flag == True:
      return True
    else :
      return False

def Checkpassworld(cur,id,pas):
    try:
        pas_old=cur.execute('SELECT PASSWORD FROM SV WHERE ID = ?;',(id,))
        pas_old=pas_old.fetchone()
        pas_old=pas_old[0]
    except:
        return False  
    if(pas_old==pas):
        return True
    else:
        return False

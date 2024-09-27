import sqlite3
import pandas as pd


def db_query_database(str_path, str_sql):
    conn = None
    try:
        conn = sqlite3.connect(str_path)
        df = pd.read_sql(str_sql, conn)
        return {"status": "OK", "df": df}    

    except sqlite3.Error as e:
        return {"status": "ERRO", "msg": str(e)}
       
    finally:
        if conn:
            conn.close()
            

def db_updata_database(str_path, str_sql, dados):
    conn = None
    try:
        conn = sqlite3.connect(str_path)
        cursor = conn.cursor()
        cursor.execute(str_sql, dados)
        conn.commit()
        return {"status": "OK"}
    
    except sqlite3.Error as e:
        return {"status": "ERRO", "msg": str(e)}
        
    finally:
        if conn:
            conn.close()
            
def db_insert_database(str_path, tab, dados, columns):
    conn = None
    try:
        conn = sqlite3.connect(str_path)
        df = pd.DataFrame(dados, columns=columns)
        df.to_sql(tab, conn, if_exists="append", index=False)
        
        return {"status": "OK"}
    
    except sqlite3.Error as e:
        return {"status": "ERRO", "msg": str(e)}
        
    finally:
        if conn:
            conn.close()          



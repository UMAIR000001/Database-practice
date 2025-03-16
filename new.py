import psycopg2
conn_detail={
    "user":"postgres",
     "host":"localhost",
      "password":"umair1234A@",
       "database":"school",
     "port":"5432"
}

try:
    conn=psycopg2.connect(conn_detail)
    print("Successfully connected ...")
    cursor=conn.cursor()
    query="select *from class"
    cursor.execute(query)
    result=cursor.fetchall()
    print(result)
except Exception as e:
    print("error",e)

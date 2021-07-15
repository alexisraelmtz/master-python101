import psycopg2
import psycopg2.extras


DB_HOST = "localhost"  # "127.0.0.1"
DB_NAME = "sample01_april_db"
DB_USER = "postgres"
DB_PASS = "132525"
DB_PORT = "5432"

conn = psycopg2.connect(
    dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT
)
# postgresql+psycopg2://user:password@host:port/dbname[?key=value&key=value...]

with conn:
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        # cur.execute("SELECT * FROM student WHERE id = %s;", (1,))
        # cur.execute("INSERT INTO student (name) VALUES(%s)", ("Erick",))
        cur.execute("SELECT * FROM student;")
        print(cur.fetchall())

        # print(cur.fetchone()['name'])


# c = conn.cursor()


# c.execute(
#     """CREATE TABLE employees (
#     first TEXT,
#     last TEXT,
#     pay INTEGER
#     )"""
# )


######


# cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# cur.execute("CREATE TABLE student (id SERIAL PRIMARY KEY, name VARCHAR);")

# cur.execute("INSERT INTO student (name) VALUES(%s)", ("Cristina",))

# cur.execute("SELECT * FROM student;")

# print(cur.fetchall())

######

# conn.commit()

# cur.close()

# conn.close()

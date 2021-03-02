import sqlite3


# conn = sqlite3.connect(":memory:")
conn = sqlite3.connect("store_inventory.db")

c = conn.cursor()

# c.execute(
#     """CREATE TABLE employees (
#     first TEXT,
#     last TEXT,
#     pay INTEGER
#     )"""
# )

# c.execute("INSERT INTO employees VALUES ('SHADDAI', 'MARTINEZ',9050)")
# c.execute("DELETE FROM employees")
c.execute("SELECT * FROM employees WHERE last='MARTINEZ'")
print(c.fetchall())


conn.commit()
conn.close()
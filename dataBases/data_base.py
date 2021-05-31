from client import Developers
import sqlite3


# conn = sqlite3.connect(":memory:")
conn = sqlite3.connect(
    r"/mnt/c/Users/7K/Documents/Python/master-python101/ecommerce/store_inventory.db"
)
c = conn.cursor()


# c.execute(
#     """CREATE TABLE employees (
#     first TEXT,
#     last TEXT,
#     pay INTEGER
#     )"""
# )


def insert_emp(emp):
    with conn:
        c.execute(
            "INSERT INTO employees VALUES (:first, :last, :pay)",
            {"first": emp.first, "last": emp.last, "pay": emp.pay},
        )


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {"last": lastname})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute(
            """UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
            {"first": emp.first, "last": emp.last, "pay": pay},
        )


def remove_emp(emp):
    with conn:
        c.execute(
            "DELETE from employees WHERE first = :first AND last = :last",
            {"first": emp.first, "last": emp.last},
        )


def all():
    c.execute("SELECT * FROM employees")
    return c.fetchall()


dev_1 = Developers("JOHN", "DOE", 85000)
dev_2 = Developers("JANE", "DOE", 95200)
dev_3 = Developers("KEVIN", "DOE", 35500)

print(dev_1.first)
print(dev_2.last)
print(dev_2.pay)

# insert_emp(dev_1)
# insert_emp(dev_2)
# insert_emp(dev_3)

# c.execute("INSERT INTO employees VALUES (?,?,?)", (dev_1.first, dev_1.last, dev_1.pay))
# # c.execute("DELETE FROM employees")
# conn.commit()


# c.execute(
#     "INSERT INTO employees VALUES (:first,:last,:pay)",
#     {"first": dev_2.first, "last": dev_2.last, "pay": dev_2.pay},
# )

# # c.execute("DELETE FROM employees")
# conn.commit()

# c.execute("DELETE FROM employees WHERE last=:last", {"last": "DOE"})
# print(c.fetchall())

# conn.commit()
print(all())
conn.close()
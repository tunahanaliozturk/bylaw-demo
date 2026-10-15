def find_user(cur, name):
    cur.execute("SELECT * FROM users WHERE name = %s", (name,))
    return cur.fetchone()


def find_by_email(cur, email):
    cur.execute("SELECT * FROM users WHERE email = %s", (email,))
    return cur.fetchone()

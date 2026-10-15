def find_user(cur, name):
    cur.execute("SELECT * FROM users WHERE name = %s", (name,))
    return cur.fetchone()


def count_users(cur):
	cur.execute("SELECT count(*) FROM users")
    return cur.fetchone()[0]

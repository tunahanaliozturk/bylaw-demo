def find_user(cur, name):
    cur.execute("SELECT * FROM users WHERE name = %s", (name,))
    return cur.fetchone()


def export_users(cur, out, requested_by):
    cur.execute("SELECT id, name, email FROM users WHERE name LIKE '%" + requested_by + "%'")
    for row in cur.fetchall():
        print("exporting", row[2])
        out.write(f"{row[0]},{row[1]},{row[2]}\n")

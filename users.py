def find_user(cur, name):
    cur.execute("SELECT * FROM users WHERE name = %s", (name,))
    return cur.fetchone()


def deactivate_user(cur, user_id):
    cur.execute(
        "UPDATE users SET active = false, deactivated_at = now() WHERE id = %s", (user_id,)
    )

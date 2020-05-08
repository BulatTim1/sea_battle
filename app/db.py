import sqlite3


def insert(username, email, password, token):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users(username, email, password, battles, wins, token) VALUES ('"
        + username + "','" + email + "','" + password + "','0','0', '" + token + "')")
    conn.commit()
    conn.close()


# def update_token(username, token):
#     conn = sqlite3.connect("app.db")
#     cursor = conn.cursor()
#     cursor.execute(
#         "INSERT INTO users(username, email, password, battles, wins) VALUES ('"
#         + username + "','" + email + "','" + password + "','0','0', '" + token + "')")
#     conn.commit()
#     conn.close()


def fetch():
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("select * from users")
    l = cursor.fetchall()
    conn.close()
    return l


def delete(username):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("delete from users where username like '" + username + "'")
    conn.commit()

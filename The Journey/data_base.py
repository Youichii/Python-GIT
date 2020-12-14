import sqlite3


def save_to_db(player_id, score):
    conn = sqlite3.connect("db_test.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS ALL_SCORES
                                (Score integer, 
                                Pseudo varchar(100))""")

    sql = "INSERT INTO ALL_SCORES (Score, Pseudo) VALUES (:score,:id)"
    c.execute(sql, {'score': score, 'id': player_id})
    conn.commit()

    sql = "SELECT * FROM ALL_SCORES"
    c.execute(sql)

    rows = c.fetchall()

    for row in rows:
        print(row)

    conn.close()

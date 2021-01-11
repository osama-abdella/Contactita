import sqlite3

with sqlite3.connect("Quiz.db") as db:
    curser = db.cursor()

curser.execute('''
CREATE TABLE IF NOT EXISTS user(
userID INTEGER PRIMARY KEY,
username VARCHAR(20) NOT NULL,
firstname VARCHAR(20) NOT NULL,
surname VARCHAR(20) NOT NULL,
password VARCHAR(20) NOT NULL);
''')

curser.execute('''
INSERT INTO user(username,firstname,surname,password)
VALUES("Osama","Allianz","Abdella","thegunner")
''')
db.commit()

curser.execute("SELECT * FROM user")
print(curser.fetchall())



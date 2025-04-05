import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="moviegeek"
)

cursor = conn.cursor()

def insert_userid(userid,tbname):
    sql = "INSERT INTO user_movie_interactions(user_id) VALUES (%s)"
    cursor.execute(sql)

# cursor.execute("""
#     CREATE TABLE user_movie_interactions (
#     interaction_id INT AUTO_INCREMENT PRIMARY KEY,
#     user_id INT,
#     movie_id INT,
#     rating INT, 
#     watched BOOLEAN DEFAULT FALSE,  
#     timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (user_id) REFERENCES collector_log(user_id),
#     FOREIGN KEY (movie_id) REFERENCES moviegeeks_movie(movie_id)
#     );
# """)

print("Table 'users' created successfully!")



# Đóng kết nối
cursor.close()
conn.close()
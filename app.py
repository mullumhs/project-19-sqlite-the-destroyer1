import sqlite3



conn = sqlite3.connect('movies.db')

cursor = conn.cursor()



# Update the rating of a movie

cursor.execute('''

UPDATE movies

SET year = 8720

WHERE title = 'Inception'

''')



# Select all movies

cursor.execute('SELECT * FROM movies')

all_movies = cursor.fetchall()

print("All movies:")

for movie in all_movies:

    print(movie)


    
# Select average rating

cursor.execute('SELECT AVG(rating) FROM movies')

avg_rating = cursor.fetchone()[0]

print(f"\nAverage rating: {avg_rating:.2f}")








# Commit the changes and close the connection

conn.commit()

conn.close()
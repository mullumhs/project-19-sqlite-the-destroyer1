# HTML Basics Project

Teacher: David Steedman

This repository contains two HTML tasks for the MHS Software Engineering class. This project focuses on creating basic HTML pages, introducing students to fundamental HTML concepts and structure. Students will learn about HTML tags, semantic elements, tables, and forms.

## Task 1: Basic HTML Page

- File: `task1.html`
- Description: Create a basic HTML page that includes a main heading, a picture with a subheading, and a list of links. This task covers:
  - Basic HTML structure (`<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`)
  - Headings (`<h1>` to `<h6>`)
  - Images (`<img>`)
  - Lists (`<ul>`, `<ol>`, `<li>`)
  - Links (`<a>`)

## Task 2: Contact Form

- File: `task2.html`
- Description: Create a more complex HTML page with a team profile table and a contact form. This task covers:
  - Semantic HTML elements (`<header>`, `<nav>`, `<section>`, `<footer>`)
  - Tables (`<table>`, `<thead>`, `<tbody>`, `<tr>`, `<th>`, `<td>`)
  - Forms (`<form>`, `<input>`, `<textarea>`, `<button>`)
  - Radio buttons and labels

## How to Submit Your Work

1. Accept the assignment and clone this repository to your local machine.
2. Create your HTML files (`task1.html` and `task2.html`) in the root directory of the repository.
3. Commit your changes with meaningful commit messages.
4. Push your changes to your GitHub repository.

## Resources

- [MDN Web Docs - HTML Basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics)
- [W3Schools HTML Tutorial](https://www.w3schools.com/html/)
- [HTML Validator](https://validator.w3.org/)

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

cursor.execute('SELECT \* FROM movies')

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

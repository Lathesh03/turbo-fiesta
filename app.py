"""Simple Flask app for storing and displaying messages in MySQL.

This module provides a minimal two-tier Flask application that stores
user-submitted messages in a MySQL database and renders them on the
frontend. Configuration is read from environment variables so the app
can be run locally or inside a container with different settings.
"""

import os
from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL


# Create the Flask application instance
app = Flask(__name__)


# ------------------
# MySQL configuration
# ------------------
# Read database connection settings from environment variables so the
# same code works in development and in containerized deployments.
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'default_user')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'default_password')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'default_db')


# Initialize the MySQL helper from flask_mysqldb. This wraps the
# connection object and exposes it via `mysql.connection`.
mysql = MySQL(app)


def init_db():
    """Create the `messages` table if it doesn't already exist.

    This function uses the Flask application context to access the
    MySQL connection and executes a simple CREATE TABLE statement.
    It is safe to call multiple times because the SQL uses
    `IF NOT EXISTS`.
    """
    with app.app_context():
        cur = mysql.connection.cursor()
        # Create a simple messages table with an auto-incrementing id
        cur.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INT AUTO_INCREMENT PRIMARY KEY,
            message TEXT
        );
        ''')
        # Commit the DDL change and close the cursor
        mysql.connection.commit()
        cur.close()


@app.route('/')
def hello():
    """Render the main page with all stored messages.

    Opens a cursor, selects all messages, closes the cursor, and
    passes the results to the `index.html` template as `messages`.
    """
    cur = mysql.connection.cursor()
    # Fetch all messages; `fetchall()` returns a list of tuples
    cur.execute('SELECT message FROM messages')
    messages = cur.fetchall()
    cur.close()
    # Render the template and provide the messages for display
    return render_template('index.html', messages=messages)


@app.route('/submit', methods=['POST'])
def submit():
    """Handle new message submissions from the frontend.

    Expects a form field named `new_message`. Inserts the message into
    the database and returns a JSON response containing the submitted
    text. Uses parameterized queries to avoid SQL injection.
    """
    # Get the submitted message from the form data
    new_message = request.form.get('new_message')
    cur = mysql.connection.cursor()
    # Parameterized insert; pass values as a sequence
    cur.execute('INSERT INTO messages (message) VALUES (%s)', [new_message])
    mysql.connection.commit()
    cur.close()
    # Return a simple JSON acknowledgment
    return jsonify({'message': new_message})


if __name__ == '__main__':
    # Ensure the database table exists before starting the app
    init_db()
    # Start the development server (bind to all interfaces)
    app.run(host='0.0.0.0', port=5000, debug=True)

#!/usr/bin/python3

"""
    Flask Web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/airbnb-onepage/')
def hello ():
    """Prints Hello HBNB! when (/) is called"""
    return 'Hello HBNB!'


if (__name__) == "__main__":
    """Main function getting called"""
    app.run(host='0.0.0.0', port=5000)

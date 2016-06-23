# -*- coding: utf-8 -*-
"""
`main` is the top level module for your Flask application.
"""
import jinja2
import os
from flask import Flask, render_template, request, make_response, redirect, url_for
from datetime import datetime, timedelta
app = Flask(__name__)
# Import custom libraries
from util.security import *
from models.models import URLMap

# Template Directories
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

"""
Home Controller
"""
# Home Controller
@app.route('/')
def home():
    """Return the main page where a URL can be created"""
    # Display homepage
    if request.method == 'GET':
        return render_template('home.html', page_title="ephemerURL")
    # Create a new URLMap
    else:
        pass


"""
Redirect Controller
"""
# Profile Controller
@app.route('/<shortcode>')
def timeline(id=None):
    """Redirect user to mapped URL"""
    if shortcode:
        url_map = URLMap.get_url_by_shortcode(shortcode)
        # If the shortcode is valid
        if url_map:
            if url_map.is_still_valid():
                # Decrement the counter
                url_map.counter -= 1
                url_map.put()
                return redirect(url_map.url)
            else:
                url_map.key.delete()
        # Redirect to home if not redirected to the URLMap url
        error = "URL shortcode is not valid."
        return render_template('home.html', page_title="ephemerURL", error=error)

"""
API
"""
# Application Health Controller
@app.route('/health')
def health():
    """Return OK if the app is working"""
    return "OK"

"""
Error Handlers
"""
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404

@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500

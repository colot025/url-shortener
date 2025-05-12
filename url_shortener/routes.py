import validators
from flask import Blueprint, render_template, request, redirect, flash

from .extensions import db
from .models import Link

from .auth import require_auth

shortener = Blueprint('shortener', __name__)

@shortener.route('/<short_url>')
def redirect_to_url(short_url):
    link = Link.query.filter_by(short_url=short_url).first_or_404()
    if not link:
        flash("Invalid or expired URL.", "danger")
        return redirect('/')
    if link.is_expired():
        flash("The URL has expired.", "danger")
        return redirect('/')
    link.views = link.views + 1
    db.session.commit()
    return redirect(link.original_url)

@shortener.route('/create_link', methods=['POST'])
def create_link():
       
    original_url = request.form['original_url']
    custom_id = request.form['custom_id']
 
    if not original_url:
        flash("Original URL cannot be empty.", "danger")
        return redirect('/')
    if not validators.url(original_url):
        flash("Invalid URL", "danger")
        return redirect('/')

    if custom_id:
        if Link.query.filter_by(short_url=custom_id).first():
            flash("Custom ID is already in use. Please choose another.", "danger")
            return redirect('/')
        short_url = custom_id
    else:
        short_url = None 

    link = Link(original_url=original_url, short_url=short_url)

    db.session.add(link)
    db.session.commit()

    return render_template('link_success.html',
    new_url=link.short_url, original_url=link.original_url)

@shortener.route('/regenerate', methods=['POST'])
def regenerate_url():
    original_url = request.form.get('original_url')

    if not original_url:
        flash("Original URL cannot be empty.", "danger")
        return redirect('/')

    # Check if the URL exists in the database
    link = Link.query.filter_by(original_url=original_url).first()

    if not link:
        return page_not_found(404)

    # Regenerate the short URL
    link.short_url = link.generate_short_link()
    db.session.commit()

    # Render the template with the regenerated link
    return render_template('link_success.html', original_url=original_url, new_url=link.short_url)

@shortener.route('/delete/<int:link_id>', methods=['POST'])
def delete_link(link_id):
    link = db.session.get(Link, link_id)  
    if link:
        db.session.delete(link)
        db.session.commit()
        flash("Short URL successfully removed.", "success")
    else:
        flash("Short URL not found.", "danger")
    
    return redirect('/analytics')

@shortener.route('/')
def index():
    return render_template('index.html')

@shortener.route('/analytics')
#@require_auth
def analytics():
    links = Link.query.all()

    return render_template('analytics.html', links=links)

@shortener.errorhandler(404)
def page_not_found(e):
    return '<h1>Page Not Found 404</h1>', 404
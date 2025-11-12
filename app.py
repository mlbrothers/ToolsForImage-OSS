# Author: Siddharth1India
import os
import io
import time
import json
import uuid
import queue
import threading
from collections import deque
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageFilter
from io import BytesIO

from flask import (
    Flask, abort, g, jsonify, redirect, render_template, request,
    send_file, send_from_directory, url_for, Response
)
from jinja2 import TemplateNotFound

from all_blog_data import blogs_list


app = Flask(__name__)

# At the top of your file, add:
supported_languages = ['en', 'hi', 'fr', 'zh', 'es']  # Add more as needed

@app.before_request
def before_request():
    # Exclude static files from language handling
    if request.path.startswith('/static/'):
        return  # Skip setting language for static file requests

    # Extract language from URL if present
    parts = request.path.split('/')
    if len(parts) > 1 and parts[1] in supported_languages:
        g.lang = parts[1]
    else:
        g.lang = 'en'  # Default to English

from werkzeug.exceptions import NotFound

@app.route('/<lang>/<path:subpath>')
def localized_route(lang, subpath):
    if lang not in supported_languages:
        # If language is not supported, redirect to English version
        return redirect(f'/en/{subpath}')
    
    # Set the language for this request
    g.lang = lang
    
    # Create a MapAdapter bound to the current host
    url_adapter = app.url_map.bind(request.host)
    
    try:
        # Try to match the subpath to a route
        endpoint, arguments = url_adapter.match('/' + subpath)
        return app.view_functions[endpoint](**arguments)
    except NotFound:
        # If no matching route found, try to render a template
        template_path = f'{lang}/{subpath}.html'
        if os.path.exists(os.path.join(app.template_folder, template_path)):
            return render_template(template_path)
        elif os.path.exists(os.path.join(app.template_folder, f'en/{subpath}.html')):
            return render_template(f'en/{subpath}.html')
        else:
            abort(404)

@app.route('/')
@app.route('/<lang>/')
def index(lang='en'):
    if lang not in supported_languages:
        return redirect('/en/')
    return render_template(f'{lang}/index.html')

@app.route('/image-compression')
@app.route('/<lang>/image-compression')
def image_compression(lang='en'):
    if lang not in supported_languages:
        return redirect('/en/image-compression')
    return render_template(f'{lang}/compress_en.html')

@app.route('/image-rotate')
@app.route('/<lang>/image-rotate')
def image_rotate(lang='en'):
    if lang not in supported_languages:
        return redirect('/en/image-rotate')
    return render_template(f'{lang}/rotate_en.html')

@app.route('/image-crop')
@app.route('/<lang>/image-crop')
def image_crop(lang='en'):
    if lang not in supported_languages:
        return redirect('/en/image-crop')
    return render_template(f'{lang}/crop_en.html')

@app.route('/image-resize')
@app.route('/<lang>/image-resize')
def image_resize(lang='en'):
    if lang not in supported_languages:
        return redirect('/en/image-resize')
    return render_template(f'{lang}/resize_en.html')

@app.route('/image-effects')
@app.route('/<lang>/image-effects')
def image_effects(lang='en'):
    if lang not in supported_languages:
        return redirect('/en/image-effects')
    return render_template(f'{lang}/image_effects_en.html')

@app.route('/convert-image-format')
@app.route('/<lang>/convert-image-format')
def convert_image_format(lang='en'):
    if lang not in supported_languages:
        return redirect('/en/convert-image-format')
    return render_template(f'{lang}/convert_en.html')

@app.route('/convert/<from_format>-to-<to_format>')
@app.route('/<lang>/convert/<from_format>-to-<to_format>')
def convert_image_format_route(lang='en', from_format='', to_format=''):
    if lang not in supported_languages:
        return redirect(f'/en/convert/{from_format}-to-{to_format}')
    
    supported_formats = ['png', 'jpg', 'jpeg', 'bmp', 'tiff', 'webp', 'ico']
    
    # Normalize formats
    from_format = from_format.lower()
    to_format = to_format.lower()
    
    # Validate formats
    if from_format not in supported_formats or to_format not in supported_formats:
        return render_template(f'{lang}/error.html', error="Unsupported image format"), 400
    
    # Prevent unnecessary conversions
    if from_format == to_format:
        return render_template(f'{lang}/error.html', error="Source and target formats are the same"), 400
    
    template_name = f'{from_format}-to-{to_format}.html'
    
    # Check if a specific template exists, otherwise use a generic template
    if os.path.exists(os.path.join(app.template_folder, f'{lang}/{template_name}')):
        return render_template(f'{lang}/{template_name}')
    else:
        return render_template(f'{lang}/generic_convert.html', from_format=from_format, to_format=to_format)

@app.route('/image-watermarking')
@app.route('/<lang>/image-watermarking')
def image_watermarking(lang='en'):
    if lang not in supported_languages:
        return redirect('/en/image-watermarking')
    return render_template(f'{lang}/watermark_en.html')

@app.route('/blur-face')
@app.route('/<lang>/blur-face')
def image_blur(lang='en'):
    if lang not in supported_languages:
        return redirect('/en/blur-face')
    return render_template(f'{lang}/blur_en.html')

@app.route('/remove-background')
@app.route('/<lang>/remove-background')
def remove_background_page(lang='en'):
    if lang not in supported_languages:
        return redirect('/en/remove-background')
    return render_template(f'{lang}/remove-background.html')


# Consolidate static page routes
@app.route('/about')
@app.route('/<lang>/about')
def about(lang='en'):
    if lang not in supported_languages:
        return redirect('/en/about')
    return render_template(f'{lang}/about.html')

@app.route('/contact-us')
@app.route('/<lang>/contact-us')
def contact_us(lang='en'):
    if lang not in supported_languages:
        return redirect('/en/contact-us')
    return render_template(f'{lang}/contact_us.html')

@app.route('/help')
@app.route('/<lang>/help')
def help(lang='en'):
    if lang not in supported_languages:
        return redirect('/en/help')
    return render_template(f'{lang}/help.html')

@app.route('/faq')
@app.route('/<lang>/faq')
def faq(lang='en'):
    if lang not in supported_languages:
        return redirect('/en/faq')
    return render_template(f'{lang}/faq.html')

@app.route('/media')
@app.route('/<lang>/media')
def media(lang='en'):
    if lang not in supported_languages:
        return redirect('/en/media')
    return render_template(f'{lang}/media.html')

@app.route('/legal')
@app.route('/<lang>/legal')
def legal(lang='en'):
    if lang not in supported_languages:
        return redirect('/en/legal')
    return render_template(f'{lang}/legal.html')

@app.route('/blogs')
@app.route('/<lang>/blogs')
def blogs(lang='en'):
    if lang not in supported_languages:
        return redirect('/en/blogs')

    # Get the blogs for the selected language
    blog_data = blogs_list.get(lang, blogs_list['en'])
    return render_template(f'{lang}/blogs.html', blogs=blog_data, lang=lang)

@app.route('/blogs/<blog_slug>')
@app.route('/<lang>/blogs/<blog_slug>')
def blog_post(blog_slug, lang='en'):
    if lang not in supported_languages:
        return redirect(url_for('blog_post', blog_slug=blog_slug, lang='en'))
    
    try:
        return render_template(f'{lang}/blogs/{blog_slug}.html')
    except TemplateNotFound:
        return redirect(url_for('blogs', lang=lang))

@app.route('/our-story')
@app.route('/<lang>/our-story')
def our_story(lang='en'):
    if lang not in supported_languages:
        return redirect('/en/our-story')
    return render_template(f'{lang}/our_story.html')

@app.route('/team')
@app.route('/<lang>/team')
def team(lang='en'):
    if lang not in supported_languages:
        return redirect('/en/team')
    return render_template(f'{lang}/team.html')

@app.route('/features')
@app.route('/<lang>/features')
def features(lang='en'):
    if lang not in supported_languages:
        return redirect('/en/features')
    return render_template(f'{lang}/features.html')

@app.route('/pricing')
@app.route('/<lang>/pricing')
def pricing(lang='en'):
    if lang not in supported_languages:
        return redirect('/en/pricing')
    return render_template(f'{lang}/pricing.html')

@app.route('/languages')
@app.route('/<lang>/languages')
def languages(lang='en'):
    if lang not in supported_languages:
        return redirect('/en/languages')
    return render_template(f'{lang}/languages.html')

@app.route('/tools')
@app.route('/<lang>/tools')
def tools(lang='en'):
    if lang not in supported_languages:
        return redirect('/en/tools')
    return render_template(f'{lang}/tools.html')

@app.route('/privacy_policy')
@app.route('/<lang>/privacy_policy')
def privacy_policy(lang='en'):
    if lang not in supported_languages:
        return redirect('/en/privacy_policy')
    return render_template(f'{lang}/privacy_policy.html')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('static', 'sitemap.xml')

@app.route('/robots.txt')
def robots():
    return send_from_directory('static', 'robots.txt')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('en/error.html', error="404 - Page Not Found"), 404

@app.route('/svgs-and-icons')
def svg_and_icon():
    svg_folder = os.path.join('static', 'svgicons')
    svg_categories = {}
    print(f'hello:{svg_folder}')
    
    # Iterate through subdirectories in svgicons
    for category in os.listdir(svg_folder):
        category_path = os.path.join(svg_folder, category)
        
        if os.path.isdir(category_path):
            # Find SVG files in the category subdirectory
            svg_files = [f for f in os.listdir(category_path) if f.endswith('.svg')]
            
            # Create names by removing .svg extension and replacing underscores
            svg_names = [os.path.splitext(f)[0] for f in svg_files]
            
            # Store category information
            svg_categories[category] = list(zip(svg_files, svg_names))
    
    return render_template('en/svgs-and-icons.html', 
                           svg_categories=svg_categories)

@app.route('/api/get-svgs')
def get_svgs():
    category = request.args.get('category', '')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 24))
    search_term = request.args.get('search', '').lower()

    svg_base_folder = os.path.join('static', 'svgicons')
    
    # If no category selected, use all categories
    if not category:
        svg_files = []
        for subdir in os.listdir(svg_base_folder):
            subdir_path = os.path.join(svg_base_folder, subdir)
            if os.path.isdir(subdir_path):
                category_files = [
                    (subdir, f) for f in os.listdir(subdir_path) 
                    if f.endswith('.svg') and 
                    (not search_term or search_term in f.lower())
                ]
                svg_files.extend(category_files)
    else:
        # If a specific category is selected
        svg_folder = os.path.join(svg_base_folder, category)
        svg_files = [
            (category, f) for f in os.listdir(svg_folder) 
            if f.endswith('.svg') and 
            (not search_term or search_term in f.lower())
        ]

    # Pagination
    start = (page - 1) * per_page
    end = start + per_page
    paginated_files = svg_files[start:end]

    # Prepare response
    svgs_data = []
    for cat, svg in paginated_files:
        svgs_data.append({
            'name': os.path.splitext(svg)[0],
            'filename': svg,
            'category': cat  # Add category to the response
        })

    return jsonify({
        'svgs': svgs_data,
        'has_more': end < len(svg_files)
    })

@app.route('/svgs-and-icons/<string:svg_name>.html')
def svg_detail(svg_name):
    # Remove .html extension if present
    svg_name = svg_name.replace('.html', '')
    
    # Find the SVG in all categories
    svg_base_folder = os.path.join('static', 'svgicons')
    svg_info = None
    
    # Search through all categories to find the SVG
    for category in os.listdir(svg_base_folder):
        category_path = os.path.join(svg_base_folder, category)
        if os.path.isdir(category_path):
            for svg_file in os.listdir(category_path):
                if svg_file.startswith(svg_name + '.'):
                    svg_info = {
                        'name': svg_name,
                        'filename': svg_file,
                        'category': category,
                        'path': f'/static/svgicons/{category}/{svg_file}'
                    }
                    break
    
    if svg_info is None:
        return abort(404)
        
    return render_template('en/svg-detail.html', svg=svg_info)
    
@app.route('/ads.txt')
def ads_txt():
    return send_from_directory('.', 'ads.txt', mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
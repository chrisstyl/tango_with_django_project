import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    python_pages = [
        {'title': 'Official Python Tutorial', 'url': 'http://docs.python.org/3/tutorial/', 'views': 150},
        {'title': 'How to Think like a Computer Scientist', 'url': 'http://www.greenteapress.com/thinkpython/', 'views': 23},
        {'title': 'Learn Python in 10 Minutes', 'url': 'http://www.korokithakis.net/tutorials/python/', 'views':3} ]

    django_pages = [
        {'title': 'Official Django Tutorial', 'url': 'http://docs.djangoproject.com/en/2.1/intro/tutorial01/', 'views': 70},
        {'title': 'Django Rocks', 'url': 'http://www.djangorocks.com/', 'views': 80},
        {'title': 'How to Tango with Django', 'url': 'http://www.tangowithdjango.com/', 'views': 14} ]

    other_pages = [
        {'title':'Bottle', 'url': 'http://bottlepy.org/docs/dev/', 'views': 6},
        {'title':'Flask', 'url': 'http://flask.pocoo.org', 'views': 66} ]

    cats = {'Python': {'pages': python_pages, 'views': 127, 'likes': 63},
            'Django': {'pages': django_pages, 'views': 63, 'likes': 31},
            'Other Frameworks': {'pages': other_pages, 'views': 31, 'likes': 15} }
    
    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

#Execution begins here
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
            

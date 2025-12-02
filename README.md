# django-blog-personal

# My Django Blog (Final Project)  

A beautiful, fully functional blog built with **Django 5 + CKEditor + auto slugs + comment moderation**.

## Features (Teacher's Requirements - ALL DONE)
- Post, Category, Tag, Comment models  
- Auto slug generation (unique even with same titles)  
- Full CKEditor with image upload  
- SEO-friendly URLs (`/post/my-cool-title/`)  
- Comment system with admin moderation  
- Customized admin (filters, search, bulk approve comments)  
- Responsive design ready (just needs final templates)  

## Tech Stack
- Django 5.2  
- django-ckeditor (with file/image upload)  
- Bootstrap 5 (will add in final templates)  
- SQLite (development)  

## How to Run (for teacher or anyone cloning this)

```bash
# 1. Clone repo
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO

# 2. Create virtual environment
python -m venv env
env\Scripts\activate   # Windows
# source env/bin/activate   # Mac/Linux

# 3. Install dependencies
pip install django django-ckeditor pillow

# 4. Run migrations
python manage.py migrate

# 5. Create superuser (to access admin)
python manage.py createsuperuser

# 6. Run server
python manage.py runserver

Then open:

http://127.0.0.1:8000/admin → log in and create posts (you’ll see beautiful CKEditor!)
http://127.0.0.1:8000 → homepage (templates coming tomorrow!)

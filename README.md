# Kasipodaq Clone - Django Website

A functional Django clone of the kasipodaq.kz website (Federation of Trade Unions of the Republic of Kazakhstan) with Supabase PostgreSQL backend, admin panel for news management, and responsive design.

## Features

✅ **Django 4.2+** backend with Python 3.10+  
✅ **Supabase PostgreSQL** database integration  
✅ **News Management System** with admin CRUD operations  
✅ **Rich Text Editor** (CKEditor) for article content  
✅ **Image Upload** functionality for news articles  
✅ **Responsive Design** with Tailwind CSS  
✅ **Blue/White/Yellow** color scheme matching kasipodaq.kz  
✅ **Public Access** - no login required for browsing  
✅ **Secure Admin Panel** for content management  

## Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Supabase account (free tier available at https://supabase.com)
- Git (optional, for version control)

## Project Structure

```
Website/
├── kasipodaq_project/       # Main Django project
│   ├── __init__.py
│   ├── settings.py          # Project settings & Supabase config
│   ├── urls.py              # Main URL routing
│   ├── wsgi.py
│   └── asgi.py
├── news/                    # News application
│   ├── migrations/          # Database migrations (auto-generated)
│   ├── __init__.py
│   ├── admin.py             # Admin panel configuration
│   ├── apps.py
│   ├── models.py            # NewsArticle model
│   ├── urls.py              # News app URLs
│   └── views.py             # View functions
├── templates/               # HTML templates
│   ├── base.html            # Base template with nav & footer
│   └── news/
│       ├── index.html       # Homepage with news grid
│       └── detail.html      # News detail page
├── static/                  # Static files (CSS, JS, images)
├── media/                   # User uploaded files
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
├── .gitignore
└── README.md                # This file
```

## Installation & Setup

### Step 1: Clone or Download the Project

If using Git:
```bash
cd C:\Users\User\Desktop
git clone <your-repo-url> Website
cd Website
```

Or simply navigate to the project directory:
```bash
cd C:\Users\User\Desktop\Website
```

### Step 2: Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` appear in your terminal prompt.

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Django 4.2+
- psycopg2-binary (PostgreSQL driver)
- Pillow (Image processing)
- django-ckeditor (Rich text editor)
- python-dotenv (Environment variables)

### Step 4: Configure Supabase Database

#### 4.1 Create Supabase Project

1. Go to https://supabase.com and sign up/login
2. Click "New Project"
3. Fill in project details:
   - **Name**: kasipodaq-clone (or your choice)
   - **Database Password**: Create a strong password (save this!)
   - **Region**: Choose closest to you
4. Wait for project setup (1-2 minutes)

#### 4.2 Get Database Credentials

1. In Supabase dashboard, go to **Settings** → **Database**
2. Scroll to **Connection Info** section
3. Note down:
   - **Host**: `db.xxxxxxxxxxxxx.supabase.co`
   - **Database name**: `postgres`
   - **Port**: `5432`
   - **User**: `postgres`
   - **Password**: Your database password from step 4.1

#### 4.3 Update Django Settings

Edit `kasipodaq_project/settings.py` (around line 70):

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'YOUR_SUPABASE_PASSWORD_HERE',  # ← Change this
        'HOST': 'db.xxxxxxxxxxxxx.supabase.co',      # ← Change this
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
}
```

**Alternative: Use SQLite for Local Development**

If you want to test locally without Supabase first, you can use SQLite instead:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### Step 5: Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

This creates all necessary database tables.

### Step 6: Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

You'll be prompted to enter:
- **Username**: admin (or your choice)
- **Email**: your-email@example.com
- **Password**: Create a strong password
- **Password (again)**: Confirm password

### Step 7: Create Static/Media Directories

The directories should already exist, but if not:

**Windows:**
```bash
mkdir static media
```

**macOS/Linux:**
```bash
mkdir -p static media
```

### Step 8: Start Development Server

```bash
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
```

## Usage Guide

### Accessing the Website

**Homepage:**  
http://127.0.0.1:8000/

This displays:
- Hero section with call-to-action
- Statistics section
- Activities/Services grid
- Latest news articles
- Join CTA section

**Admin Panel:**  
http://127.0.0.1:8000/admin/

Login with the superuser credentials created in Step 6.

### Managing News Articles

#### Creating News

1. Go to admin panel: http://127.0.0.1:8000/admin/
2. Click **News** → **News articles** → **Add News Article**
3. Fill in:
   - **Title**: Article headline
   - **Slug**: Auto-generated from title (or customize)
   - **Content**: Article body with rich text formatting
   - **Image**: Upload featured image (optional)
4. Click **Save**

The article will immediately appear on the homepage.

#### Editing News

1. In admin panel, go to **News** → **News articles**
2. Click on the article you want to edit
3. Make changes
4. Click **Save**

#### Deleting News

1. In admin panel, go to **News** → **News articles**
2. Select article(s) with checkboxes
3. Select "Delete selected news articles" from dropdown
4. Click **Go** → Confirm deletion

### Viewing News

**Homepage News Grid:**  
http://127.0.0.1:8000/

Shows latest 12 articles with:
- Thumbnail image
- Title
- Short excerpt
- Publication date
- "Read more" link

**Individual Article:**  
http://127.0.0.1:8000/news/article-slug/

Shows:
- Full article title
- Featured image
- Complete content with rich text formatting
- Publication and update dates
- Back to news button

## Customization

### Changing Colors

Edit `templates/base.html` (line 50):

```javascript
colors: {
    'kasip-blue': '#1E3A8A',        // Main blue
    'kasip-light-blue': '#3B82F6',  // Light blue
    'kasip-yellow': '#FCD34D',      // Yellow accent
}
```

### Modifying Content

- **Header/Footer**: Edit `templates/base.html`
- **Homepage**: Edit `templates/news/index.html`
- **News Detail**: Edit `templates/news/detail.html`

### Adding New Pages

1. Create view function in `news/views.py`
2. Add URL pattern in `news/urls.py`
3. Create template in `templates/news/`

## Deployment (Production)

For production deployment:

1. **Security Settings** (`settings.py`):
   ```python
   DEBUG = False
   SECRET_KEY = 'generate-new-secret-key'
   ALLOWED_HOSTS = ['yourdomain.com']
   ```

2. **Static Files**:
   ```bash
   python manage.py collectstatic
   ```

3. **Use Environment Variables** for sensitive data:
   ```python
   import os
   SECRET_KEY = os.getenv('SECRET_KEY')
   ```

4. **Deploy to platforms like**:
   - Railway.app
   - Heroku
   - DigitalOcean
   - AWS
   - PythonAnywhere

## Troubleshooting

### Database Connection Error

**Error:** `could not connect to server`

**Solution:**
- Verify Supabase credentials in `settings.py`
- Check internet connection
- Ensure Supabase project is running
- Verify SSL mode is set to 'require'

### Static Files Not Loading

**Solution:**
```bash
python manage.py collectstatic --clear
```

### Image Upload Not Working

**Solution:**
- Check `MEDIA_ROOT` and `MEDIA_URL` in `settings.py`
- Ensure `media/` directory exists
- Verify Pillow is installed: `pip install Pillow`

### Port Already in Use

**Error:** `That port is already in use`

**Solution:**
```bash
python manage.py runserver 8001
```

## Tech Stack

- **Backend**: Django 4.2+
- **Database**: PostgreSQL (Supabase)
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **Rich Text Editor**: CKEditor
- **Image Processing**: Pillow
- **Font**: Google Fonts (Roboto)

## License

This project is created for educational purposes as a demonstration of Django web development.

## Support

For issues or questions:
1. Check Django documentation: https://docs.djangoproject.com/
2. Check Supabase documentation: https://supabase.com/docs
3. Review this README carefully

## Credits

Design inspired by kasipodaq.kz (Federation of Trade Unions of the Republic of Kazakhstan).

---

**Built with ❤️ using Django and Supabase**

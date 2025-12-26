# Django Kasipodaq Clone - Implementation Plan

A functional Django website that replicates the design and core functionality of kasipodaq.kz (Federation of Trade Unions of the Republic of Kazakhstan). The project will include a news management system with admin CRUD operations, Supabase PostgreSQL integration, and a responsive frontend.

## User Review Required

> [!IMPORTANT]
> **Supabase Configuration**: You will need to provide your Supabase database credentials (host, database name, user, password, port) to connect the Django application. The implementation will include a template configuration that you'll need to update with your actual credentials.

> [!IMPORTANT]
> **Static Files in Production**: This implementation focuses on development setup. For production deployment, you'll need to configure static file hosting (e.g., using WhiteNoise or a CDN) and set `DEBUG=False` in settings.

> [!NOTE]
> **Simplified Clone**: This implementation will create a simplified version focusing on the core features (news system, admin panel, responsive design). The full kasipodaq.kz site includes many additional sections (about, activities, legal documents, etc.) that can be added later following the same pattern.

## Proposed Changes

### Django Core

#### [NEW] [manage.py](file:///c:/Users/User/Desktop/Website/manage.py)
Standard Django management script for running commands.

#### [NEW] [requirements.txt](file:///c:/Users/User/Desktop/Website/requirements.txt)
Project dependencies including Django, Pillow for image handling, psycopg2 for PostgreSQL, and django-ckeditor for rich text editing.

#### [NEW] [.gitignore](file:///c:/Users/User/Desktop/Website/.gitignore)
Git ignore file to exclude virtual environment, database files, and sensitive data.

---

### Project Configuration

#### [NEW] [kasipodaq_project/\_\_init\_\_.py](file:///c:/Users/User/Desktop/Website/kasipodaq_project/__init__.py)
Empty init file to make the directory a Python package.

#### [NEW] [kasipodaq_project/settings.py](file:///c:/Users/User/Desktop/Website/kasipodaq_project/settings.py)
Main Django settings with:
- Supabase PostgreSQL database configuration template
- Installed apps including CKEditor for rich text
- Static and media files configuration
- Tailwind CSS integration via CDN
- Security settings

#### [NEW] [kasipodaq_project/urls.py](file:///c:/Users/User/Desktop/Website/kasipodaq_project/urls.py)
Main URL configuration routing to news app and admin panel.

#### [NEW] [kasipodaq_project/wsgi.py](file:///c:/Users/User/Desktop/Website/kasipodaq_project/wsgi.py)
WSGI configuration for deployment.

#### [NEW] [kasipodaq_project/asgi.py](file:///c:/Users/User/Desktop/Website/kasipodaq_project/asgi.py)
ASGI configuration for async support.

---

### News Application

#### [NEW] [news/\_\_init\_\_.py](file:///c:/Users/User/Desktop/Website/news/__init__.py)
Empty init file for news app.

#### [NEW] [news/models.py](file:///c:/Users/User/Desktop/Website/news/models.py)
NewsArticle model with:
- `title`: CharField for article title
- `slug`: SlugField for URL-friendly identifier (auto-generated from title)
- `content`: RichTextField for article content with CKEditor
- `image`: ImageField for article image upload
- `publication_date`: DateTimeField with auto_now_add
- `updated_at`: DateTimeField with auto_now
- Meta ordering by publication_date (newest first)

#### [NEW] [news/admin.py](file:///c:/Users/User/Desktop/Website/news/admin.py)
Admin panel configuration with:
- Custom list display showing title, publication date, and slug
- Search functionality by title and content
- Date filters for publication date
- Prepopulated slug field from title
- Rich text editor integration

#### [NEW] [news/views.py](file:///c:/Users/User/Desktop/Website/news/views.py)
Views for:
- Homepage: displays latest news articles in grid layout
- News detail page: displays full article with image and content

#### [NEW] [news/urls.py](file:///c:/Users/User/Desktop/Website/news/urls.py)
URL patterns for news app routes.

#### [NEW] [news/apps.py](file:///c:/Users/User/Desktop/Website/news/apps.py)
News app configuration.

---

### Templates

#### [NEW] [templates/base.html](file:///c:/Users/User/Desktop/Website/templates/base.html)
Base template with:
- Tailwind CSS via CDN
- Navigation header with kasipodaq.kz style (blue navigation)
- Footer with contact information
- Responsive mobile menu
- Blue/white/yellow color scheme matching original site

#### [NEW] [templates/news/index.html](file:///c:/Users/User/Desktop/Website/templates/news/index.html)
Homepage template with:
- Hero section with call-to-action 
- News grid displaying articles with images
- Responsive card layout (3 columns desktop, 1 column mobile)
- "Join the Union" button matching original design

#### [NEW] [templates/news/detail.html](file:///c:/Users/User/Desktop/Website/templates/news/detail.html)
News detail page displaying:
- Article title
- Publication date
- Featured image
- Full article content (rich text)
- Back to homepage link

---

### Static Files Structure

#### [NEW] [static/.gitkeep](file:///c:/Users/User/Desktop/Website/static/.gitkeep)
Placeholder for static files directory.

#### [NEW] [media/.gitkeep](file:///c:/Users/User/Desktop/Website/media/.gitkeep)
Placeholder for media uploads directory.

---

### Documentation

#### [NEW] [README.md](file:///c:/Users/User/Desktop/Website/README.md)
Comprehensive setup guide including:
- Project overview and features
- Prerequisites (Python 3.10+, Supabase account)
- Virtual environment setup instructions
- Dependency installation
- Supabase configuration steps
- Database migration commands
- Superuser creation
- Development server startup
- Admin panel access instructions
- Project structure explanation

## Verification Plan

### Automated Tests
Currently no automated tests are included in this initial implementation. Tests can be added in future iterations.

### Manual Verification

1. **Database Connection**
   - Update `settings.py` with Supabase credentials
   - Run `python manage.py migrate` successfully
   - Verify tables are created in Supabase dashboard

2. **Admin Panel Access**
   - Create superuser: `python manage.py createsuperuser`
   - Navigate to `http://127.0.0.1:8000/admin/`
   - Login with superuser credentials
   - Verify admin dashboard loads

3. **News CRUD Operations**
   - In admin panel, create a new news article with title, content, and image
   - Verify slug is auto-generated
   - Edit the article and save changes
   - Delete a test article
   - Create at least 3 articles for homepage testing

4. **Homepage Display**
   - Navigate to `http://127.0.0.1:8000/`
   - Verify news articles display in grid layout
   - Check images load correctly
   - Verify responsive design by resizing browser window
   - Test mobile view (should show single column)

5. **News Detail Page**
   - Click on a news article from homepage
   - Verify detail page displays full content
   - Check rich text formatting renders correctly
   - Verify image displays
   - Test back button

6. **Design Verification**
   - Verify blue/white/yellow color scheme matches kasipodaq.kz
   - Check navigation header styling
   - Verify footer displays correctly
   - Test responsive breakpoints (mobile, tablet, desktop)

7. **Public Access**
   - Open homepage in incognito/private browsing
   - Verify news can be viewed without login
   - Confirm admin panel requires authentication

# Step-by-Step Guide: Transfer Django Project to Another PC

## Method 1: Flash Drive Transfer (Quick & Simple)

### On Current PC:

1. **Stop the Django server** (if running)
   - Press Ctrl+C in PowerShell

2. **Copy the project folder**
   - Copy the entire `Website` folder to your flash drive
   - **IMPORTANT**: You can delete the `venv` folder first to save space (it's large and not needed)
   - Keep `db.sqlite3` - this has your admin user and data

### On New PC:

1. **Install Python 3.10+**
   - Go to https://python.org/downloads
   - Download and install
   - ✅ CHECK "Add Python to PATH" during installation!

2. **Copy project from flash drive**
   - Copy `Website` folder to your Desktop (or wherever you want)

3. **Open PowerShell** in the Website folder:
   - Right-click the `Website` folder
   - Choose "Open in Terminal" or "Open PowerShell here"

4. **Set up the project**:
   ```powershell
   # Create virtual environment
   python -m venv venv
   
   # Activate it
   .\venv\Scripts\Activate.ps1
   
   # If you get execution policy error:
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Start the server
   python manage.py runserver
   ```

5. **Open browser**: http://127.0.0.1:8000/

---

## Method 2: Using GitHub (BEST PRACTICE - Recommended)

### Benefits:
✅ Work on multiple PCs easily
✅ Version control (track all changes)
✅ Backup in the cloud
✅ Collaborate with others
✅ Professional workflow

### Setup on Current PC:

1. **Create GitHub account** (free)
   - Go to https://github.com
   - Sign up

2. **Install Git**
   - Download from https://git-scm.com
   - Install with default settings

3. **Initialize Git in your project**:
   ```powershell
   cd C:\Users\User\Desktop\Website
   
   # Initialize git
   git init
   
   # Add all files (gitignore will exclude venv and cache)
   git add .
   
   # Commit
   git commit -m "Initial commit - Kasipodaq website"
   ```

4. **Create repository on GitHub**
   - Go to https://github.com/new
   - Name it "kasipodaq-website"
   - Click "Create repository"

5. **Push your code**:
   ```powershell
   # Link to GitHub (replace YOUR_USERNAME)
   git remote add origin https://github.com/YOUR_USERNAME/kasipodaq-website.git
   
   # Push code
   git push -u origin main
   ```

### On New PC:

1. **Install Python** (as above)

2. **Install Git** (as above)

3. **Clone the project**:
   ```powershell
   cd C:\Users\YourName\Desktop
   
   # Clone from GitHub (replace YOUR_USERNAME)
   git clone https://github.com/YOUR_USERNAME/kasipodaq-website.git
   
   cd kasipodaq-website
   ```

4. **Set up** (same as Method 1):
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   python manage.py runserver
   ```

### Update Changes:
When you make changes on one PC and want to sync to another:

**On PC where you made changes**:
```powershell
git add .
git commit -m "Added new features"
git push
```

**On other PC**:
```powershell
git pull
```

---

## Method 3: Compress to ZIP (Saves Space)

### On Current PC:
1. Right-click `Website` folder
2. Choose "Compress to ZIP file" or use 7-Zip/WinRAR
3. Copy ZIP to flash drive (much smaller!)

### On New PC:
1. Extract the ZIP
2. Follow Method 1 steps above

---

## ⚠️ IMPORTANT NOTES

### Don't Copy These Folders:
- ❌ `venv/` - Recreate this on each PC (it's PC-specific)
- ❌ `__pycache__/` - Auto-generated Python cache
- ❌ `staticfiles/` - Can be regenerated

### DO Copy These Files:
- ✅ All `.py` files (your code)
- ✅ `templates/` folder
- ✅ `static/` folder
- ✅ `media/` folder (if you have uploaded images)
- ✅ `db.sqlite3` (your database with admin user)
- ✅ `requirements.txt`
- ✅ `.gitignore`
- ✅ `README.md`

### Database Options:

**Option A: Keep your data**
- Copy `db.sqlite3` file
- Your admin user and news articles will be on the new PC

**Option B: Start fresh**
- Don't copy `db.sqlite3`
- On new PC, run:
  ```powershell
  python manage.py migrate
  python manage.py createsuperuser
  ```

---

## 🎯 My Recommendation

For your situation, I recommend:

1. **Short term** (just trying on another PC): Use Method 1 (Flash Drive)
2. **Long term** (serious development): Use Method 2 (GitHub)

GitHub is what professional developers use and it's free. It will make your life much easier!

---

## 🆘 Troubleshooting on New PC

**Problem**: `python` command not found
- **Solution**: Reinstall Python and check "Add to PATH"

**Problem**: Can't activate virtual environment
- **Solution**: Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

**Problem**: Missing modules after pip install
- **Solution**: Make sure virtual environment is activated (you should see `(venv)` in PowerShell)

**Problem**: Port 8000 already in use
- **Solution**: Use `python manage.py runserver 8001`

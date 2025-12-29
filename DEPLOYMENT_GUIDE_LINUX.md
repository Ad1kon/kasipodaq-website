# Linux Deployment Guide (Ubuntu 22.04/24.04)

This guide walks you through deploying your Django Kasipodaq website on a Linux server (VPS). This is the standard production setup used by professional developers.

**Stack:** Ubuntu + Gunicorn + Nginx

---

## 1. Initial Server Setup

Login to your server via SSH:
```bash
ssh root@YOUR_SERVER_IP
```

Update the system and install necessary packages:
```bash
sudo apt update
sudo apt upgrade -y
sudo apt install python3-pip python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl -y
```

---

## 2. Clone Your Project

Navigate to the web directory:
```bash
cd /var/www
```

Clone your repository (assuming you pushed it to GitHub as recommended in the Transfer Guide):
```bash
# Replace with your actual GitHub URL
git clone https://github.com/YOUR_USERNAME/kasipodaq-website.git
```

*Alternatively, you can use SFTP/FileZilla to upload your `Website` folder to `/var/www/kasipodaq-website`.*

---

## 3. Python Environment Setup

Go into the project folder:
```bash
cd /var/www/kasipodaq-website
```

Create and activate the virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
pip install gunicorn  # Required for production server
```

---

## 4. Configure Django for Production

Open your settings file:
```bash
nano kasipodaq_project/settings.py
```

Make these changes:
1.  **Debug**: Set `DEBUG = False`
2.  **Allowed Hosts**: Set `ALLOWED_HOSTS = ['yourdomain.com', 'YOUR_SERVER_IP']`
3.  **Static Root**: Ensure `STATIC_ROOT` is configured (it is in your file).

Save and exit (`Ctrl+X`, then `Y`, then `Enter`).

Prepare static files and database:
```bash
python manage.py collectstatic
python manage.py migrate
```

---

## 5. Setup Gunicorn (Application Server)

Create a systemd socket file:
```bash
sudo nano /etc/systemd/system/gunicorn.socket
```

Paste this content:
```ini
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```

Create a systemd service file:
```bash
sudo nano /etc/systemd/system/gunicorn.service
```

Paste this content (adjust paths if yours are different):
```ini
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/var/www/kasipodaq-website
ExecStart=/var/www/kasipodaq-website/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          kasipodaq_project.wsgi:application

[Install]
WantedBy=multi-user.target
```

Start Gunicorn:
```bash
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
```

Check status (it should be green/active):
```bash
sudo systemctl status gunicorn.socket
```

---

## 6. Setup Nginx (Web Server)

Create a configuration file for your site:
```bash
sudo nano /etc/nginx/sites-available/kasipodaq
```

Paste this content (replace `yourdomain.com` with your actual domain or IP):
```nginx
server {
    listen 80;
    server_name yourdomain.com YOUR_SERVER_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    # Serve static files directly
    location /static/ {
        root /var/www/kasipodaq-website;
    }

    # Serve media files directly
    location /media/ {
        root /var/www/kasipodaq-website;
    }

    # Pass everything else to Gunicorn
    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```

Enable the site:
```bash
sudo ln -s /etc/nginx/sites-available/kasipodaq /etc/nginx/sites-enabled
```

Test Nginx config:
```bash
sudo nginx -t
```
*(If successful, you will see "syntax is ok")*

Restart Nginx:
```bash
sudo systemctl restart nginx
```

---

## 7. Firewall & Security

Allow traffic on ports 80 (HTTP) and 22 (SSH):
```bash
sudo ufw allow 'Nginx Full'
sudo ufw allow OpenSSH
sudo ufw enable
```

---

## 8. Add HTTPS (Free SSL Certificate)

If you have a domain name, secure it with Certbot:

```bash
sudo apt install python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

Follow the prompts, and Certbot will automatically configure SSL for you!

---

## ✅ Deployment Complete!

Visit your domain or IP address in the browser. Your site should be live!

### Useful Commands for Maintenance

*   **Restart App**: `sudo systemctl restart gunicorn` (do this after code changes)
*   **Restart Web Server**: `sudo systemctl restart nginx`
*   **Check Logs**: `sudo journalctl -u gunicorn`

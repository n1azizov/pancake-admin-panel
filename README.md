
# Reusable Flask Authentication Template

This is a **generic, reusable template** for building:
- Login pages
- Admin panels
- Protected content pages
- JSON-based user storage
- Static HTML content routing
- Deployable on **PythonAnywhere**, **Render**, **Railway**, or locally

It is intentionally minimal so users can adapt it for:
- School projects
- Portfolio websites
- Small internal tools
- Classwork distribution portals
- Authentication demos

---

## 🚀 Features

- 🔐 Simple email/password authentication
- 🔧 Admin panel with login
- ➕ Add/delete users (JSON-based)
- 📁 Serve multiple protected HTML documents (`Page1.html`, `Page2.html`, ...)
- 📦 Very lightweight, vanilla HTML/CSS/JS
- 🌐 Flask backend (easy to extend)
- ⚙️ GitHub Actions ready

---

## 📁 Project Structure

```
project/
│── app.py
│── index.html
│── admin.html
│── users.json
│── pages/
│     ├── Page1.html
│     ├── Page2.html
│     └── ...
│── requirements.txt
│── README.md
│── .github/workflows/python-app.yml
```

---

## 🧪 Local Testing

Install dependencies:

```
pip install -r requirements.txt
```

Run the server:

```
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## ☁️ Deploy to PythonAnywhere

1. Open **PythonAnywhere Dashboard**
2. Create a folder and upload all project files
3. Create a Virtualenv:

```
python3.12 -m venv venv
source venv/bin/activate
pip install flask
```

4. In the **Web** tab:
   - Set working directory: `/home/yourusername/project`
   - Set WSGI file to import:

```
from app import app as application
```

5. Set virtualenv path:

```
/home/yourusername/project/venv
```

6. **Reload** the web app.

---

## 🤖 GitHub Actions (CI)

The template includes:

```
.github/workflows/python-app.yml
```

A simple workflow that:
- Installs dependencies  
- Runs syntax checks  
- Ensures project bootstraps correctly

---

## 🧩 Customize

You can:
- Replace login UI  
- Add CSS frameworks  
- Add a database instead of JSON  
- Build dashboards  
- Add file uploads  
- Add role-based access control  

This template is meant to be **fully extensible**.

Enjoy building! 🔥

---

## 🥞 Author & Maintainer

Made with ❤️ by **Nadir Azizov** — the guy who created the pancake-themed admin panel 🥞😄

- 📧 Email: nadir.azizov@example.com  
- 🐙 GitHub: github.com/n1azizov  
- 🎓 LinkedIn: linkedin.com/in/nadirazizov  

If you like this project, star ⭐ the repo!

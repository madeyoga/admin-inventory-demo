# 🛠️ Django Admin Customization Demo

This project showcases how to customize the Django Admin interface for better **user experience**, **performance**, and **internal tool usability**.

Whether you're building tools for a startup, internal dashboard for teams, or personal backend interfaces — Django Admin can be supercharged with the right tweaks.

---

## 🚀 Features

- ✅ Custom filters, search fields, and admin actions
- 🎨 Improved layout & navigation & theme using [Django Unfold](https://github.com/unfoldadmin/django-unfold)
- 📊 Dashboard with charts (e.g. Chart.js or Plotly integration)
- 🔐 Custom permissions and user access control
- 🐢 Performance optimization (N+1 queries fix with `select_related`, `prefetch_related`)
- 🛠️ Debugging with `django-debug-toolbar`
- 📁 Custom list displays, inlines, and form layouts

---

## 📸 Screenshots

<img width="1440" height="776" alt="Image" src="https://github.com/user-attachments/assets/a950fe15-5d69-4db5-881c-ee30d5f58453" />

<img width="1440" height="777" alt="Image" src="https://github.com/user-attachments/assets/977db1ac-805b-4ab7-8da7-7d243ba309da" />

---


## Setup

1. **Install uv**  
   https://docs.astral.sh/uv/getting-started/installation/
2. **Apply migrations**  
   ```sh
   uv run manage.py migrate
   ```
3. **Create superuser** (admin access)  
   ```sh
   uv run manage.py createsuperuser
   ```
4. **Run the development server**  
   ```sh
   uv run manage.py runserver
   ```
5. **Access the admin interface**  
   Navigate to `http://127.0.0.1:8000/admin` in your web browser.


## Usage

- Log in with the superuser account to access the admin interface.
- Manage categories, products, and stock movements using the custom views.
- Use the debug toolbar for SQL query and performance analysis.


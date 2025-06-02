# 🧑‍🎓 Student Portal

Welcome to my first Django project!  
This is a basic student portal where users can register, log in, and access content based on their role — student, instructor, or admin.

I built it from scratch to really *understand* the core parts of Django — not just copy and paste from tutorials.

---

## 🚀 What it Does

- Users can sign up and pick a role (student, instructor, admin).
- Everyone gets a connected profile behind the scenes (using Django signals — that was new for me!).
- The login system is fully functional, with sessions, redirects, and feedback messages.
- Bootstrap adds just enough style to make it clean without getting into frontend distractions.

It’s not meant to be flashy — it's focused, clear, and meant to show that I understand the **backend logic** of a real app.

---

## 🧠 Why I Built It

I didn’t want to just build another to-do list app.  
This project helped me dive into:

- Django forms and how they work behind the scenes
- Handling user roles the right way
- Working with `UserProfile` and `signals`
- Managing redirection and login state clearly

More importantly, it helped me learn **how Django wants you to think** — not just what buttons to push.

---

## 🛠 Tech Stack

- Python 3
- Django (vanilla — no REST yet)
- SQLite3 (for dev, no Postgres here)
- HTML templates + Bootstrap 5
- Classic MVC structure (not API yet — that's coming later)

---

## 🔧 How to Run It

```bash
git clone https://github.com/YOUR_USERNAME/student-portal.git
cd student-portal

# optional
python -m venv env
source env/bin/activate

# install dependencies
pip install -r requirements.txt

# setup database
py manage.py migrate

# run it
py manage.py runserver

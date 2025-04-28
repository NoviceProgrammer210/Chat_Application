

# 📚 Real-Time Chat Application

A real-time chat application built using **Django**, **Django Channels**, **Daphne**, **ASGI**, and **Websockets**, styled using **TailwindCSS CDN**.

---

## 🚀 Features

- Real-time messaging with Websockets
- User Authentication (Login, Signup, Logout)
- Create and Join Chat Rooms
- Responsive design with TailwindCSS (via CDN)
- ASGI-powered with Daphne

---

## 📂 Tech Stack

- **Backend:** Django, Django Channels, Daphne
- **Frontend:** TailwindCSS (via CDN)
- **Websockets:** ASGI Protocol

---

## 🛠️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/NoviceProgrammer210/Chat_Application.git
cd Chat

# 2. Create and activate a virtual environment
python -m venv env
source env/bin/activate    # For Linux/macOS
env\Scripts\activate       # For Windows

pip install django channels websocket

# 4. Run database migrations
python manage.py migrate

# 5. Run the Daphne server
daphne your_project_name.asgi:application
```


## 🌐 How It Works

- **Authentication:** Users must log in to access chat features.
- **Rooms:** Users can  chat With Other Users By Rooms.
- **Real-Time Chat:** Messages are sent instantly using Websockets through Django Channels and Daphne.

---








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

# 1. Create and activate a virtual environment
python -m venv env
source env/bin/activate    # For Linux/macOS
env\Scripts\activate       # For Windows

# 2. Clone the repository
git clone https://github.com/NoviceProgrammer210/Chat_Application.git



pip install django channels websocket

# 3. Run database migrations
python manage.py migrate

# 4. Run the Daphne server
daphne -b 127.0.0.1 -p 8000 Chat.asgi:application # To run the Chat Application 
```


## 🌐 How It Works

- **Authentication:** Users must log in to access chat features.
- **Rooms:** Users can  chat With Other Users By Rooms.
- **Real-Time Chat:** Messages are sent instantly using Websockets through Django Channels and Daphne.

---






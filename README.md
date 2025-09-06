# Chat-Application-project

# 🗨️ Chat Application Project

A **real-time chat application** built with **Django, Django Channels, Redis, WebSockets, PostgreSQL, HTML, CSS, and JavaScript**.  

This project demonstrates how to combine **modern web technologies** to build an interactive and scalable communication platform. Unlike traditional apps that reload for updates, this chat system uses **WebSockets** to provide **instant messaging** between users.  

Users can register, log in, create or join chat rooms, and communicate instantly. The backend handles **real-time connections** through Django Channels and Redis, while PostgreSQL stores user data, rooms, and chat history.  

---
## 🛠️ Tech Stack
**Frontend**
- HTML5  
- CSS3  
- JavaScript  

**Backend**
- Django  
- Django Channels (ASGI support for WebSockets)  

**Database**
- PostgreSQL  

**Messaging / Broker**
- Redis  

**Other Tools**
- Git & GitHub  
- Virtualenv (environment management)  

---

## 🚀 Features
- 🔑 User **registration & login, logout**
- 💬 Create and join multiple **chat rooms**
- ⚡ **Real-time messaging** with WebSockets
- 👥 Show **online users**
- 🗄️ **Persistent storage** of users, rooms, and chat history with PostgreSQL
- 📡 **Scalable backend** using Django Channels + Redis
- 🎨 Frontend built with **HTML, CSS, JS**

---
## 🏗 System Architecture

    User[User Browser] -->|HTTP/HTTPS| DjangoApp[Django App (ASGI)];
    DjangoApp -->|WebSocket| Channels[Django Channels];
    Channels --> Redis[Redis Server];
    DjangoApp --> DB[PostgreSQL Database];
    ---
## 🖼️ Screenshots
### Chat Room Login
![Chat Room](https://github.com/Jaimitha13/Chat-Application-project/blob/ef485777f9dc2589f8bb1d952548b342736424e5/Screenshot%202025-09-06%20134416.png?raw=true)

##  Chat Room Screenshot

![Chat app](https://github.com/Jaimitha13/Chat-Application-project/blob/834015dfe047b77ea4218509b4e14b7e1bc0bb74/Screenshot%202025-09-06%20134747.png?raw=true)

![Chat Room ](https://github.com/Jaimitha13/Chat-Application-project/blob/70b8da878c407b67c7693bf12c84a32b72af9fe4/Screenshot%202025-09-06%20134840.png?raw=true)


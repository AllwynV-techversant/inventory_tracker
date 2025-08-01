# Inventory Tracker – Setup Guide

Follow these steps to get the app running locally.

---

## 1. Clone the repository

```bash
git clone https://github.com/your-username/inventory_tracker.git
cd inventory_tracker
```

---

## 2. Build and run the app using Docker Compose

```bash
docker-compose up --build
```

This will:
- Start the MongoDB container
- Start the FastAPI backend at http://localhost:8000

---

## 3. To stop the app

```bash
docker-compose down
```

---

## 4. API Docs

- Swagger: http://localhost:8000/docs  


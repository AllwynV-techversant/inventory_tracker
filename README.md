# 🗃️ Inventory Tracker – Setup Guide

Follow these steps to get the app running locally.

---

## 1. Clone the repository

```bash
git clone https://github.com/your-username/inventory_tracker.git
cd inventory_tracker
```

---

## 2. Create the `.env` file

```bash
echo "MONGO_URI=mongodb://mongo:27017/inventory_db" > .env
```

---

## 3. Build and run the app using Docker Compose

```bash
docker-compose up --build
```

This will:
- Start the MongoDB container
- Start the FastAPI backend at http://localhost:8000

---

## 4. To stop the app

```bash
docker-compose down
```

---

## 5. API Docs

- Swagger: http://localhost:8000/docs  


# 🚚 Delivery Cost Calculator API

### 📌 Description
This Flask-based REST API calculates the minimum delivery cost from multiple warehouse centers to a customer based on the order details. It uses dynamic programming to find the optimal path considering weight and distance costs.

---

### 🔗 Live Demo
**POST Endpoint:** [`/calculate`](https://twf-assignment-3zcv.onrender.com/calculate)  
**Base URL:** `https://twf-assignment-3zcv.onrender.com/calculate`

---

### 📦 Request Format (JSON)
```json
{
  "A": 1,
  "B": 1,
  "C": 1
}

### 📦 Response Format (JSON)
```json
{
   "minimum_cost": 78
}

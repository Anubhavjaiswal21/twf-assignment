# 🚚 Delivery Cost Calculator API

### 📌 Description
This Flask-based REST API calculates the minimum delivery cost from multiple warehouse centers to a customer based on the order details. It uses dynamic programming to find the optimal path considering weight and distance costs.

---

### 🔗 Live Demo
**POST Endpoint:** [`/calculate`](https://delivery-cost-api.onrender.com/calculate)  
**Base URL:** `https://delivery-cost-api.onrender.com/calculate`

---

### 📦 Request Format (JSON)
```json
{
  "A": 1,
  "B": 2,
  "H": 1
}

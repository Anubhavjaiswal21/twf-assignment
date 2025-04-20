# from flask import Flask, request, jsonify
# from itertools import permutations

# app = Flask(__name__)

# product_data = {
#     "C1": {"A": 3, "B": 2, "C": 8},
#     "C2": {"D": 12, "E": 25, "F": 15},
#     "C3": {"G": 0.5, "H": 1, "I": 2}
# }

# distances = {
#     ("C1", "C2"): 4,
#     ("C2", "L1"): 2.5,
#     ("L1", "C1"): 3,
#     ("C2", "C3"): 3,
#     ("C3", "L1"): 2
# }

# @app.route("/")
# def home():
#     return "Welcome to the Delivery Cost API!"

# @app.route("/calculate", methods=["POST"])
# def calculate():
#     order = request.get_json()
#     order = {k.upper(): v for k, v in order.items() if v > 0}
#     required_centers = find_centers(order)

#     all_paths = []
#     for start in required_centers:
#         for perm in permutations(required_centers):
#             if perm[0] != start:
#                 continue
#             path = []
#             for center in perm:
#                 path += [center, "L1"]
#             all_paths.append(path)

#     min_cost = float('inf')
#     for path in all_paths:
#         carried = set()
#         weight = 0
#         total_cost = 0
#         for i in range(len(path) - 1):
#             curr = path[i]
#             if curr in product_data:
#                 for p in product_data[curr]:
#                     if p in order and p not in carried:
#                         weight += product_data[curr][p] * order[p]
#                         carried.add(p)
#             dist = distances.get((path[i], path[i+1])) or distances.get((path[i+1], path[i])) or 0
#             total_cost += calculate_cost(weight, dist)
#         min_cost = min(min_cost, total_cost)

#     return jsonify({"minimum_cost": round(min_cost)})

# def calculate_cost(weight, distance):
#     cost = 0
#     if weight <= 5:
#         cost = 10 * distance
#     else:
#         cost = 10 * distance
#         weight -= 5
#         chunks = int(weight // 5)
#         remainder = weight % 5
#         cost += chunks * 8 * distance
#         if remainder > 0:
#             cost += 8 * distance
#     return cost

# def get_distance(path):
#     total = 0
#     for i in range(len(path) - 1):
#         a, b = path[i], path[i + 1]
#         dist = distances.get((a, b)) or distances.get((b, a)) or 0
#         total += dist
#     return total

# def find_centers(order):
#     centers = set()
#     for p in order:
#         for c in product_data:
#             if p in product_data[c]:
#                 centers.add(c)
#     return list(centers)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)

from flask import Flask, request, jsonify
from itertools import permutations

app = Flask(__name__)

product_data = {
    "C1": {"A": 3, "B": 2, "C": 8},
    "C2": {"D": 12, "E": 25, "F": 15},
    "C3": {"G": 0.5, "H": 1, "I": 2}
}

distances = {
    ("C1", "C2"): 4,
    ("C2", "L1"): 2.5,
    ("L1", "C1"): 3,
    ("C2", "C3"): 3,
    ("C3", "L1"): 2
}

@app.route("/")
def home():
    return "Welcome to the Delivery Cost API!"

@app.route("/calculate", methods=["POST"])
def calculate():
    order = request.get_json()
    order = {k.upper(): v for k, v in order.items() if v > 0}
    required_centers = find_centers(order)

    all_paths = []
    for start in required_centers:
        for perm in permutations(required_centers):
            if perm[0] != start:
                continue
            path = []
            for center in perm:
                path += [center, "L1"]
            all_paths.append(path)

    min_cost = float('inf')
    for path in all_paths:
        carried = set()
        weight = 0
        total_cost = 0
        for i in range(len(path) - 1):
            curr = path[i]
            if curr in product_data:
                for p in product_data[curr]:
                    if p in order and p not in carried:
                        weight += product_data[curr][p] * order[p]
                        carried.add(p)
            dist = distances.get((path[i], path[i + 1])) or distances.get((path[i + 1], path[i])) or 0
            total_cost += calculate_cost(weight, dist)
            weight = 0  # Reset weight after each trip to L1
        min_cost = min(min_cost, total_cost)

    return jsonify({"minimum_cost": round(min_cost)})

def calculate_cost(weight, distance):
    cost = 10 * distance  # Base charge for each delivery trip
    weight -= 5
    if weight > 0:
        chunks = int(weight // 5)
        remainder = weight % 5
        cost += chunks * 8 * distance
        if remainder > 0:
            cost += 8 * distance
    return cost

def get_distance(path):
    total = 0
    for i in range(len(path) - 1):
        a, b = path[i], path[i + 1]
        dist = distances.get((a, b)) or distances.get((b, a)) or 0
        total += dist
    return total

def find_centers(order):
    centers = set()
    for p in order:
        for c in product_data:
            if p in product_data[c]:
                centers.add(c)
    return list(centers)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


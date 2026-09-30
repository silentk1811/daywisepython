from flask import Flask, jsonify, request
app = Flask(__name__)
books=[
    {"id": 1, "title": "Python Crash Course", "author": "Eric Matthes"},
    {"id": 2, "title": "Automate the Boring Stuff with Python ", "author": " Al Sweigar"},
    {"id": 3, "title": "Think Python ", "author": "Allen B. Downey"}
]

@app.route("/api/books", methods=["GET"])
def get_books():
    return jsonify(books), 200

@app.route("/api/books", methods=["POST"])
def add_book():
    data = request.get_json()
    new_book = {  "id": len(books) + 1, "title": data["title"],"author": data["author"],"price": data["price"]}
    books.append(new_book)
    return jsonify(new_book), 201

    
students=[
    {"id": 1, "name": "Kalyani", "marks": 75, "status": "Pass"},
    {"id": 2, "name": "Sejal", "marks": 35, "status": "Fail"},
    {"id": 3, "name": "Kartiki", "marks": 60, "status": "Pass"}
]

@app.route("/api/students", methods=["GET"])
def get_students():
    return jsonify(students), 200

@app.route("/api/students", methods=["POST"])
def add_student():
    data = request.get_json()
    if data["marks"] >= 40:
        status = "Pass"
    else:
        status = "Fail"
    new_student = {"id": len(students) + 1, "name": data["name"], "marks": data["marks"], "status": status}
    students.append(new_student)
    return jsonify(new_student), 201

employees=[
    {"id": 1, "name": "Employee 1", "department": "HR", "salary": 30000},
    {"id": 2, "name": "Employee 2", "department": "IT", "salary": 40000},
    {"id": 3, "name": "Employee 3", "department": "Finance", "salary": 35000}
]

@app.route("/api/employees", methods=["GET"])
def get_employees():
    return jsonify(employees), 200

@app.route("/api/employees", methods=["POST"])
def add_employee():
    data = request.get_json()
    new_employee = {"id": len(employees) + 1, "name": data["name"], "department": data["department"], "salary": data["salary"]}
    employees.append(new_employee)
    return jsonify(new_employee), 201

@app.route("/api/employees/<int:emp_id>", methods=["DELETE"])
def delete_employee(emp_id):
    for employee in employees:
        if employee["id"] == emp_id:
            employees.remove(employee)
            return jsonify({"message": "Employee deleted successfully"}), 200
    return jsonify({"message": "Employee not found"}), 404

cart=[]

@app.route("/api/cart", methods=["POST"])
def add_to_cart():
    data = request.get_json()
    if data["price"] <= 0:
        return jsonify({"message": "Invalid price"}), 400
    new_item = {"product_name": data["product_name"], "price": data["price"]}
    cart.append(new_item)
    return jsonify({"message": "Product added successfully", "data": new_item}), 201
if __name__ == "__main__":
    app.run(debug=True)
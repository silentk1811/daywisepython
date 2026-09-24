from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    app_name = "My First Flask App"
    age = 21
    current_year = datetime.now().year

    return render_template(
        "index.html",
        app_name=app_name,
        age=age,
        current_year=current_year
    )
    
@app.route("/score")
def score_card():
    student_name = "Kalyani"
    score = 85

    return render_template(
        "score.html",
        student_name=student_name,
        score=score
    )

@app.route("/product/<int:id>")
def product(id):
    return render_template("product.html", id=id)


@app.route("/greet/<username>")
def greet(username):
    return render_template("greet.html", username=username)


@app.route("/voter")
def voter():
    age = 19

    return render_template(
        "voter.html",
        age=age
    )
    
@app.route("/admin")
def admin():
    user = {
        "name": "admin",
        "role": "admin"
    }

    return render_template(
        "admin.html",
        user=user
    )
    
@app.route("/result")
def result():
    marks = 65

    return render_template(
        "result.html",
        marks=marks
    )
    
@app.route("/stock")
def stock():
    stock = 10

    return render_template(
        "stock.html",
        stock=stock
    )
    
@app.route("/number")
def number():
    num = 7

    return render_template(
        "number.html",
        num=num
    )
    
@app.route("/login")
def login():
    logged_in = True

    return render_template(
        "login.html",
        logged_in=logged_in
    )
    
@app.route("/fruits")
def fruits():
    fruits = ["Apple", "Banana", "Mango", "Orange"]

    return render_template(
        "fruits.html",
        fruits=fruits
    )
    
@app.route("/student")
def student():
    students = ["Kalyani", "Rahul", "Priya", "Amit"]

    return render_template(
        "student.html",
        students=students
    )
    
@app.route("/products")
def products():
    products = ["Laptop", "Mouse", "Keyboard", "Headphones"]

    return render_template(
        "products.html",
        products=products
    )
    
@app.route("/empty")
def empty():
    products = []

    return render_template(
        "empty.html",
        products=products
    )
    
@app.route("/numbered-fruits")
def numbered_fruits():
    fruit = ["Apple", "Banana", "Mango", "Orange"]

    return render_template(
        "fruit.html",
        fruit=fruit
    )
    
@app.route("/even")
def even():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    return render_template(
        "even.html",
        numbers=numbers
    )
    
@app.route("/profile")
def profile():
    user = {
        "name": "Kalyani",
        "age": 21,
        "city": "Pune"
    }

    return render_template(
        "profile.html",
        user=user
    )
    
@app.route("/grade")
def grade():
    student = {
        "name": "Kalyani",
        "python": 85,
        "java": 78,
        "web": 90
    }

    return render_template(
        "grade.html",
        student=student
    )
    
@app.route("/blog")
def blog():
    posts = ["My First Blog", "Learning Flask", "Learning Jinja2"]

    return render_template(
        "blog.html",
        posts=posts
    )
    
@app.route("/cart")
def cart():
    prices = [100, 200, 150]

    total = sum(prices)

    return render_template(
        "cart.html",
        prices=prices,
        total=total
    )
    
@app.route("/highscore")
def highscore():
    scores = [45, 78, 92, 65, 88]

    highest = max(scores)

    return render_template(
        "highscore.html",
        highest=highest
    )
    
@app.route("/directory")
def directory():
    folders = {
        "Frontend": ["HTML", "CSS", "JavaScript"],
        "Backend": ["Python", "Flask", "Django"]
    }

    return render_template(
        "directory.html",
        folders=folders
    )


if __name__ == "__main__":
    app.run(debug=True)
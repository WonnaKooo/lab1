from flask import jsonify, request
from Project import app

from Project.category import Category
from Project.customer import Customer


Categories = [
    {
        "id": 1,
        "name": "Food",
    },
]


@app.route("/categories")
def get_categories():
    return jsonify({"categories": Categories})


@app.route("/category", methods=['POST'])
def create_category():
    pass
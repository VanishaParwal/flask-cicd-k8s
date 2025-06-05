from flask import Blueprint, request, jsonify, current_app, render_template
from app.models.book import Book
from app.utils.validator import (
    validate_book,
    validate_book_update,
)

# 🔵 Create Blueprint
books_bp = Blueprint("books_bp", __name__)

@books_bp.route("/view")
def view_books():
    return render_template("books.html", books=current_app.books)

@books_bp.route("/", methods=["GET"])
def list_books():
    return jsonify([book.__dict__ for book in current_app.books]), 200

@books_bp.route("/", methods=["POST"])
def create_book():
    data = request.get_json()
    if not validate_book(data):
        return jsonify({"error": "Invalid input"}), 400

    new_id = len(current_app.books) + 1
    book = Book(id=new_id, title=data["title"], author=data["author"])
    current_app.books.append(book)
    return jsonify(book.__dict__), 201

@books_bp.route("/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.get_json()
    if not validate_book_update(data):
        return jsonify({"error": "Invalid update input"}), 400

    for book in current_app.books:
        if book.id == book_id:
            if "title" in data:
                book.title = data["title"]
            if "author" in data:
                book.author = data["author"]
            return jsonify(book.__dict__), 200

    return jsonify({"error": "Book not found"}), 404

@books_bp.route("/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    for book in current_app.books:
        if book.id == book_id:
            current_app.books.remove(book)
            return jsonify({"message": "Book deleted"}), 200

    return jsonify({"error": "Book not found"}), 404
@books_bp.route("/<int:book_id>", methods=["GET"])
def get_book(book_id):
    for book in current_app.books:
        if book.id == book_id:
            return jsonify(book.__dict__), 200

    return jsonify({"error": "Book not found"}), 404                
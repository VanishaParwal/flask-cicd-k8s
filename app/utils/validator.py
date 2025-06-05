def validate_book(data):
    """
    Validates input for creating a new book.
    Required fields: title (str), author (str)
    """
    return (
        isinstance(data, dict)
        and "title" in data
        and "author" in data
        and isinstance(data["title"], str)
        and isinstance(data["author"], str)
        and data["title"].strip() != ""
        and data["author"].strip() != ""
    )


def validate_book_update(data):
    """
    Validates input for updating a book.
    At least one of 'title' or 'author' must be present.
    Only those two fields allowed.
    """
    if not isinstance(data, dict):
        return False
    allowed_keys = {"title", "author"}
    return (
        any(k in data for k in allowed_keys)
        and set(data).issubset(allowed_keys)
        and all(isinstance(data[k], str) and data[k].strip() != "" for k in data)
    )


def validate_book_delete(data):
    """
    Validates input for deleting a book by ID.
    Only used if deletion expects JSON body.
    """
    return (
        isinstance(data, dict)
        and "id" in data
        and isinstance(data["id"], int)
        and data["id"] > 0
    )

# Personal Library Analyzer
# -------------------------
# A simple program that stores a small book collection and analyzes it.
#
# How it works:
#     1. Stores the books in a dictionary (title -> author, genre, year).
#     2. Displays all the books and looks up a specific one.
#     3. Collects the unique authors and genres, counts the books per author,
#        and groups the titles by author.
#     4. Searches for a given author and lists their books.
#     5. Finds the most prolific author and prints a final library report.
#
# Concepts practiced:
#     - Dictionaries with tuples as values
#     - Tuple unpacking
#     - Sets for unique values
#     - Counting and grouping with dictionaries
#     - For loops with .items()
#     - The max function with a key argument
#     - Conditional logic (if / else)
#     - String formatting with f-strings

# ==========================================
# 1. LIBRARY DATA
# ==========================================

my_books = {
    "Hamlet": ("William Shakespeare", "Tragedy", 1603),
    "The Martian Chronicles": ("Ray Bradbury", "Science fiction", 1950),
    "Fahrenheit 451": ("Ray Bradbury", "Dystopian", 1953),
}


# ==========================================
# 2. DISPLAY BOOK INFORMATION
# ==========================================

print("========== MY BOOKS ==========")

for title, (author, genre, year) in my_books.items():
    print(f"{title} | {author} | {genre} | {year}")


# ==========================================
# 3. ACCESS A SPECIFIC BOOK
# ==========================================

author, genre, year = my_books["Fahrenheit 451"]

print(f"\nFahrenheit 451 was written by {author} in {year}.")


# ==========================================
# 4. LIBRARY ANALYSIS
# ==========================================

unique_authors = set()
unique_genres = set()
author_counts = {}
books_by_author = {}

for title, (author, genre, year) in my_books.items():
    # Collect unique authors and genres
    unique_authors.add(author)
    unique_genres.add(genre)

    # Count books by author
    if author in author_counts:
        author_counts[author] += 1
    else:
        author_counts[author] = 1

    # Group book titles by author
    if author not in books_by_author:
        books_by_author[author] = []

    books_by_author[author].append(title)


# ==========================================
# 5. AUTHOR SEARCH
# ==========================================

search_author = "Ray Bradbury"

if search_author in unique_authors:
    print(f"\n{search_author} is one of my authors!")

    print(f"{search_author}'s books:")

    for book in books_by_author[search_author]:
        print(f"- {book}")


# ==========================================
# 6. MOST PROLIFIC AUTHOR
# ==========================================

most_prolific_author = max(author_counts, key=author_counts.get)
highest_count = author_counts[most_prolific_author]


# ==========================================
# 7. LIBRARY REPORT
# ==========================================

print("\n========== MY LIBRARY REPORT ==========")

print(f"Total books: {len(my_books)}")
print(f"Unique authors: {len(unique_authors)}")
print(f"Unique genres: {len(unique_genres)}")

print("\nBooks by author:")

for author, count in author_counts.items():
    print(f"- {author}: {count}")

print(f"\nMost prolific author: {most_prolific_author} ({highest_count} books)")

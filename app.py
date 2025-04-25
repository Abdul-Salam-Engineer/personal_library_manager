import streamlit as st
import json
import os

# File where books will be stored
LIBRARY_FILE = "library.json"

# Function to load books from the file
def load_books():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

# Function to save books to the file
def save_books(books):
    with open(LIBRARY_FILE, "w", encoding="utf-8") as file:
        json.dump(books, file, indent=4)

# Function to add a book
def add_book(title, author, year):
    books = load_books()
    books.append({"title": title, "author": author, "year": year})
    save_books(books)

# Function to remove a book
def remove_book(title):
    books = load_books()
    books = [book for book in books if book['title'].lower() != title.lower()]
    save_books(books)

# Function to search books
def search_books(keyword):
    books = load_books()
    return [book for book in books if keyword.lower() in book['title'].lower() or keyword.lower() in book['author'].lower()]

# Streamlit UI
st.title("Personal Library Manager.")

# Add new book section
st.header("Add a New Book")
title = st.text_input("Book Title")
author = st.text_input("Author Name")
year = st.text_input("Publication Year")

if st.button("Add Book"):
    if title and author and year:
        add_book(title, author, year)
        st.success(f"'{title}' Added Successfully!")
    else:
        st.error("Please Fill All Fields!")

# Search book section
st.header("Search For a Book")
search_term = st.text_input("Enter Book Title or Author to Search")
if st.button("Search"):
    results = search_books(search_term)
    if results:
        st.write("### Search Results:")
        for book in results:
            st.write(f"**{book['title']}** by *{book['author']}* ({book['year']})")
    else:
        st.warning("No Matching Books Found.")

# List all books section
st.header("All Books in Library")
books = load_books()
if books:
    for book in books:
        st.write(f"**{book['title']}** by *{book['author']}* ({book['year']})")
else:
    st.info("No books Found in the Library.")

# Remove book section
st.header("Remove a Book")
remove_title = st.text_input("Enter Book Title to Remove")
if st.button("Remove Book"):
    if remove_title:
        remove_book(remove_title)
        st.success(f"'{remove_title}' removed successfully!")
    else:
        st.error("Please Enter a Book Title!")

# Footer
st.markdown("<hr><p style='color: red'>Created by A.Salam</p>", unsafe_allow_html=True)
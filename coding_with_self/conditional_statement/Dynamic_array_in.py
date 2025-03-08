# Initialize the shelves and the array for queries
num_shelves = int(input())  # Number of shelves
num_requests = int(input())  # Number of requests

# Arrays for tracking books and pages
total_number_of_books = [0] * num_shelves  # Stores the number of books on each shelf
total_number_of_pages = [[] for _ in range(num_shelves)]  # 2D array, stores pages for each book per shelf

# Process each query
for _ in range(num_requests):
    query = list(map(int, input().split()))
    
    if query[0] == 1:  # Insert a book with 'y' pages on shelf 'x'
        if len(query) == 3:  # Ensure query has enough elements
            x, y = query[1], query[2]
            total_number_of_books[x] += 1  # Increase the number of books on shelf 'x'
            total_number_of_pages[x].append(y)  # Add 'y' pages to the shelf's book list
        else:
            print("Error: Invalid input for type 1 query. Expected format: 1 x y")
    
    elif query[0] == 2:  # Print the number of pages in book 'y' on shelf 'x'
        if len(query) == 3:  # Ensure query has enough elements
            x, y = query[1], query[2]
            print(total_number_of_pages[x][y])  # Access and print the number of pages for the book
        else:
            print("Error: Invalid input for type 2 query. Expected format: 2 x y")
    
    elif query[0] == 3:  # Print the number of books on shelf 'x'
        if len(query) == 2:  # Ensure query has enough elements
            x = query[1]
            print(total_number_of_books[x])  # Access and print the number of books on shelf 'x'
        else:
            print("Error: Invalid input for type 3 query. Expected format: 3 x")

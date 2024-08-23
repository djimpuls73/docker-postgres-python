import os
import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(
    host=os.environ.get("POSTGRES_HOST", "postgres"),
    database=os.environ.get("POSTGRES_DB", "your_lastname"),
    user=os.environ.get("POSTGRES_USER", "your_lastname"),
    password=os.environ.get("POSTGRES_PASSWORD", "your_lastname")
)

# Create a cursor
cur = conn.cursor()

# Execute a query to get the max and min age for names with length less than 6 characters
cur.execute("""
    SELECT
        MAX(age) AS max_age,
        MIN(age) AS min_age
    FROM test_table
    WHERE LENGTH(name) < 6;
""")

# Print the result
result = cur.fetchone()
print(f"Maximum age for names with length less than 6 characters: {result[0]}")
print(f"Minimum age for names with length less than 6 characters: {result[1]}")

# Close the connection
cur.close()
conn.close()

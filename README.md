
# FastAPI ETL Pipeline to PostgreSQL Data Warehouse

This project demonstrates a complete ETL (Extract, Transform, Load) pipeline that fetches data from a FastAPI-powered REST API and loads it into a PostgreSQL data warehouse.

## Technologies Used

- FastAPI – Python web framework to expose the API.
- PostgreSQL – Relational database for storing post data.
- Pandas – For data transformation and manipulation.
- SQLAlchemy – ORM and database engine integration.
- psycopg2 – PostgreSQL database adapter for Python.
- Python 3.10



## FastAPI Endpoints

Base URL: `http://localhost:8000`

| Method | Endpoint             | Description                   |
|--------|----------------------|-------------------------------|
| GET    | `/posts/`            | Retrieve all posts            |
| GET    | `/posts/{id}`        | Retrieve a single post by ID  |
| POST   | `/posts/`            | Create a new post             |
| PUT    | `/posts/{id}`        | Update an existing post       |
| DELETE | `/posts/{id}`        | Delete a post                 |


## API Testing with Postman

You can test the API using [Postman](https://www.postman.com/):

### Create Post

 URL: `http://localhost:8000/posts/


### Get All Posts

 URL: `http://localhost:8000/posts/

### Get a Post by ID

 URL: `http://localhost:8000/posts/1

### Update a Post

URL: `http://localhost:8000/posts/1

### Delete a Post

 URL: `http://localhost:8000/posts/1`

---

## ⚙️ Running the ETL Pipeline

This script extracts data from the FastAPI /posts endpoint and loads it into a PostgreSQL data warehouse.

### Step 1: Update your `fastapi_to_postgres.py`

Ensure this file includes the correct `API_URL`, `DB_URL`, and table name.

```python
API_URL = "http://localhost:8000/posts"
DB_URL = "postgresql://username:password@localhost:5432/warehouse_db"
TABLE_NAME = "posts"
```

### Step 2: Activate your Python environment

```bash
source venv/bin/activate
```

### Step 3: Run the ETL script

```bash
python etl/fastapi_to_postgres.py
```


## Example PostgreSQL Table Schema


```sql
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    published BOOLEAN DEFAULT TRUE
);
```

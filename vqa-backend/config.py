import os

# Database configuration for PostgreSQL
DB_CONFIG = {
    'dbname': os.getenv('DB_NAME', 'vqa_db'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', 'password'),
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', '5432'),
}

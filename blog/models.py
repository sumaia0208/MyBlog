from django.db import models
from blog.db_connection.db_connection import db

blog_collection = db["blogs"]

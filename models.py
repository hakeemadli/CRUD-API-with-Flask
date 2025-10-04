from sqlalchemy import Table, Column, MetaData, Uuid, create_engine, func, ForeignKey, ForeignKeyConstraint
from sqlalchemy.dialects import mysql
from flask import Blueprint, g, current_app
from config import Config
import uuid, enum


models_bp = Blueprint("models", __name__)

'''
models_bp.config["SQLALCHEMY_DB_URI"] = Config.SQLALCHEMY_DB_URI
engine = create_engine(models_bp.config["SQLALCHEMY_DB_URI"],
                       pool_size=10, 
                       max_overflow=20, 
                       pool_recycle=1800, 
                       echo=False, 
                       future=True )
'''

engine = create_engine(Config.SQLALCHEMY_DB_URI)
metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", mysql.INTEGER, primary_key = True, autoincrement = True, unique = True),
    Column("pid", Uuid, unique = True, default= uuid.uuid4),
    Column("email", mysql.VARCHAR(50), nullable = False, unique = True),
    Column("password", mysql.VARCHAR(20), nullable = False),
    Column("permission",mysql.ENUM("Admin", "User", name= "permision_enum"), nullable = False),
    Column("create_at", mysql.DATETIME, server_default = func.now() )
)

contents = Table(
    "contents", 
    metadata,
    Column("id", 1, primary_key= True, unique = True, autoincrement=True),
    Column("user_id", Uuid),
    Column("tag",mysql.ENUM("Personal", "Project", "Documentation", "Tutorial", name= "tag_enum"), nullable = False),
    Column("content", mysql.TEXT),
    Column("create_at", mysql.DATETIME, server_default = func.now() ),
    ForeignKeyConstraint(["user_id"],["users.pid"]),
    
)

metadata.create_all(engine)
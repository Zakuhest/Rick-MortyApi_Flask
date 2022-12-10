from pymongo import MongoClient

conexion = MongoClient('mongodb+srv://cris:134679@clusterdc.1xeuvdc.mongodb.net/test')

db = conexion['Proyecto']
from sqlalchemy import create_engine
import pandas as pd

# Crear conexión a la base de datos
engine = create_engine('mysql+pymysql://usuario:contraseña@host:puerto/nombre_base_datos')

# Extraer datos de cada tabla
orders_df = pd.read_sql('SELECT * FROM Olist_order_dataset', engine)
sellers_df = pd.read_sql('SELECT * FROM Olist_sellers_dataset', engine)
order_items_df = pd.read_sql('SELECT * FROM Olist_order_items_dataset', engine)
geolocation_df = pd.read_sql('SELECT * FROM Olist_geolocation_dataset', engine)
customers_df = pd.read_sql('SELECT * FROM Olist_customers_dataset', engine)
payments_df = pd.read_sql('SELECT * FROM Olist_order_payments_dataset', engine)
reviews_df = pd.read_sql('SELECT * FROM Olist_order_reviews_dataset', engine)
products_df = pd.read_sql('SELECT * FROM Olist_products_dataset', engine)
category_translation_df = pd.read_sql('SELECT * FROM Product_category_name_translation', engine)

from contextlib import closing

from app.models.admin import init_admin_db
from app.models.analytics import (
    get_category_analytics_summary,
    get_product_analytics_summary,
    init_product_analytics_tables,
    record_product_cart_event,
)
from app.models.shared import get_connection

init_admin_db()
init_product_analytics_tables()

with closing(get_connection()) as conn:
    conn.execute("DELETE FROM product_cart_events")
    conn.execute("DELETE FROM product_views")
    conn.execute("DELETE FROM reviews")
    conn.execute("DELETE FROM order_items")
    conn.execute("DELETE FROM orders")
    conn.execute("DELETE FROM customers")
    conn.execute("DELETE FROM products")
    conn.execute("DELETE FROM categories")
    conn.execute("INSERT INTO categories (id, name, slug) VALUES (1, 'Phones', 'phones')")
    conn.execute("INSERT INTO products (id, name, price, currency, image, category_id, description, quantity, sale_percent) VALUES (1, 'Demo', '100', 'PKR', 'x', 1, 'd', 10, 0)")
    conn.commit()

record_product_cart_event(1, user_session_id='abc', user_ip='127.0.0.1', quantity=2, source_page='/search')
print('summary=', get_product_analytics_summary())
print('category=', get_category_analytics_summary())

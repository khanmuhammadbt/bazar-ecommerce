from app import create_app
from app.models.catalog.product import get_all_products

app = create_app()
with app.test_request_context('/'):
    products = get_all_products(page=1, per_page=50)
    sale = [p for p in products if p.get('sale_percent', 0) > 0]
    print('sale count', len(sale))
    if sale:
        product = sale[0]
        print('sale product', product)
        template = app.jinja_env.get_template('index.html')
        html = template.render(
            products=[product],
            hero={},
            hero_slides=[],
            trust_badges=[],
            offers=[],
            title='Home',
            selected_category='',
            selected_price='',
            category_filters=[],
            price_filters=[],
            meta_description='Home page',
            canonical_url='https://example.com/',
            og_image_url='https://example.com/static/images/logo.png',
            structured_data={
                '@context': 'https://schema.org',
                '@type': 'Store',
                'name': 'Banta Bazar',
                'url': 'https://example.com/',
            },
        )
        print('sale-price block exists', 'sale-price' in html, 'regular-price' in html)
        idx = html.find('sale-price')
        print('sale-price index', idx)
        if idx != -1:
            print(html[idx-120:idx+220])

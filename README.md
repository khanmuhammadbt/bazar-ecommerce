
```markdown
# Banta Bazar

Banta Bazar aik full featured e-commerce website hai jo Flask, Jinja2 aur SQLite se banaya gaya hai. Yeh pehle "Electro Shop" ke naam se jana jata tha.

## Features

- Product listing aur AJAX based shopping cart
- Admin dashboard jis mein Chart.js se analytics dikhte hain
- Real time viewer counts (WebSocket se)
- Coupon system for discounts
- Brute force login protection for security
- Modular Blueprint architecture (clean aur scalable code structure)
- Fast performance: image lazy loading, WebP images, render blocking fixes
- Mobile responsive design, sab devices par sahi chalta hai

## Tech Stack

- Backend: Python (Flask)
- Templates: Jinja2
- Database: SQLite
- Frontend: HTML, CSS, JavaScript (Fetch API)
- Real time: WebSocket

## Project Structure

```

bazar-ecommerce/
│
├── app/              # Main application code
├── scripts/          # Helper scripts
├── tests/            # Test files
├── utils/            # Utility functions
├── run.py            # App ko run karne wali file
├── shop.db           # SQLite database
├── requirements.txt  # Python dependencies
├── FEATURES.md       # Features ki detail list
└── project_rules.md  # Security, SEO, performance conventions
```

## Installation

1. Repo clone karo:
```bash
git clone https://github.com/khanmuhammadbt/bazar-ecommerce.git
cd bazar-ecommerce
```

2. Virtual environment banao aur activate karo:
```bash
python -m venv venv
source venv/bin/activate   # Windows par: venv\Scripts\activate
```

3. Dependencies install karo:
```bash
pip install -r requirements.txt
```

4. App run karo:

```bash
python run.py
```

## Default Login (Demo/Testing)

> Note: Yeh sirf demo purpose ke liye hain. Production mein deploy karne se pehle inko zaroor change kar dena.

**Admin Panel:**
- Username: `admin`
- Password: `admin123`

**Test User:**
- Username: `testuser`
- Password: `test1234`

## Environment Variables

Project chalane se pehle `.env` file mein zaroori keys set karo (jaise database URL, secret key, payment gateway keys waghera). Yeh file kabhi bhi public repo mein commit mat karo, isme sensitive data hota hai.

## Contributing

Pull requests aur suggestions ka khair maqdam hai. Koi bug milay ya feature idea ho to Issues section mein bata sakte hain.

## Author

Banta (Khan Muhammad) — Banta Tech ka founder, developer aur content creator.

## License

Abhi is project ka license specify nahi kiya gaya hai.

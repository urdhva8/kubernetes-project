# 🌍 Wanderlust — Travel Booking Website

A full-featured travel booking web application built with Flask and vanilla HTML/CSS/JS.

## Features
- **Home Page** — Hero carousel with 5 destinations, national & international place cards, stats counter, testimonials, newsletter
- **National Destinations** — 6 curated India travel spots with category filter
- **International Destinations** — 6 global destinations with category filter
- **About Page** — Company story, values, team section
- **Booking Page** — Full booking form with sidebar showing selected trip details
- **Booking Success** — Confirmation page with step indicators

## Setup & Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the app
```bash
python app.py
```

### 3. Open in browser
```
http://localhost:5000
```

## Project Structure
```
travel_app/
├── app.py                    # Flask backend
├── requirements.txt
├── templates/
│   ├── base.html             # Shared layout (navbar + footer)
│   ├── index.html            # Home page
│   ├── places.html           # National/International listing
│   ├── about.html            # About & Team
│   ├── booking.html          # Booking form
│   └── booking_success.html  # Confirmation
└── static/
    ├── css/style.css         # All styles
    └── js/main.js            # Interactions
```

## Tech Stack
- **Backend**: Python / Flask
- **Frontend**: HTML5, CSS3, Vanilla JS
- **Fonts**: Playfair Display + DM Sans (Google Fonts)
- **Images**: Unsplash (HD, free to use)

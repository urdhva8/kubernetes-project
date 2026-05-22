from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

national_places = [
    {
        "id": 1,
        "name": "Taj Mahal",
        "location": "Agra, Uttar Pradesh",
        "description": "A stunning ivory-white marble mausoleum and UNESCO World Heritage Site, symbol of eternal love.",
        "image": "https://images.unsplash.com/photo-1564507592333-c60657eea523?w=800&q=80",
        "price": 8999,
        "duration": "3 Days",
        "rating": 4.9,
        "category": "Heritage"
    },
    {
        "id": 2,
        "name": "Kerala Backwaters",
        "location": "Alleppey, Kerala",
        "description": "Serene network of lagoons, lakes, and canals with iconic houseboat experiences.",
        "image": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?w=800&q=80",
        "price": 12499,
        "duration": "5 Days",
        "rating": 4.8,
        "category": "Nature"
    },
    {
        "id": 3,
        "name": "Rajasthan Desert",
        "location": "Jaisalmer, Rajasthan",
        "description": "Golden sand dunes, camel safaris, and majestic forts under a star-studded sky.",
        "image": "https://images.unsplash.com/photo-1477587458883-47145ed94245?w=800&q=80",
        "price": 10999,
        "duration": "4 Days",
        "rating": 4.7,
        "category": "Adventure"
    },
    {
        "id": 4,
        "name": "Manali Valley",
        "location": "Manali, Himachal Pradesh",
        "description": "Snow-capped peaks, apple orchards, and thrilling mountain adventures await.",
        "image": "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?w=800&q=80",
        "price": 9499,
        "duration": "5 Days",
        "rating": 4.8,
        "category": "Mountains"
    },
    {
        "id": 5,
        "name": "Goa Beaches",
        "location": "North Goa, Goa",
        "description": "Vibrant beaches, Portuguese architecture, and an electrifying nightlife scene.",
        "image": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?w=800&q=80",
        "price": 11999,
        "duration": "4 Days",
        "rating": 4.6,
        "category": "Beach"
    },
    {
        "id": 6,
        "name": "Varanasi Ghats",
        "location": "Varanasi, Uttar Pradesh",
        "description": "One of the world's oldest cities, with sacred ghats and mesmerizing Ganga Aarti.",
        "image": "https://images.unsplash.com/photo-1561361058-c24cecae35ca?w=800&q=80",
        "price": 7499,
        "duration": "3 Days",
        "rating": 4.7,
        "category": "Spiritual"
    }
]

international_places = [
    {
        "id": 7,
        "name": "Santorini",
        "location": "Cyclades, Greece",
        "description": "Iconic whitewashed buildings, crystal-blue domes, and breathtaking caldera sunsets.",
        "image": "https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?w=800&q=80",
        "price": 89999,
        "duration": "7 Days",
        "rating": 4.9,
        "category": "Beach"
    },
    {
        "id": 8,
        "name": "Bali",
        "location": "Denpasar, Indonesia",
        "description": "Tropical paradise with terraced rice fields, ancient temples, and spiritual retreats.",
        "image": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?w=800&q=80",
        "price": 54999,
        "duration": "7 Days",
        "rating": 4.8,
        "category": "Tropical"
    },
    {
        "id": 9,
        "name": "Paris",
        "location": "Île-de-France, France",
        "description": "The City of Light — art, haute cuisine, the Eiffel Tower, and timeless romance.",
        "image": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=800&q=80",
        "price": 119999,
        "duration": "8 Days",
        "rating": 4.9,
        "category": "City"
    },
    {
        "id": 10,
        "name": "Maldives",
        "location": "South Malé Atoll, Maldives",
        "description": "Overwater bungalows, turquoise lagoons, and the world's most pristine coral reefs.",
        "image": "https://images.unsplash.com/photo-1573843981267-be1999ff37cd?w=800&q=80",
        "price": 149999,
        "duration": "6 Days",
        "rating": 5.0,
        "category": "Luxury"
    },
    {
        "id": 11,
        "name": "Swiss Alps",
        "location": "Interlaken, Switzerland",
        "description": "Majestic alpine scenery, chocolate-box villages, and world-class ski resorts.",
        "image": "https://images.unsplash.com/photo-1531366936337-7c912a4589a7?w=800&q=80",
        "price": 134999,
        "duration": "8 Days",
        "rating": 4.8,
        "category": "Mountains"
    },
    {
        "id": 12,
        "name": "Tokyo",
        "location": "Kanto, Japan",
        "description": "A mesmerizing blend of ancient temples, futuristic tech, and extraordinary culinary culture.",
        "image": "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=800&q=80",
        "price": 109999,
        "duration": "9 Days",
        "rating": 4.9,
        "category": "City"
    }
]

team_members = [
    {"name": "Priya Sharma", "role": "CEO & Founder", "image": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=400&q=80", "bio": "15 years crafting unforgettable journeys across 60+ countries."},
    {"name": "Arjun Mehta", "role": "Head of Operations", "image": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=400&q=80", "bio": "Expert logistics planner ensuring seamless travel experiences."},
    {"name": "Sneha Kapoor", "role": "Travel Curator", "image": "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=400&q=80", "bio": "Passionate about discovering hidden gems and local culture."},
    {"name": "Rohan Verma", "role": "Customer Experience", "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&q=80", "bio": "Dedicated to making every traveler's dream come true."}
]

@app.route('/')
def home():
    return render_template('index.html', 
                           national=national_places[:4], 
                           international=international_places[:4],
                           year=datetime.now().year)

@app.route('/national')
def national():
    return render_template('places.html', places=national_places, title="National Destinations", year=datetime.now().year)

@app.route('/international')
def international():
    return render_template('places.html', places=international_places, title="International Destinations", year=datetime.now().year)

@app.route('/about')
def about():
    return render_template('about.html', team=team_members, year=datetime.now().year)

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    place_id = request.args.get('id', type=int)
    all_places = national_places + international_places
    selected_place = next((p for p in all_places if p['id'] == place_id), None)
    if request.method == 'POST':
        return render_template('booking_success.html', 
                               name=request.form.get('name'),
                               place=request.form.get('place'),
                               year=datetime.now().year)
    return render_template('booking.html', 
                           places=all_places, 
                           selected=selected_place,
                           year=datetime.now().year)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

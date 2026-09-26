from flask import Flask, render_template_string
app = Flask(__name__)

products = [
    {"name": "HP Laptop", "price": 45000, "image": "https://images.unsplash.com/photo-1588872657576-7efd1f1555ed?w=500&q=80", "desc": "Core i5, 8GB RAM, Fast"},
    {"name": "Tecno Phone", "price": 18000, "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500&q=80", "desc": "128GB Storage, 5000mAh"},
    {"name": "Bluetooth Speaker", "price": 3500, "image": "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=500&q=80", "desc": "Loud Bass, 12H Battery"},
    {"name": "Smart Watch", "price": 5000, "image": "https://images.unsplash.com/photo-1523275335684-37898b6af30f?w=500&q=80", "desc": "Heart Rate, Waterproof"},
    {"name": "Wireless Earbuds", "price": 2500, "image": "https://images.unsplash.com/photo-1572569511254-d8f925fe2cbb?w=500&q=80", "desc": "Noise Cancel, Case"},
    {"name": "Power Bank 20000mAh", "price": 3000, "image": "https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5?w=500&q=80", "desc": "Fast Charge, 2 Ports"}
]

TEMPLATE = """
<html><head><title>TJMALL</title><meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{font-family:Arial;margin:0;background:#f5f5f5}
.header{background:#0a8a0a;color:white;padding:15px;text-align:center}
.products{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:15px;padding:15px;max-width:1000px;margin:auto}
.card{background:white;border-radius:10px;overflow:hidden;box-shadow:0 2px 5px rgba(0,0,0,0.1)}
.card img{width:100%;height:160px;object-fit:cover;background:#eee}
.info{padding:10px}
.price{color:#0a8a0a;font-weight:bold;font-size:18px}
.btn{display:block;background:#0a8a0a;color:white;text-align:center;padding:10px;border-radius:5px;text-decoration:none;margin-top:8px;font-weight:bold}
</style></head><body>
<div class="header"><h1>TJMALL</h1><p>Fast Delivery Kenya | Pay on Delivery | Call: 0724650536</p></div>
<div class="products">
{% for p in products %}
<div class="card"><img src="{{p.image}}" loading="lazy"><div class="info">
<h3>{{p.name}}</h3><p>{{p.desc}}</p><div class="price">KSh {{p.price}}</div>
<a class="btn" href="https://wa.me/254724650536?text=Hello%20TJMALL%20I%20want%20{{p.name}}%20KSh%20{{p.price}}" target="_blank">Order WhatsApp</a>
</div></div>
{% endfor %}
</div>
</body></html>
"""

@app.route('/')
def home():
    return render_template_string(TEMPLATE, products=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

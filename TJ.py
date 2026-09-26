from flask import Flask, render_template_string

app = Flask(__name__)

products = [
    {"name": "HP Laptop", "price": 45000, "image": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=500", "desc": "Core i5, 8GB RAM"},
    {"name": "Tecno Phone", "price": 18000, "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500", "desc": "128GB, 6.5 inch"},
    {"name": "Speaker", "price": 3500, "image": "https://images.unsplash.com/photo-1608043152269-423dbba4e7e4?w=500", "desc": "Super bass"},
    {"name": "Smart Watch", "price": 5000, "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500", "desc": "Waterproof"},
]

TEMPLATE = """
<html><head><title>TJMALL</title><meta name="viewport" content="width=device-width, initial-scale=1">
<style>body{font-family:Arial;margin:0;background:#f5f5f5}.header{background:#0a8a0a;color:white;padding:15px;text-align:center}
.products{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:15px;padding:15px;max-width:1000px;margin:auto}
.card{background:white;border-radius:10px;overflow:hidden;box-shadow:0 2px 5px rgba(0,0,0,0.1)}
.card img{width:100%;height:160px;object-fit:cover}.info{padding:10px}
.price{color:#0a8a0a;font-weight:bold}.btn{display:block;background:#0a8a0a;color:white;text-align:center;padding:8px;border-radius:5px;text-decoration:none;margin-top:8px}
</style></head><body>
<div class="header"><h1>TJMALL - Online Store</h1><p>Fast Delivery Kenya | Pay on Delivery</p></div>
<div class="products">
{% for p in products %}
<div class="card"><img src="{{p.image}}"><div class="info">
<h3>{{p.name}}</h3><p>{{p.desc}}</p><div class="price">KSh {{p.price}}</div>
<a class="btn" href="https://wa.me/254700000000?text=I%20want%20{{p.name}}" target="_blank">Order WhatsApp</a>
</div></div>
{% endfor %}</div></body></html>
"""

@app.route('/')
def home():
    return render_template_string(TEMPLATE, products=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

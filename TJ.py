from flask import Flask, render_template_string

app = Flask(__name__)

products = [
    {"name": "HP Laptop", "price": 45000, "image": "https://images.unsplash.com/photo-1496181133206-80ce9b8a8536?w=500&q=80", "desc": "Core i5, 8GB RAM, Fast"},
    {"name": "Tecno Phone", "price": 18000, "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500&q=80", "desc": "128GB Storage, 5000mAh"},
    {"name": "Bluetooth Speaker", "price": 3500, "image": "https://images.unsplash.com/photo-1608043152269-423dbbb4e7e4?w=500&q=80", "desc": "Loud Bass, 12H Battery"},
    {"name": "Smart Watch", "price": 5000, "image": "https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=500&q=80", "desc": "Heart Rate, Waterproof"},
    {"name": "Wireless Earbuds", "price": 2500, "image": "https://images.unsplash.com/photo-1572569511254-d8f925fe2cbb?w=500&q=80", "desc": "Noise Cancel, Case"},
    {"name": "Power Bank 20000mAh", "price": 3000, "image": "https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5?w=500&q=80", "desc": "Fast Charge, 2 Ports"}
]

TEMPLATE = """
<!DOCTYPE html>
<html><head>
<title>TJMALL - Best Deals Kenya</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{font-family:Arial;margin:0;background:#f5f5f5}
.header{background:#0a8a0a;color:white;padding:15px;text-align:center;position:sticky;top:0;z-index:10}
.header h1{margin:0}
.products{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:15px;padding:15px;max-width:1000px;margin:auto}
.card{background:white;border-radius:10px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,0.1);transition:0.2s}
.card:hover{transform:translateY(-3px)}
.card img{width:100%;height:180px;object-fit:cover;background:#eee;display:block}
.info{padding:12px}
.info h3{margin:5px 0;font-size:16px}
.info p{color:#666;font-size:13px;margin:5px 0}
.price{color:#0a8a0a;font-weight:bold;font-size:18px;margin:8px 0}
.btn{display:block;background:#0a8a0a;color:white;text-align:center;padding:10px;border-radius:6px;text-decoration:none;font-weight:bold}
.btn:hover{background:#076607}
.footer{text-align:center;padding:20px;color:#666}
</style>
</head><body>
<div class="header">
<h1>TJMALL</h1>
<p>Fast Delivery Kenya | Pay on Delivery | Call: +254 724 650 536</p>
</div>
<div class="products">
{% for p in products %}
<div class="card">
<img src="{{p.image}}" alt="{{p.name}}" loading="lazy" onerror="this.src='https://via.placeholder.com/500x300?text={{p.name}}'">
<div class="info">
<h3>{{p.name}}</h3>
<p>{{p.desc}}</p>
<div class="price">KSh {{p.price}}</div>
<a class="btn" href="https://wa.me/254724650536?text=Hello%20TJMALL%20I%20want%20to%20order%20{{p.name}}%20for%20KSh%20{{p.price}}" target="_blank">Order WhatsApp (+254)</a>
</div></div>
{% endfor %}
</div>
<div class="footer">
<p>© 2026 TJMALL Kenya - All Rights Reserved<br>WhatsApp: +254 724 650 536</p>
</div>
</body></html>
"""

@app.route('/')
def home():
    return render_template_string(TEMPLATE, products=products)

@app.route('/health')
def health():
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

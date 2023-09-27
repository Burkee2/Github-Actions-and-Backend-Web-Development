from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/page1')
def page1():
   
    dynamic_content = "This content is generated from the server side i think maybe maybe not"
    return render_template('page1.html', dynamic_content=dynamic_content)

@app.route('/page2')
def page2():
    
    dynamic_content = "More dynamic content from the server woohoo!"
    return render_template('page2.html', dynamic_content=dynamic_content)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # List of image URLs
    image_urls = [
        'https://www.jenkins.io/images/logo-title-opengraph.png',
        'https://bunnyacademy.b-cdn.net/what-is-docker.png',
        'https://miro.medium.com/v2/resize:fit:600/1*Pbb5rmrwh-eAFWXd8ws79A.png',
        # Add more image URLs as needed
    ]

    return render_template('index.html', image_urls=image_urls)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/price')
def get_avg_price():
    try:
        # Fetch the HTML content of the Website provided
        url = 'https://www.metal.com/Lithium-ion-Battery/202303240001'
        response = requests.get(url)
        html = response.content

        # Use BeautifulSoup to parse the HTML and extract the div element that contains the span element for the average price 
        soup = BeautifulSoup(html, 'html.parser')
        div_element = soup.find('div', class_='block___2RfAT')
        if div_element is None:
            raise Exception('Failed to find the div tag that containts span element with average price.')

        price = [span.get_text(strip=True) for span in div_element.find_all('span')][1]

        # Return the price in the API response as a string
        #return jsonify({'price': price})
        return price
        
    except Exception as e:
        # Handle any errors that occur during the request
        print(e)
        return jsonify({'error': 'Failed to fetch price'}), 500

if __name__ == '__main__':
    app.run(debug=True)

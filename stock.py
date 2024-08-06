# Python Flask code
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def inventory_quantity():
    if request.method == 'POST':
        urls = request.form['url'].split('\n')
        inventory_data = []

        for url in urls:
            try:
                response = requests.get(url.strip())
                html_content = response.text
                soup = BeautifulSoup(html_content, 'html.parser')

                title_element = soup.find(class_='product-page--title')
                title_text = title_element.get_text() if title_element else '無'

                vendor_element = soup.find(class_='product-page--vendor')
                vendor_text = vendor_element.get_text() if vendor_element else '無'

                variant_select = soup.find('select', class_='product-form--variant-select')
                data_inventory_quantity = variant_select.find('option')['data-inventory-quantity']

                inventory_data.append({'title': title_text, 'vendor': vendor_text, 'quantity': data_inventory_quantity})
            except:
                inventory_data.append({'title': '無', 'vendor': '無', 'quantity': '無'})

        return render_template('index.html', inventory_data=inventory_data)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()

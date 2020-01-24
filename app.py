from flask import Flask, request, render_template
#from airtable import Airtable

import pickle
import csv

app = Flask(__name__)
# airtable = Airtable('apppRkyEG5N3DMbaZ', 'user_data', api_key='keyfbkI9WoPwdcQT1')

crops_dict = {'Arecanut': 0, 'Other Kharif pulses': 1, 'Rice': 2, 'Banana': 3, 'Cashewnut': 4, 'Coconut': 5,
              'Dry ginger': 6, 'Sugarcane': 7, 'Sweet potato': 8, 'Tapioca': 9, 'Black pepper': 10,
              'Dry chillies': 11, 'other oilseeds': 12, 'Turmeric': 13, 'Maize': 14, 'Moong(Green Gram)': 15,
              'Urad': 16, 'Arhar/Tur': 17, 'Groundnut': 18, 'Sunflower': 19, 'Bajra': 20, 'Castor seed': 21,
              'Cotton(lint)': 22, 'Horse-gram': 23, 'Jowar': 24, 'Korra': 25, 'Ragi': 26, 'Tobacco': 27,
              'Gram': 28, 'Wheat': 29, 'Masoor': 30, 'Sesamum': 31, 'Linseed': 32, 'Safflower': 33,
              'Onion': 34, 'other misc. pulses': 35, 'Samai': 36, 'Small millets': 37, 'Coriander': 38,
              'Potato': 39, 'Other  Rabi pulses': 40, 'Soyabean': 41, 'Beans & Mutter(Vegetable)': 42,
              'Bhindi': 43, 'Brinjal': 44, 'Citrus Fruit': 45, 'Cucumber': 46, 'Grapes': 47, 'Mango': 48,
              'Orange': 49, 'other fibres': 50, 'Other Fresh Fruits': 51, 'Other Vegetables': 52, 'Papaya': 53,
              'Pome Fruit': 54, 'Tomato': 55, 'Rapeseed &Mustard': 56, 'Mesta': 57, 'Cowpea(Lobia)': 58,
              'Lemon': 59, 'Pome Granet': 60, 'Sapota': 61, 'Cabbage': 62, 'Peas  (vegetable)': 63,
              'Niger seed': 64, 'Bottle Gourd': 65, 'Sannhamp': 66, 'Varagu': 67, 'Garlic': 68,
              'Ginger': 69, 'Oilseeds total': 70, 'Pulses total': 71, 'Jute': 72, 'Peas & beans (Pulses)': 73,
              'Blackgram': 74, 'Paddy': 75, 'Pineapple': 76, 'Barley': 77, 'Khesari': 78, 'Guar seed': 79,
              'Moth': 80, 'Other Cereals & Millets': 81, 'Cond-spcs other': 82, 'Turnip': 83, 'Carrot': 84,
              'Redish': 85, 'Arcanut (Processed)': 86, 'Atcanut (Raw)': 87, 'Cashewnut Processed': 88,
              'Cashewnut Raw': 89, 'Cardamom': 90, 'Rubber': 91, 'Bitter Gourd': 92, 'Drum Stick': 93,
              'Jack Fruit': 94, 'Snak Guard': 95, 'Pump Kin': 96, 'Tea': 97, 'Coffee': 98, 'Cauliflower': 99,
              'Other Citrus Fruit': 100, 'Water Melon': 101, 'Total foodgrain': 102, 'Kapas': 103,
              'Colocosia': 104, 'Lentil': 105, 'Bean': 106, 'Jobster': 107, 'Perilla': 108, 'Rajmash Kholar': 109,
              'Ricebean (nagadal)': 110, 'Ash Gourd': 111, 'Beet Root': 112, 'Lab-Lab': 113, 'Ribed Guard': 114,
              'Yam': 115, 'Apple': 116, 'Peach': 117, 'Pear': 118, 'Plums': 119, 'Litchi': 120, 'Ber': 121,
              'Other Dry Fruit': 122, 'Jute & mesta': 123}

season_dict = {'Kharif': 0, 'Whole Year': 1, 'Autumn': 2, 'Rabi': 3, 'Summer': 4, 'Winter': 5}

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
kharif_months = {'Jul', 'Aug', 'Sep', 'Oct'}
autumn_months = {'Sep', 'Oct', 'Nov'}
rabi_months = {'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar'}
summer_months = {'Jun', 'Jul', 'Aug'}
winter_months = {'Dec', 'Jan', 'Feb'}

crops_dist = {}
with open('crops_dist.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        crops_dist[row[0]] = row[1:]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/register.html')
def register():
    return render_template('register.html')


@app.route('/weatherupdates.html')
def weatherupdates():
    return render_template('weatherupdates.html')

@app.route('/DiscussionForum.html')
def discussionFrom():
    return render_template('DiscussionForum.html')

@app.route('/register.html', methods=['POST'])
def register_airtable():
    # f_name = request.form['firstname']
    # l_name = request.form['lastname']
    # phone = request.form['phone']
    # state = request.form['state']
    # dist = request.form['district']
    # pin = request.form['pin']
    # address = request.form['address']

    # if len(phone) > 10:
    #     phone = phone[len(phone)-10:]
    #
    # details = {'Phone': phone, 'First Name': f_name, 'Last Name': l_name,
    #            'State': state, 'District': dist, 'Pin Code': pin, 'Address': address}
    #
    # airtable.insert(details)

    return render_template('index.html')


@app.route('/results.html')
def results():
    return render_template('results.html')


@app.route('/askaquestion.html')
def askaquestion():
    return render_template('askaquestion.html')


@app.route('/smartguide.html')
def smartguide():
    return render_template('smartguide.html')

# @app.route('/results.html')
# def results():
#     return render_template('results.html')


def seasons_extract(mon):
    seasons = ['Whole Year']
    if mon in kharif_months:
        seasons.append('Kharif')

    if mon in autumn_months:
        seasons.append('Autumn')

    if mon in rabi_months:
        seasons.append('Rabi')

    if mon in summer_months:
        seasons.append('Summer')

    if mon in winter_months:
        seasons.append('Winter')

    return seasons


@app.route('/smartguide.html', methods=['POST'])
def predict():
    # print(type(request.args))
    # if request.method == 'POST':
    date = request.form['date']
    state = request.form['state'].title()
    dist = request.form['district'].upper()

    print(date, state, dist)

    year = date[:4]
    mon = months[int(date[5:7]) - 1]
    # print(int(date[5:7]), year, mon)

    rainfall_avg = 0
    for m in months:
        rainfall_file_name = 'Rainfall/' + dist.lower() + '_' + m.lower() + '_rainfall.pkl'
        rainfall_model = pickle.load(open(rainfall_file_name, 'rb'))

        rainfall_avg += rainfall_model.predict([[year]])

    rainfall_avg = rainfall_avg / 12

    crop_file_name = 'Crop/' + dist.lower() + '_crop.pkl'
    crop_model = pickle.load(open(crop_file_name, 'rb'))

    seasons = seasons_extract(mon)

    result = {}
    for season in seasons:
        for crop in crops_dist[dist]:
            pa = crop_model.predict([[year, season_dict[season], crops_dict[crop], rainfall_avg]])

            # result.append([pa[0], crop])

            if crop in result.keys():
                # result[crop] = max(pa[0], result[crop])
                if pa[0] > result[crop][0]:
                    result[crop] = [pa[0], season]

            else:
                result[crop] = [pa[0], season]

    result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)}

        # first_key1 = next(iter(result))
        # crop_img1 = 'https://source.unsplash.com/200x300/?'+first_key1
    # print(rainfall, pa)
    # print(crops_dist)

    print(result)

    itr = iter(result)

    first_key1 = next(itr)
    crop_img1 = first_key1+'.png'

    try:
        first_key2 = next(itr)
        crop_img2 = first_key2 + '.png'

    except StopIteration:
        return render_template('results.html', crop_name1=first_key1, crop_img1=crop_img1, production1=result[first_key1])

    try:
        first_key3 = next(itr)
        crop_img3 = first_key3 + '.png'

    except StopIteration:
        return render_template('results.html',
                               crop_name1=first_key1, crop_img1=crop_img1, production1=result[first_key1],
                               crop_name2=first_key2, crop_img2=crop_img2, production2=result[first_key2])

    return render_template('results.html',
                           crop_name1=first_key1, crop_img1=crop_img1, production1=result[first_key1],
                           crop_name2=first_key2, crop_img2=crop_img2, production2=result[first_key2],
                           crop_name3=first_key3, crop_img3=crop_img3, production3=result[first_key3])


if __name__ == "__main__":
    app.run(debug=True)

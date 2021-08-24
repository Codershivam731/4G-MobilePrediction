import pickle

from flask import Flask, render_template, request
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('naive_model.pkl', 'rb'))


@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        battery_power = int(request.form['battery_power'])
        clock_speed = float(request.form['clock_speed'])
        blue = int(request.form['blue'])
        dual_sim = int(request.form['dual_sim'])
        int_memory = int(request.form['int_memory'])
        fc = int(request.form['fc'])
        n_cores = int(request.form['n_cores'])
        m_dep = float(request.form['m_dep'])
        mobile_wt = int(request.form['mobile_wt'])
        pc = int(request.form['pc'])
        px_height = int(request.form['px_height'])
        px_width = int(request.form['px_width'])
        ram = int(request.form['ram'])
        sc_h = int(request.form['sc_h'])
        sc_w = int(request.form['sc_w'])
        talk_time = int(request.form['talk_time'])
        three_g = int(request.form['three_g'])
        touch_screen = int(request.form['touch_screen'])
        wifi = int(request.form['wifi'])
        price_range = int(request.form['price_range'])

        prediction = model.predict([[battery_power, clock_speed, blue, dual_sim, int_memory, fc, n_cores, m_dep,
                                     mobile_wt, pc, px_height, px_width, ram, sc_h, sc_w, talk_time, three_g,
                                     touch_screen, wifi, price_range]])
        output = int(prediction)
        if output == 0:
            return render_template('index.html', prediction_text="PHONE IS NOT 4G [{}]".format(output))
        elif output == 1:
            return render_template('index.html', prediction_text="PHONE IS 4G  [{}]".format(output))
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

from flask import *
#追加------------
import sukii
import Rebuildin
import rental
import paypay
#------------------

app = Flask(__name__)

menber1 = 0
menber2 = 0
menber3 = 0
menber4 = 0
menber5 = 0
menber6 = 0
menber7 = 0
menber8 = 0


@app.route("/")
def index():
    return render_template('index.html')
    
#変更&追加-----------------------
@app.route("/nittei")
def nittei():
	return render_template('nittei.html')

@app.route("/skiing", methods=['GET','POST'])
def skiing():
	if request.method == 'GET':
		return render_template('skiing.html')
	elif request.method == 'POST':
		lift1 = request.form['lift1']
		wear1 = request.form['wear1']
		chose1 = request.form['chose1']
		change1 = request.form['change1']
		lift2 = request.form['lift2']
		wear2 = request.form['wear2']
		chose2 = request.form['chose2']
		change2 = request.form['change2']
		result1 = sukii.client(lift1, wear1, chose1, change1, lift2, wear2, chose2, change2)
		return render_template('skiing.html', 
                         lift1 = result1[0], 
                         wear1 = result1[1], 
                         chose1 = result1[2], 
                         change1 = result1[3], 
                         lift2 = result1[4], 
                         wear2 = result1[5], 
                         chose2 = result1[6], 
                         change2 = result1[7], 
                         money = result1[8])

@app.route("/Rebuilding", methods=['GET','POST'])
def Rebuilding():
    if request.method == 'GET':
        result = paypay.All()
        return render_template('Rebuilding.html',
                               allpay = result[8], 
                               hitori = result[9],
                               tatekae = result[10],
                               num = result[11],
                               menber = result[12])
    elif request.method == 'POST':
        tatekae = request.form['tatekae']
        delnumber = ""
        if tatekae == "del":
            delnumber = request.form['del']
        kinds = request.form['kinds']
        sonota = "None"
        if request.form.get('kingaku'):
            kingaku = request.form['kingaku']
            if kinds == "sonota":
                if request.form.get('sonota'):
                    sonota = request.form['sonota']
        
        n = 0
        name = [0,0,0,0,0,0,0,0]
        if request.form.get('ginji'):
            name.insert(0,1)
            n = n + 1
        if request.form.get('daiki'):
            name.insert(1,1)
            n = n + 1
        if request.form.get('riki'):
            name.insert(2,1)
            n = n + 1
        if request.form.get('miyu'):
            name.insert(3,1)
            n = n + 1
        if request.form.get('hikaru'):
            name.insert(4,1)
            n = n + 1
        if request.form.get('kana'):
            name.insert(5,1)
            n = n + 1
        if request.form.get('ryuya'):
            name.insert(6,1)
            n = n + 1
        if request.form.get('kai'):
            name.insert(7,1)
            n = n + 1
        Rebuildin.client(kingaku, tatekae, n, name, kinds, sonota, delnumber)
        result = paypay.All()
        return render_template('Rebuilding.html',
                               allpay = result[8], 
                               hitori = result[9],
                               tatekae = result[10],
                               num = result[11],
                               menber = result[12])

@app.route("/rentalcar", methods=['GET','POST'])
def rentalcar():
    if request.method == "GET":
        return render_template('rentalcar.html')
    elif request.method == "POST":
        kyori = request.form['kyori']
        car = request.form['car']
        result3 = rental.client(kyori, car)
        return render_template('rentalcar.html', 
                               money = result3[0], 
                               car = result3[1])
@app.route("/money", methods=['GET','POST'])
def pay():
    if request.method == "GET":
        return render_template('paypay.html')
    elif request.method == "POST":
        menber = request.form['menber']
        if menber == "all":
            result = paypay.All()
            return render_template('paypay.html', all = result)
        else:
            result = paypay.client(menber)
            return render_template('paypay.html', 
                                   menber=result[0], 
                                   money1 = result[1], 
                                   money2 = result[2], 
                                   human = result[3])
#-------------------------------------

if __name__ == '__main__':
    app.run(port=1000,host="0.0.0.0")
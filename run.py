from flask import Flask,render_template
app = Flask(__name__)

@app.route('/moro')
def template_test():
    return render_template('template.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5],liste_des_technos=['Linux','Physique','Jenkins','Ansible','Kubernetes','Docker','Git','Terraform','cloud_aws'])

@app.route("/")
def index():
  return render_template('index.html')
    #return "cool les gars, ca marche!!"

@app.route('/yvon')
def yvon_index():
  return render_template('yvon_index.html')
    #return "cool les gars, ca marche!!"

@app.route('/amel')
def amel_index():
  return render_template('amel_index.html')
    #return "cool les gars, ca marche!!"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5555)

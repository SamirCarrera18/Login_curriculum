from flask import Flask, render_template, request, url_for 

app = Flask(__name__) 
 
@app.route("/")
def index():
    return render_template("Login_curriculum.html")
 

@app.route("/", methods=["GET","POST"])
def hola():
    email = request.form.get("email") 
    email=email
    if email == "samir.carrera@ucsp.edu.pe":
        return render_template("Curriculum1.html")
        
    elif email == "valeria.delaoliva@ucsp.edu.pe":
        return render_template("Curriculum2.html")
        
    elif email == "juan.farfan@ucsp.edu.pe":
        return render_template("Curriculum3.html")
    else:
        return "Revise que sus datos fueron ingresados correctamente"
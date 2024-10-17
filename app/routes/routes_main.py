from flask import Blueprint, render_template, url_for

bp = Blueprint("main",__name__,template_folder='../templates/main')

@bp.route('/',endpoint='home')
def index():
    return render_template("frutas.html")

@bp.route('/categorias',endpoint='categorias')
def categorias():
    return render_template("categorias.html")

@bp.route('/cadastro',endpoint='cadastro')
def cadastro():
    return render_template("cadastro.html")
from flask import Flask, request, render_template
from modules.chromadb_handler import query_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if not query:
        return render_template('index.html', error="Nenhuma consulta foi fornecida.")

    results = query_data(query)
    if results:
        return render_template('index.html', results=results)
    else:
        return render_template('index.html', error="Nenhum dado encontrado.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

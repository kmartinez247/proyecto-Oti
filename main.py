from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import os
from db_unified import guardar_residuo, obtener_todos_registros, obtener_estadisticas, eliminar_registro, actualizar_estado

app = Flask(__name__)
CORS(app)  # Permitir peticiones desde el HTML

@app.route('/')
def index():
    # Leer el archivo HTML
    with open('ecorecycle (1).html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    return render_template_string(html_content)

@app.route('/api/residuos', methods=['GET'])
def get_residuos():
    """API para obtener todos los residuos"""
    registros = obtener_todos_registros()
    # Convertir al formato que espera el frontend
    residuos_formateados = []
    for r in registros:
        residuos_formateados.append({
            'id': r['id'],
            'tipo': r['aparato'],
            'marca': r['marca'],
            'descripcion': r['comentario'],
            'peso': r['cantidad_peso'],
            'cantidad': 1,
            'punto': r['punto_entrega'],
            'estado': r['estado'],
            'usuario': r['usuario']
        })
    return jsonify(residuos_formateados)

@app.route('/api/residuos', methods=['POST'])
def post_residuo():
    """API para guardar un nuevo residuo"""
    data = request.json
    
    id_nuevo = guardar_residuo(
        aparato=data.get('tipo', ''),
        cantidad_peso=data.get('peso', 0),
        categoria=data.get('tipo', ''),
        estado='Pendiente',
        comentario=data.get('descripcion', ''),
        usuario=data.get('usuario', 'usuario'),
        punto_entrega=data.get('punto', '')
    )
    
    return jsonify({'ok': True, 'id': id_nuevo})

@app.route('/api/residuos/<int:id_registro>', methods=['DELETE'])
def delete_residuo(id_registro):
    """API para eliminar un residuo"""
    eliminar_registro(id_registro)
    return jsonify({'ok': True})

@app.route('/api/residuos/<int:id_registro>/estado', methods=['PUT'])
def update_estado(id_registro):
    """API para actualizar estado"""
    data = request.json
    actualizar_estado(id_registro, data.get('estado'))
    return jsonify({'ok': True})

@app.route('/api/estadisticas', methods=['GET'])
def get_estadisticas():
    """API para obtener estadísticas"""
    stats = obtener_estadisticas()
    return jsonify(stats)

@app.route('/enviar', methods=['POST'])
def enviar():
    """Endpoint original para el formulario"""
    aparato = request.form.get('aparato')
    cantidad = request.form.get('cantidad')
    categoria = request.form.get('categoria')
    estado = request.form.get('estado')
    comentario = request.form.get('comentario', '')
    
    guardar_residuo(aparato, cantidad, categoria, estado, comentario)
    
    return "Registro exitoso. Datos guardados en registros_ewaste.xlsx"

if __name__ == '__main__':
    # Asegurar que la base de datos existe
    from db_unified import get_workbook
    get_workbook()
    
    print("=" * 50)
    print("🔄 Servidor EcoRecycle iniciado")
    print(f"📁 Base de datos: registros_ewaste.xlsx")
    print(f"🌐 Servidor en: http://localhost:5000")
    print("=" * 50)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
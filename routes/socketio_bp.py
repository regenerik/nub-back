# routes/socketio_bp.py
from flask import request
from flask_socketio import emit

def init_socketio(socketio):
    """
    Inicializa los eventos de Socket.IO.
    """
    @socketio.on('connect')
    def handle_connect():
        """
        Se ejecuta cada vez que un cliente se conecta.
        """
        print(f">>> Un cliente se ha conectado: {request.sid}")
        # Emitimos un mensaje de bienvenida solo a este cliente
        emit('server_message', {'msg': '¡Conexión establecida!'}, room=request.sid)

    @socketio.on('disconnect')
    def handle_disconnect():
        """
        Se ejecuta cada vez que un cliente se desconecta.
        """
        print(f"<<< Un cliente se ha desconectado: {request.sid}")

    @socketio.on('test_message')
    def handle_test_message(data):
        """
        Una ruta de prueba. Recibe un mensaje del cliente y responde.
        """
        received_message = data.get('message', 'No message received')
        print(f"Mensaje de prueba recibido: '{received_message}'")
        # Enviamos un mensaje de vuelta al cliente que lo mandó
        emit('test_response', {'status': 'OK', 'received': received_message})
        
    @socketio.on('saludo')
    def handle_saludo(data):
        received_message = data.get('message', 'No message received')
        print(f"Mensaje de prueba recibido: '{received_message}'")
        # Enviamos un mensaje de vuelta al cliente que lo mandó
        emit('saludo', {'status': 'OK', 'received': received_message})
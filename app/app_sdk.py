import tornado.ioloop
import tornado.web
import json
import os
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Importar Dynatrace OneAgent SDK
import oneagent

# Inicializar Dynatrace OneAgent SDK
oneagent.initialize()

# Obtener variables de entorno
db_host = os.getenv('DBHOST', 'localhost')  # Default a 'localhost' si no está definida
db_port = os.getenv('DBPORT', '3306')       # Default a '3306' si no está definida

# Configuración de la Base de Datos
DATABASE_URI = f'mysql+pymysql://user:password@{db_host}:{db_port}/mydatabase'
Base = declarative_base()

# Modelo SQLAlchemy para pedidos
class Pedido(Base):
    __tablename__ = 'pedidos'
    id = Column(Integer, primary_key=True)
    numero = Column(Integer)

# Crear motor y sesión de SQLAlchemy
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

# Tornado Request Handler para /ping
class PingHandler(tornado.web.RequestHandler):
    def get(self):
        with oneagent.get_sdk().trace_web_request(self.request) as tracer:
            tracer.start()
            self.write("pong")
            tracer.end()

# Tornado Request Handler para /pedido (POST)
class PedidoHandler(tornado.web.RequestHandler):
    def post(self):
        with oneagent.get_sdk().trace_web_request(self.request) as tracer:
            tracer.start()
            try:
                data = json.loads(self.request.body)
                numero = int(data.get('numero'))
                session = Session()
                nuevo_pedido = Pedido(numero=numero)
                session.add(nuevo_pedido)
                session.commit()
                session.close()
                self.write({"message": "registro agregado"})
            except ValueError:
                self.set_status(400)
                self.write({"error": "Solo se aceptan números"})
                tracer.error("Error: Solo se aceptan números")
            tracer.end()

# Tornado Request Handler para /pedidos (GET)
class PedidosHandler(tornado.web.RequestHandler):
    def get(self):
        with oneagent.get_sdk().trace_web_request(self.request) as tracer:
            tracer.start()
            session = Session()
            pedidos = session.query(Pedido).all()
            session.close()
            self.write({"pedidos": [{"id": pedido.id, "numero": pedido.numero} for pedido in pedidos]})
            tracer.end()

# Crear aplicación Tornado y definir rutas
def make_app():
    return tornado.web.Application([
        (r"/ping", PingHandler),
        (r"/pedido", PedidoHandler),
        (r"/pedidos", PedidosHandler),
    ])

# Ejecutar aplicación
if __name__ == "__main__":
    Base.metadata.create_all(engine)
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

    # Apagar el SDK de Dynatrace antes de finalizar la aplicación
    oneagent.shutdown()

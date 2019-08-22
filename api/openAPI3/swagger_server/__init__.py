import sys
sys.path.append('../..')
hasconfig=True
try:
  import config.server.params as params
except ImportError:
  hasconfig=False

import connexion

from swagger_server import encoder

def create_app():
    port=8080 # default

    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder

    addApi=True
    if hasconfig:
      if params.port != "":
        port=params.port
      if params.basePath != "":
        app.add_api('swagger.yaml', base_path=params.basePath, arguments={'title': 'RENCI Translational Sciece simple queue API: Swagger v2'})
        addApi=False

    if addApi:
      app.add_api('swagger.yaml', arguments={'title': 'RENCI Translational Sciece simple queue API: Swagger v2'})

    return app

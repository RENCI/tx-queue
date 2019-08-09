#!/usr/bin/env python3

import sys
sys.path.append('../..')
import config.server.params as params

import connexion

from swagger_server import encoder

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    if params.basePath != "":
        app.add_api('swagger.yaml', base_path=params.basePath, arguments={'title': 'RENCI Translational Sciece simple queue API: Swagger v2'})
    else:
        app.add_api('swagger.yaml', arguments={'title': 'RENCI Translational Sciece simple queue API: Swagger v2'})
    if params.port != "":
        app.run(port=params.port)
    else:
        app.run()


if __name__ == '__main__':
    main()

from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.api import ModelRestApi
from flask_appbuilder.api import BaseApi, expose
from flask import request, Response
from . import appbuilder, db
from .models import Queue
from datetime import datetime

def dt_string():
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")


class GreetingApi(BaseApi):
    resource_name = "greeting"
    openapi_spec_methods = {
        "greeting": {
            "get": {
                "description": "Override description",
            }
        }
    }

    @expose('/')
    def greeting(self):
        """Send a greeting
        ---
        get:
          responses:
            200:
              description: Greet the user
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      message:
                        type: string
        """
        return self.response(200, message="Hello")


appbuilder.add_api(GreetingApi)


class QueusModelApi(ModelRestApi):
    resource_name = 'queue'
    datamodel = SQLAInterface(Queue)

    def post_headless(self):
        request_data = request.get_json()
        ip = request_data['ip']
        identity = request_data['identity']

#        print(SQLAInterface.query(Queue, ip=ip))

        if ip:
            entry = db.session.query(Queue).filter_by(ip=ip)
            if not entry.first():
                device = Queue(ip=ip, identity=identity, time=dt_string())
                db.session.add(device)
                db.session.commit()
            else:
                entry.update(dict(time=dt_string()))
                db.session.commit()
        else:
            print("ip is required")


appbuilder.add_api(QueusModelApi)
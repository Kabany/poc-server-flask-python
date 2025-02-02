from config import Config
from flask import Flask, jsonify

def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(config_class)

  from app.meta import bp as meta_bp

  app.register_blueprint(meta_bp)

  return app

def success_response(data, message: str = None):
  toSend = {"success": True}
  if data != None:
    toSend["data"] = data
  if message !=None:
    toSend["message"] = message
  return jsonify(toSend)
from flask import request

from app import success_response
from app.auth import bp
from app.auth.services import create_jwt_from_string, create_hash, create_totp

@bp.post("/auth/jwt/string")
def send_jwt_token():
  content = request.json
  message = create_jwt_from_string(content["message"])
  return success_response({"token": message}), 200

@bp.post("/auth/hash/string")
def send_hash():
  content = request.json
  message = create_hash(content["message"])
  return success_response({"hash": message}), 200

@bp.post("/auth/totp/string")
def send_totp_code():
  content = request.json
  message = create_totp(content["message"])
  return success_response({"code": message}), 200
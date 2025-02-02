from app import success_response
from app.meta import bp
from config import Config

@bp.get("/meta/ping")
def ping():
  return success_response(None, "pong!"), 200

@bp.get("/meta/health-check")
def health_check():
  return success_response(None, "ok!"), 200

@bp.get("/meta/version")
def version():
  return success_response(None, Config.VERSION), 200
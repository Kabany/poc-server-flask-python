from flask import request

from app import success_response
from app.operations import bp
from app.operations.services import create_list, fibonacci_sum, fibonacci_list

@bp.get("/operations/list/params/<int:times>")
def send_list_with_params(times):
  my_list = create_list(times)
  return success_response(my_list), 200

@bp.get("/operations/list/query")
def send_list_with_query():
  my_list = create_list(int(request.args.get("times")))
  return success_response(my_list), 200

@bp.post("/operations/list/body")
def send_list_with_body():
  content = request.json
  my_list = create_list(content["times"])
  return success_response(my_list), 200

@bp.get("/operations/list/headers")
def send_list_with_headers():
  my_list = create_list(int(request.headers.get("times")))
  return success_response(my_list), 200

@bp.get("/operations/fibonacci/sum/<int:number>")
def send_fibonacci_sum(number):
  fib = fibonacci_sum(number)
  return success_response({"sum": fib}), 200

@bp.get("/operations/fibonacci/list/<int:number>")
def send_fibonacci_list(number):
  fib = fibonacci_list(number)
  return success_response({"list": fib}), 200
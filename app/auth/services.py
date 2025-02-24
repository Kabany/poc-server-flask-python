from jwcrypto import jwt, jwk
import pyotp 
import json
import hashlib

FIRST_JWT_SECRET = "ThisIsAVeryLongStringToAlignWithTheIDX10720RequirementForDotNetWebApps"

def create_jwt_from_string(text: str):
  key = jwk.JWK().from_password(FIRST_JWT_SECRET)
  token = jwt.JWT(header={"alg": "HS256"}, claims={"message": text})
  token.make_signed_token(key)
  return token.serialize()

def validate_jwt_token(token: str):
  key = jwk.JWK().from_password(FIRST_JWT_SECRET)
  tok = jwt.JWT()
  tok.deserialize(token)
  tok.validate(key)
  return json.loads(tok.claims)["message"]

def create_hash(text):
  return hashlib.sha512(str.encode(text)).hexdigest()

def create_totp(text):
  totp = pyotp.TOTP(s=text, digits=8, digest="sha512", interval=30)
  return totp.now()
import unittest

from config import Config
from app import create_app
from app.auth.services import create_jwt_from_string, validate_jwt_token, create_hash, create_totp

class AuthTestConfig(Config):
  name = "AuthTest"
  pass

class AuthTest(unittest.TestCase):
  def setUp(self):
    self.app = create_app(AuthTestConfig)
    self.app_context = self.app.app_context()
    self.app_context.push()

  def tearDown(self):
    self.app_context.pop()

  def test_should_create_jwt_token_from_simple_string(self):
    message = "Hello World!"
    token = create_jwt_from_string(message)
    self.assertEqual("eyJhbGciOiJIUzI1NiJ9.eyJtZXNzYWdlIjoiSGVsbG8gV29ybGQhIn0.yX3llK_oxmp-qhJ7l-B0AL8wOlzCzsDHlw7xtCU2d4s", token)

  def test_should_create_jwt_token_then_decode_it(self):
    message = "Hello World!"
    token = create_jwt_from_string(message)
    decoded = validate_jwt_token(token)
    self.assertEqual(message, decoded)

    # From JavaScript, C# & Java/Kotlin
    decoded2 = validate_jwt_token("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZXNzYWdlIjoiSGVsbG8gV29ybGQhIn0.q_OAmeTO_BJ0X1_6SMzGEat8qHvcMZ6LtPhLg8yKXR4")
    self.assertEqual(message, decoded2)
    # From Swift
    decoded3 = validate_jwt_token("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZXNzYWdlIjoiSGVsbG8gV29ybGQhIn0.Qn62lWxZ5VZKovUbE8KTu_xGeDSp739uapAuBDK360Y")
    self.assertEqual(message, decoded3)

  def test_should_create_hash_using_sha512(self):
    message = "Hello World!"
    token = create_hash(message)
    self.assertEqual("861844d6704e8573fec34d967e20bcfef3d424cf48be04e6dc08f2bd58c729743371015ead891cc3cf1c9d34b49264b510751b1ff9e537937bc46b5d6ff4ecc8", token)

  def test_should_create_totp_token_from_string_using_sha512(self):
    message = "JBSWY3DPEHPK3PXP"
    token = create_totp(message)
    token2 = create_totp(message)
    self.assertEqual(token, token2)
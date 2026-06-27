from dotenv import load_dotenv
import os

load_dotenv()

# API Configuration
API_BASE_URL = os.getenv("API_BASE_URL", "")

# Authentication
USERNAME = os.getenv("USERNAME", "")
PASSWORD = os.getenv("PASSWORD", "")
MFA_CODE = os.getenv("MFA_CODE", "1234")

# Banking Test Data
ROUTING_NUMBER = os.getenv("ROUTING_NUMBER", "021000021")
ACCOUNT_NUMBER = os.getenv("ACCOUNT_NUMBER", "123456789012")

# Payment Test Data
CARDHOLDER_NAME = os.getenv("CARDHOLDER_NAME", "Munish Kumar")
CARD_NUMBER = os.getenv("CARD_NUMBER", "4242424242424242")
EXP_MONTH = int(os.getenv("EXP_MONTH", "12"))
EXP_YEAR = int(os.getenv("EXP_YEAR", "2027"))
CVC = os.getenv("CVC", "123")
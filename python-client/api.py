import requests
from exceptions import ApiError, AuthenticationError, ValidationError, RateLimitError


class OnsettoApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.token = None

    def _handle_response(self, response: requests.Response):
        if response.status_code in (401, 403):
            raise AuthenticationError(response.text)
        if response.status_code == 422:
            raise ValidationError(response.text)
        if response.status_code == 429:
            raise RateLimitError(response.text)
        if response.status_code >= 400:
            raise ApiError(response.text)

        return response.json()

    def login(self, username: str, password: str):
        response = self.session.post(
            f"{self.base_url}/auth/token",
            json={
                "email": username,
                "password": password,
            },
            timeout=20,
        )
        return self._handle_response(response)

    def verify_mfa(self, mfa_token: str, code: str):
        response = self.session.post(
            f"{self.base_url}/auth/mfa/verify",
            json={
                "mfa_token": mfa_token,
                "code": code,
            },
            timeout=20,
        )

        data = self._handle_response(response)
        self.token = data.get("access_token") or data.get("token")

        if not self.token:
            raise AuthenticationError("Bearer token missing from MFA response")

        self.session.headers.update({
            "Authorization": f"Bearer {self.token}"
        })

        return data

    def update_banking(self, routing_number: str, account_number: str):
        response = self.session.put(
            f"{self.base_url}/account/banking",
            json={
                "routing_number": routing_number,
                "account_number": account_number,
            },
            timeout=20,
        )
        return self._handle_response(response)

    def update_payment(
    self,
    cardholder_name: str,
    card_number: str,
    exp_month: int,
    exp_year: int,
    cvc: str,
):
     response = self.session.put(
        f"{self.base_url}/account/payment",
        json={
            "cardholder_name": cardholder_name,
            "card_number": card_number,
            "exp_month": exp_month,
            "exp_year": exp_year,
            "cvc": cvc,
        },
        timeout=20,
    )
     return self._handle_response(response)
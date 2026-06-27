from api import OnsettoApiClient
from config import (
    API_BASE_URL,
    USERNAME,
    PASSWORD,
    MFA_CODE,
    ROUTING_NUMBER,
    ACCOUNT_NUMBER,
    CARDHOLDER_NAME,
    CARD_NUMBER,
    EXP_MONTH,
    EXP_YEAR,
    CVC,
)
from exceptions import ApiError


def main():
    client = OnsettoApiClient(API_BASE_URL)

    try:
        print("Authenticating...")

        login_response = client.login(USERNAME, PASSWORD)

        mfa_token = (
            login_response.get("mfa_token")
            or login_response.get("token")
            or login_response.get("challenge_id")
        )

        if not mfa_token:
            raise ApiError(
                f"MFA token missing from login response: {login_response}"
            )

        client.verify_mfa(mfa_token, MFA_CODE)

        print("✓ Authentication successful")

        banking_response = client.update_banking(
            routing_number=ROUTING_NUMBER,
            account_number=ACCOUNT_NUMBER,
        )

        payment_response = client.update_payment(
            cardholder_name=CARDHOLDER_NAME,
            card_number=CARD_NUMBER,
            exp_month=EXP_MONTH,
            exp_year=EXP_YEAR,
            cvc=CVC,
        )

        print("\n=== Banking Updated Successfully ===")
        print(f"Routing Number : {banking_response['routing_masked']}")
        print(f"Account Number : {banking_response['account_masked']}")

        print("\n=== Payment Updated Successfully ===")
        print(f"Card Brand     : {payment_response['card_brand'].title()}")
        print(f"Card Ending    : ****{payment_response['last4']}")
        print(
            f"Expiry         : {payment_response['exp_month']}/{payment_response['exp_year']}"
        )

    except ApiError as error:
        print(f"\nAPI Error: {error}")

    except Exception as error:
        print(f"\nUnexpected Error: {error}")


if __name__ == "__main__":
    main()
import os
from http import HTTPStatus
from typing import Any

from dotenv import load_dotenv, set_key
from oauth2_client.credentials_manager import CredentialManager as DefaultCredentialManager, ServiceInformation
from requests import Response

load_dotenv()


class CredentialManager(DefaultCredentialManager):

    @staticmethod
    def _is_token_expired(response: Response) -> bool:
        if response.status_code == HTTPStatus.UNAUTHORIZED.value:
            try:
                json_data = response.json()
                return json_data.get('detail') == 'Authentication credentials were not provided.'
            except ValueError:
                return False
        else:
            return False

    def _process_token_response(self, token_response: dict, refresh_token_mandatory: bool) -> None:
        super()._process_token_response(token_response=token_response, refresh_token_mandatory=refresh_token_mandatory)
        # Update refresh_token in your database - replace this code with your own application logic
        set_key('.env', 'REFRESH_TOKEN', self.refresh_token)


class RentalReadyClient:

    def __init__(self) -> None:
        self.base_url = os.getenv('BASE_URL')
        client_id = os.getenv('CLIENT_ID')
        client_secret = os.getenv('CLIENT_SECRET')
        refresh_token = os.getenv('REFRESH_TOKEN')  # Obtain manually via e.g. cURL or Postman
        scopes = os.getenv('SCOPES').split(' ')
        service_information = ServiceInformation(
            'https://pms.rentalready.io/o/authorize/',
            'https://pms.rentalready.io/o/token/',
            client_id,
            client_secret,
            scopes,
        )
        self.manager = CredentialManager(service_information)
        self.manager.init_with_token(refresh_token=refresh_token)

    def _get(self, path: str) -> dict[str, Any]:
        response = self.manager.get(self.base_url + path)
        return response.json()

    def get_pricing(self) -> dict[str, Any]:
        return self._get('pricing/')

    def get_rentals(self) -> dict[str, Any]:
        return self._get('rentals/')

    def get_reservations(self) -> dict[str, Any]:
        return self._get('reservations/')

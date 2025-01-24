import requests
from time import sleep
_MYAPI_URL_: str = "https://cpmnuker.anasov.ly/api"


class CPMEwan1999:

    def __init__(self, access_key) -> None:
        self.auth_token = None
        self.access_key = access_key

    def login(self, email, password) -> int:
        payload = {"account_email": email, "account_password": password}
        params = {"key": self.access_key}
        response = requests.post(
            f"{_MYAPI_URL_}/account_login", params=params, data=payload
        )
        response_decoded = response.json()
        if response_decoded.get("ok"):
            self.auth_token = response_decoded.get("auth")
        return response_decoded.get("error")

    def register(self, email, password) -> int:
        payload = {"account_email": email, "account_password": password}
        params = {"key": self.access_key}
        response = requests.post(
            f"{_MYAPI_URL_}/account_register", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("error")

    def delete(self):
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        requests.post(f"{_MYAPI_URL_}/account_delete", params=params, data=payload)

    def get_player_data(self) -> any:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{_MYAPI_URL_}/get_data", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded

    def set_player_rank(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{_MYAPI_URL_}/set_rank", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def get_key_data(self) -> any:
        params = {"key": self.access_key}
        response = requests.get(f"{_MYAPI_URL_}/get_key_data", params=params)
        response_decoded = response.json()
        return response_decoded

    def set_player_money(self, amount) -> bool:
        payload = {"account_auth": self.auth_token, "amount": amount}
        params = {"key": self.access_key}
        response = requests.post(
            f"{_MYAPI_URL_}/set_money", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def set_player_coins(self, amount) -> bool:
        payload = {"account_auth": self.auth_token, "amount": amount}
        params = {"key": self.access_key}
        response = requests.post(
            f"{_MYAPI_URL_}/set_coins", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def set_player_name(self, name) -> bool:
        payload = {"account_auth": self.auth_token, "name": name}
        params = {"key": self.access_key}
        response = requests.post(f"{_MYAPI_URL_}/set_name", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def set_player_localid(self, id) -> bool:
        payload = {"account_auth": self.auth_token, "id": id}
        params = {"key": self.access_key}
        response = requests.post(f"{_MYAPI_URL_}/set_id", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def set_player_plates(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{_MYAPI_URL_}/set_plates", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def get_player_car(self, car_id) -> any:
        payload = {"account_auth": self.auth_token, "car_id": car_id}
        params = {"key": self.access_key}
        response = requests.post(f"{_MYAPI_URL_}/get_car", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def delete_player_friends(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{_MYAPI_URL_}/delete_friends", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_w16(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{_MYAPI_URL_}/unlock_w16", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_horns(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{_MYAPI_URL_}/unlock_horns", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def disable_engine_damage(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{_MYAPI_URL_}/disable_damage", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlimited_fuel(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{_MYAPI_URL_}/unlimited_fuel", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def set_player_wins(self, amount) -> bool:
        payload = {"account_auth": self.auth_token, "amount": amount}
        params = {"key": self.access_key}
        response = requests.post(
            f"{_MYAPI_URL_}/set_race_wins", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def set_player_loses(self, amount) -> bool:
        payload = {"account_auth": self.auth_token, "amount": amount}
        params = {"key": self.access_key}
        response = requests.post(
            f"{_MYAPI_URL_}/set_race_loses", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_houses(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{_MYAPI_URL_}/unlock_houses", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_smoke(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{_MYAPI_URL_}/unlock_smoke", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_paid_cars(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{_MYAPI_URL_}/unlock_paid_cars", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_all_cars(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{_MYAPI_URL_}/unlock_all_cars", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_all_cars_siren(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{_MYAPI_URL_}/unlock_all_cars_siren", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def account_clone(self, account_email, account_password) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "account_email": account_email,
            "account_password": account_password,
        }
        params = {"key": self.access_key}
        response = requests.post(f"{_MYAPI_URL_}/clone", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def hack_car_speed(self, car_id):
        payload = {"account_auth": self.auth_token, "car_id": car_id}
        params = {"key": self.access_key}
        response = requests.post(
            f"{_MYAPI_URL_}/hack_car_speed", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def hack_car_sexo(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{_MYAPI_URL_}/hack_car_sexo", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")                
        
    def chrome_all_cars(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{_MYAPI_URL_}/chrome_all_cars", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")                        
        
    def hack_car_milage(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{_MYAPI_URL_}/hack_car_milage", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")                                

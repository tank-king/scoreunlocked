import json

import requests


class Client:
    def __init__(self,
                 timeout: float = 5.0,
                 parse_json: bool = True,
                 endpoint: str = 'https://scoreunlocked.pythonanywhere.com',
                 raise_errors: bool = False
                 ):
        self._developer = None
        self._leaderboard = None
        self._timeout = timeout
        self._parse_json = parse_json
        self.raise_errors = raise_errors
        self._base_endpoint = endpoint
        self._get_endpoint = f'{self._base_endpoint}/leaderboards/get'
        self._post_endpoint = f'{self._base_endpoint}/leaderboards/post'

    def connect(self, developer: str, leaderboard: str):
        self._developer = developer
        self._leaderboard = leaderboard

    def parse_response(self, response: str):
        if self._parse_json:
            try:
                return json.loads(response)
            except json.JSONDecodeError:
                return response
        else:
            return response

    def get_server_status(self):
        try:
            if requests.get(self._base_endpoint, timeout=self._timeout).status_code == 200:
                return True
            else:
                return False
        except requests.ReadTimeout:
            return False
        except Exception as e:
            if self.raise_errors:
                raise e
            print(f'An Error Occurred: {e}')
            return False

    def _get_leaderboard(self):
        params = {
            'developer': self._developer,
            'leaderboard': self._leaderboard
        }
        response = requests.get(self._get_endpoint,
                                params=params,
                                timeout=self._timeout
                                )
        parsed_response = self.parse_response(response.text)
        try:
            if parsed_response.get('error'):
                return parsed_response
                # if parsed_response.get('message'):
                #     print(parsed_response.get('message'), ':', parsed_response.get('error').get('message'))
                #     return None
            else:
                if parsed_response.get('leaderboard') is not None:
                    return parsed_response.get('leaderboard')
        except AttributeError:
            return None

    def get_leaderboard(self):
        if self.raise_errors:
            return self._get_leaderboard()
        else:
            try:
                return self._get_leaderboard()
            except requests.ReadTimeout:
                return None
            except Exception as e:
                print(f'An Error Occurred: {e}')
                return None

    def _post_score(self, name, score, validation_data=''):
        data = {
            'developer': self._developer,
            'leaderboard': self._leaderboard,
            'name': name,
            'score': score,
            'validation_data': validation_data
        }
        try:
            response = requests.post(self._post_endpoint,
                                     data=data,
                                     timeout=self._timeout
                                     )
            return self.parse_response(response.text)
        except requests.ReadTimeout:
            return None
        except requests.ConnectionError:
            print('connection error')
        except Exception as e:
            print(f'An Error Occurred: {e}')
            return None

    def post_score(self, name, score, validation_data=''):
        if self.raise_errors:
            return self._post_score(name, score, validation_data)
        else:
            try:
                return self._post_score(name, score, validation_data)
            except requests.ReadTimeout:
                return None
            except Exception as e:
                print(f'An Error Occurred: {e}')
                return None

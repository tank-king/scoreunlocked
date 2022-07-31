import threading

from .scoreunlocked_client import Client
from typing import Union


class ClientThread(threading.Thread):

    """
    This thread is useful to have a constantly updated leaderboard, without constantly pausing the program.
    Also, the post requests won't pause the program too.
    As the requests take time, you'll though have to wait about ~2 seconds after a post request to see it appear in the
    leaderboard.

    It is a daemon thread, so you don't have to worry on closing it when stopping your program, as it will be stopped
    if all the non-daemon threads stop (in your case, your main thread).

    Its usage is the same as a normal client, simply the get and post method don't pause your program.
    """

    def __init__(self,
                 timeout: float = 5.0,
                 parse_json: bool = True,
                 endpoint: str = 'https://scoreunlocked.pythonanywhere.com',
                 raise_errors: bool = False
                 ) -> None:
        # init the Thread class
        super().__init__()

        # init the client
        self.client = Client(timeout=timeout, parse_json=parse_json, endpoint=endpoint, raise_errors=raise_errors)

        # Thread states
        self.running = True  # the thread is running
        self.daemon = True  # the thread is a daemon-thread
        self.connected = False  # the client is connected

        # the updated leaderboard
        self.current_leader_board = []
        # the queue for posting new scores
        self.score_to_post = []

        # start the thread at initialization
        self.start()

    def connect(self, developer: str, leaderboard: str) -> None:
        """
        Connect the client to the server.
        :param developer: The name of the developer owning the leaderboard (str)
        :param leaderboard: The name of the leaderboard (str)
        :return: None
        """
        self.connected = True
        self.client.connect(developer=developer, leaderboard=leaderboard)

    def disconnect(self) -> None:
        """
        Exit the thread, and therefore delete the client.
        :return: None
        """
        self.running = False
        del self.client

    def update_leaderboard(self) -> None:
        """
        Updates the leaderboard.
        :return: None
        """
        self.current_leader_board = self.client.get_leaderboard()

    def get_leaderboard(self) -> list:
        """
        Get the updated leaderboard.
        :return: The leaderboard (list)
        """
        return self.current_leader_board

    def post_score(self, name: str, score: Union[int, float], validation_data='') -> None:
        """
        Append a new score to the post queue.
        :param name: Name of the user (str)
        :param score: Posted score (int or float if float is enabled in the leaderboard settings)
        :param validation_data: ? (str)
        :return: None
        """
        self.score_to_post.append([name, score, validation_data])

    def run(self) -> None:
        """
        The main loop of the Thread.
        :return: None
        """

        while self.running:

            if self.connected:
                # if the client is connected, update the leaderboard
                self.update_leaderboard()

                # post every score present in the queue, and then empty it
                for score in self.score_to_post:
                    self.client.post_score(*score)
                self.score_to_post = []

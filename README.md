# Package for ScoreUnlocked API

This is a simple package for using the 
[ScoreUnlocked](https://scoreunlocked.pythonanywhere.com) 
Leaderboard System. <br>

If you have not done already, you can click [here](https://scoreunlocked.pythonanywhere.com/users/register)
to create a ScoreUnlocked developer account

You can use this package by installing it from PyPi. To do so, type the following in the terminal:

```commandline
pip install scoreunlocked
```

Once ScoreUnlocked is installed, you can use it as: <br>
```python
import scoreunlocked

client = scoreunlocked.Client()  # instantiating the client
client.connect('developer_name', 'leaderboard_name')

# to get leaderboard from server [returns None if not found or errors occurred]
client.get_leaderboard()

# to post a score to the server
client.post_score(name='name', score=100, validation_data='<data to validate score>') 
```

That's all you need to know for setting up a basic leaderboard.

# Advanced Tutorial

[TODO]

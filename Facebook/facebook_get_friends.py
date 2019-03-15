import os
import facebook
import json

if __name__ == '__main__':
    token = "EAADlZCi32wJQBALp8CKXNZCwGh8mffxAONDloZA4hSYX3u0pd079cM3yguInlcQkfkHfo7vnybrv9xdyyJk2b39MBX7924kPzUAI7El1t5qQZCg0hjWDOmJ5raLI2ZB0FAZCZCdMZA2XrP6RzcX6OuNFjfS5hs1TJ0v0tdvH20EDJqQwwJz4rjchQLHmPMfK2AKXGn7wpr1XEZCR8EzG3N7cc"

    graph = facebook.GraphAPI(token)
    user = graph.get_object("me")
    friends = graph.get_connections(user["id"], "friends")
    print(json.dumps(friends, indent=4))

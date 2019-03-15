import os
import json
import facebook
import requests


if __name__ == '__main__':
    token = "EAADlZCi32wJQBALp8CKXNZCwGh8mffxAONDloZA4hSYX3u0pd079cM3yguInlcQkfkHfo7vnybrv9xdyyJk2b39MBX7924kPzUAI7El1t5qQZCg0hjWDOmJ5raLI2ZB0FAZCZCdMZA2XrP6RzcX6OuNFjfS5hs1TJ0v0tdvH20EDJqQwwJz4rjchQLHmPMfK2AKXGn7wpr1XEZCR8EzG3N7cc"

    graph = facebook.GraphAPI(token)
    all_fields = [
        'message',
        'created_time',
        'description',
        'caption',
        'link',
        'place',
        'status_type',
        'message_tags',
        'picture',
        'privacy',
        'properties',
        'story_tags',
        'from',
        'to',
        'with_tags'
    ]
    all_fields = ','.join(all_fields)
    posts = graph.get_connections('me', 'posts', fields=all_fields)

    while True:  # keep paginating
        try:
            with open('my_posts.jsonl', 'a') as f:
                for post in posts['data']:
                    f.write(json.dumps(post)+"\n")
                # get next page
                posts = requests.get(posts['paging']['next']).json()
        except KeyError:
            # no more pages, break the loop
            break

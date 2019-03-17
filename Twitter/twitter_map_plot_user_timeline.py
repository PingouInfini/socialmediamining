import sys
import folium
import time
from tweepy import Cursor
from twitter_client import get_twitter_client
from folium.plugins import MarkerCluster
from geopy import geocoders

# dico of already resolved {location : coord}
resolved_locations = {}


def usage():
    print("Usage:")
    print("python {} <username> <filename.html>".format(sys.argv[0]))


def create_clustered_map():
    # create map
    tweet_map = folium.Map(location=[50, 5],
                           zoom_start=3,
                           tiles='Stamen Terrain')
    marker_cluster = MarkerCluster().add_to(tweet_map)

    # get tweet from user timeline and plot them in map
    for page in Cursor(client.user_timeline, screen_name=user, count=200).pages(16):
        for status in page:
            tweet = status._json

            if tweet['coordinates'] is not None:
                lng = tweet['coordinates']['coordinates'][0]
                lat = tweet['coordinates']['coordinates'][1]
                # prepare popup to show for each marker (content = tweet)
                html_popup = create_html_popup(lat, lng, tweet)
                # create markers and add them to the map
                folium.Marker([lat, lng], popup=html_popup).add_to(marker_cluster)
            elif tweet['place'] is not None:
                # relevance-based search by location and name
                (lat, lng) = geodecode(tweet['place']['full_name'])
                if lat == 0 and lng == 0:
                    # relevance-based search by different location and name values
                    (lat, lng) = geodecode(tweet['contributors'], ['coordinates'])
                    if lat == 0 and lng == 0:
                        pass

                # prepare popup to show for each marker (content = tweet)
                html_popup = create_html_popup(lat, lng, tweet)
                # create markers and add them to the map
                folium.Marker([lat, lng], popup=html_popup).add_to(marker_cluster)
            else:
                pass

    tweet_map.save(outputfile)


def create_html_popup(lat, lng, tweet):
    html = """
    <div class="content" style="font-family:Segoe UI,Arial,sans-serif">
        <div style="padding-bottom: 10px">
            <strong>{}</strong><span>&nbsp;</span><span style="color:#657786;">@{} - {}</span></a>
            <br/>{}
        </div>
        {}
        <div>
            <span style="color:#657786;">depuis </span> <span style="color:#0084b4;">{}{}</span>
        </div>
    </div>
    """

    html_popup = html.format(tweet['user']['name'], tweet['user']['screen_name'], date_beautifier(tweet['created_at']),
                             tweet['text'],
                             add_media_if_exists(tweet), tweet['place']['full_name'],
                             " [" + str(lng) + "," + str(lat) + "]")
    return html_popup


def date_beautifier(created_at):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(created_at, '%a %b %d %H:%M:%S +0000 %Y'))


def add_media_if_exists(tweet):
    medias = ""

    media_div = """
    <div style="padding-bottom: 10px">
    <img style="width:250px;"
    src="{}"
    alt="img" />
    </div>
    """

    try:
        for media in tweet['entities']['media']:
            media_url = media['media_url']
            # TODO: we can get media and store them from this <media_url>
            medias += media_div.format(media_url)

        return medias
    except:
        # pas de media...
        return ""


def geodecode(location):
    # check if location already resolved
    if location in resolved_locations:
        loc = resolved_locations.get(location, "none")
    else:
        g = geocoders.Nominatim(user_agent="testmyspecificCustomTestamoi")
        loc = g.geocode(location, timeout=10)
        # store location and coord
        resolved_locations[location] = loc

    return loc.latitude, loc.longitude


if __name__ == '__main__':
    if len(sys.argv) != 3:
        usage()
        sys.exit(1)
    user = sys.argv[1]
    outputfile = sys.argv[2]
    client = get_twitter_client()

    # get tweet from timeline, and create a map with tweet + coordinates
    create_clustered_map()

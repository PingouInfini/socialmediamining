import sys
import json
import folium
from tweepy import Cursor
from twitter_client import get_twitter_client
from folium.plugins import MarkerCluster
from folium import plugins


def usage():
    print("Usage:")
    print("python {} <username> <filename.html>".format(sys.argv[0]))


def make_geojson_from_user_timeline():
    for page in Cursor(client.user_timeline, screen_name=user, count=200).pages(16):
        for status in page:
            tweet = status._json
            try:
                if tweet['coordinates']:
                    geo_json_feature = {
                        "type": "Feature",
                        "geometry": {
                            "type": "Point",
                            "coordinates": tweet['coordinates']['coordinates']
                        },
                        "properties": {
                            "text": tweet['text'],
                            "created_at": tweet['created_at']
                        }
                    }
                    geo_data['features'].append(geo_json_feature)
            except KeyError:
                continue


def plot_location_in_clustered_map():
    tweet_map = folium.Map(location=[50, 5],
                           zoom_start=3,
                           tiles='Stamen Terrain')
    marker_cluster = MarkerCluster().add_to(tweet_map)
    geojson_layer = folium.GeoJson(data=geo_data,
                                   name='geojson')
    geojson_layer.add_to(marker_cluster)
    tweet_map.save(outputfile)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        usage()
        sys.exit(1)
    user = sys.argv[1]
    outputfile = sys.argv[2]
    client = get_twitter_client()

    geo_data = {
        "type": "FeatureCollection",
        "features": []
    }

    # get tweet from timeline, and create a [geojson feature] with tweet coordinates
    make_geojson_from_user_timeline()
    # plot locations in a clustered map
    plot_location_in_clustered_map()

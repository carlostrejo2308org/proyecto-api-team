from connection import APIConnection

import requests
import datetime


class DeezerUserStats:
    def __init__(self):
        api_connection = APIConnection()
        self.__network = api_connection.get_network()

    def get_top_tracks(self, **kwargs):
        user_top_tracks = self.__network.get_authenticated_user().get_top_tracks(**kwargs)
        top_tracks = []

        for user_top_track in user_top_tracks:
            top_track = {}
            track = user_top_track.item

            top_track["track"] = track.get_name()
            top_track["artist"] = track.artist.get_name()
            top_track["playcount"] = track.get_userplaycount()
            top_tracks.append(top_track)

        return top_tracks

    def get_top_artists(self, **kwargs):
        user_top_artists = self.__network.get_authenticated_user().get_top_artists(**kwargs)
        top_artists = []

        for user_top_artist in user_top_artists:
            top_artist = {}
            artist = user_top_artist.item
            top_artist["artists"] = artist.get_name()
            top_artist["playcount"] = user_top_artist.weight
            top_artists.append(top_artist)

        return top_artists

    def __get_track_duration(self, track, artist):
        query = f"q=artist:\"{artist}\"track:\"{track}\""
        URL = "https://api.deezer.com/search?" + query
        request = requests.get(URL)
        track_data = request.json()["data"][0]
        total_duration = datetime.timedelta(seconds=track_data["duration"])

        return total_duration

    def get_total_time_listened(self, **kwargs):
        top_tracks = self.get_top_tracks(**kwargs)
        track_durations = []

        for top_track in top_tracks:
            track_duration = self.__get_track_duration(
                top_track["track"], top_track["artist"])
            track_durations.append(track_duration)

        total_time_listened = sum(track_durations, datetime.timedelta())
        return total_time_listened

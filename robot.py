from google_play_scraper import Sort, reviews_all
from app_store_scraper import AppStore


class Robot:
    def __init__(self, name, playstore_id, appstore_id):
        self.name = name
        self.playstore_id = playstore_id
        self.appstore_id = appstore_id

    def get_playstore_reviews(self):
        result = reviews_all(
            app_id=self.playstore_id,
            sleep_milliseconds=0,
            lang="ko",
            country="kr",
            sort=Sort.MOST_RELEVANT,
            filter_score_with=5,
        )
        return result

    def get_appstore_reviews(self):
        result = AppStore(
            app_name=self.name, app_id=self.appstore_id, country="kr"
        ).review()
        return result

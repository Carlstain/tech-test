import time

from moviesmanager import celery_app


@celery_app.task(bind=True, ignore_result=True)
def process_review(self):
    time.sleep(10)

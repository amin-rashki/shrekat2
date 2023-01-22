from celery import shared_task


@shared_task
def find_expiration_records():
    print("hiii this is a celery task")

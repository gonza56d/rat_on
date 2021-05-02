
# Python
from datetime import timedelta

# Celery App
from celery import group
from celery.decorators import periodic_task

# App
from .celery import app as celery_app
from rat_on.services.dummies import ServiceDummy
from rat_on.services.functions import hit_service


@celery_app.task(bind=True)
def hit_services_task(dummy: ServiceDummy) -> None:
    hit_service(dummy)


@periodic_task(run_every=timedelta(seconds=20))
def hit_services_periodic_task() -> None:
    jobs = group(hit_services_task.s(dummy) for dummy in ServiceDummy.get_all())
    jobs.apply_async()

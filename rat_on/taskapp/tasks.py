
# Python
from datetime import timedelta

# Celery App
from celery.decorators import periodic_task

# App
from rat_on.services.dummies import ServiceDummy
from rat_on.services.functions import hit_service


@periodic_task(run_every=timedelta(seconds=20))
def hit_services_periodic_task() -> None:
    for dummy in ServiceDummy.get_all():
        hit_service(dummy) 

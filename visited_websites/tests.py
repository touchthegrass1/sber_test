import uuid
from datetime import datetime

from django.test import TestCase
from pytz import timezone

from rest_framework.test import APIClient

from visited_websites.models import VisitedLinks


class ModelsTestCase(TestCase):
    def setUp(self):
        self.time_from = datetime.now(tz=timezone('Europe/Moscow'))
        self.device_id = uuid.uuid4()

        visited_links = [
            {"device_id": self.device_id, "link": "https://ya.ru/"},
            {"device_id": self.device_id, "link": "https://ya.ru/search/?text=мемы+с+котиками"},
            {"device_id": self.device_id, "link": "https://sber.ru"}
        ]
        VisitedLinks.objects.bulk_create([VisitedLinks(**item) for item in visited_links])

    def test_get_domains(self):
        time_to = datetime.now(tz=timezone('Europe/Moscow'))
        domains = VisitedLinks.get_visited_domains(self.device_id, self.time_from, time_to)
        assert sorted(domains) == ["sber.ru", "ya.ru"]


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.time_from = datetime.now(tz=timezone('Europe/Moscow'))

    def test_get_visited_domains(self):
        response = self.client.post("/api/xops/visited_links", data={
            "links": [
                "https://ya.ru/",
                "https://ya.ru/search/?text=мемы+с+котиками",
                "https://sber.ru"
            ]
        }, format="json")

        assert response.status_code == 200
        assert response.data == {"status": "ok"}

        time_to = datetime.now(tz=timezone('Europe/Moscow'))
        response = self.client.get("/api/xops/visited_domains", {
            "from": self.time_from.timestamp(),
            "to": time_to.timestamp()
        })

        assert response.status_code == 200
        assert sorted(response.data["domains"]) == ["sber.ru", "ya.ru"]

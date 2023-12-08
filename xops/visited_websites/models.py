from django.db import models

from urllib.parse import urlparse


class VisitedLinks(models.Model):
    device_id = models.UUIDField(editable=False)
    link = models.URLField(blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_visited_domains(cls, device_id, from_, to):
        visited_links = VisitedLinks.objects.filter(
            device_id=device_id
        ).exclude(
            timestamp__gt=to
        ).exclude(
            timestamp__lt=from_
        )

        domains = set()
        for link in visited_links:
            domain = urlparse(link.link).netloc
            domains.add(domain)

        return list(domains)

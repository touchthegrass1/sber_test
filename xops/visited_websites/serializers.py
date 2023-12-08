from rest_framework import serializers

from visited_websites.models import VisitedLinks


class LinksListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        visited_links = [VisitedLinks(**item) for item in validated_data]
        return VisitedLinks.objects.bulk_create(visited_links)


class LinksSerializer(serializers.Serializer):
    device_id = serializers.UUIDField()
    link = serializers.URLField()

    class Meta:
        list_serializer_class = LinksListSerializer

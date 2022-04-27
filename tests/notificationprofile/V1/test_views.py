from django.urls import reverse
from django.test import tag

from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.test import APITestCase

from argus.incident.serializers import IncidentSerializer
from argus.notificationprofile.models import (
    Filter,
    NotificationProfile,
    Timeslot,
)
from argus.util.testing import disconnect_signals, connect_signals

from .. import IncidentAPITestCaseHelper


@tag("API", "integration")
class ViewTests(APITestCase, IncidentAPITestCaseHelper):
    def setUp(self):
        disconnect_signals()
        super().init_test_objects()

        incident1_json = IncidentSerializer([self.incident1], many=True).data
        self.incident1_json = JSONRenderer().render(incident1_json)

        self.timeslot1 = Timeslot.objects.create(user=self.user1, name="Never")
        self.timeslot2 = Timeslot.objects.create(user=self.user1, name="Never 2: Ever-expanding Void")
        filter1 = Filter.objects.create(
            user=self.user1,
            name="Critical incidents",
            filter_string=f'{{"sourceSystemIds": [{self.source1.pk}]}}',
        )
        self.notification_profile1 = NotificationProfile.objects.create(user=self.user1, timeslot=self.timeslot1)
        self.notification_profile1.filters.add(filter1)
        self.notification_profile1.destinations.set(self.user1.destinations.all())
        self.media_v1 = []
        self.phone_number = None
        if self.notification_profile1.destinations.filter(media__slug="email").exists():
            self.media_v1.append("EM")
        if self.notification_profile1.destinations.filter(media__slug="sms").exists():
            self.media_v1.append("SM")
            self.phone_number = (
                self.notification_profile1.destinations.filter(media__slug="sms")
                .order_by("pk")
                .first()
                .settings["phone_number"]
            )

    def teardown(self):
        connect_signals()

    def test_incidents_filtered_by_notification_profile_view(self):
        response = self.user1_rest_client.get(
            reverse("v1:notification-profile:notificationprofile-incidents", args=[self.notification_profile1.pk])
        )
        response.render()
        self.assertEqual(response.content, self.incident1_json)

    # TODO: test more endpoints

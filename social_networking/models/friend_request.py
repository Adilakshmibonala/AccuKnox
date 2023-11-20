import uuid

from django.db import models
from social_networking.constants.enums import FriendRequestStatus
from social_networking.models.user import User


class FriendRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    from_user = models.ForeignKey(User, related_name='sent_requests', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='received_requests', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=FriendRequestStatus.get_list_of_tuples(),
                              default=FriendRequestStatus.PENDING.value)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"FriendRequest - {self.id}"

import resend
from resend.exceptions import NoContentError
from tests.conftest import ResendBaseTest

# flake8: noqa


class TestResendBroadcasts(ResendBaseTest):
    def test_broadcasts_create(self) -> None:
        self.set_mock_json({"id": "49a3999c-0ce1-4ea6-ab68-afcd6dc2e794"})

        params: resend.Broadcasts.CreateParams = {
            "audience_id": "78b8d3bc-a55a-45a3-aee6-6ec0a5e13d7e",
            "from": "hi@example.com",
            "subject": "Hello, world!",
            "name": "Python SDK Broadcast",
        }
        broadcast = resend.Broadcasts.create(params)
        assert broadcast["id"] == "49a3999c-0ce1-4ea6-ab68-afcd6dc2e794"

    def test_broadcasts_get(self) -> None:
        self.set_mock_json(
            {
                "object": "broadcast",
                "id": "559ac32e-9ef5-46fb-82a1-b76b840c0f7b",
                "name": "Announcements",
                "audience_id": "78261eea-8f8b-4381-83c6-79fa7120f1cf",
                "from": "Acme <onboarding@resend.dev>",
                "subject": "hello world",
                "reply_to": None,
                "preview_text": "Check out our latest announcements",
                "status": "draft",
                "created_at": "2024-12-01T19:32:22.980Z",
                "scheduled_at": None,
                "sent_at": None,
            }
        )

        broadcast = resend.Broadcasts.get(id="559ac32e-9ef5-46fb-82a1-b76b840c0f7b")
        assert broadcast["id"] == "559ac32e-9ef5-46fb-82a1-b76b840c0f7b"
        assert broadcast["name"] == "Announcements"
        assert broadcast["audience_id"] == "78261eea-8f8b-4381-83c6-79fa7120f1cf"
        assert broadcast["from"] == "Acme <onboarding@resend.dev>"
        assert broadcast["subject"] == "hello world"
        assert broadcast["reply_to"] is None
        assert broadcast["preview_text"] == "Check out our latest announcements"
        assert broadcast["status"] == "draft"
        assert broadcast["created_at"] == "2024-12-01T19:32:22.980Z"
        assert broadcast["scheduled_at"] is None
        assert broadcast["sent_at"] is None

    def test_broadcasts_send(self) -> None:
        self.set_mock_json({"id": "49a3999c-0ce1-4ea6-ab68-afcd6dc2e791"})

        params: resend.Broadcasts.SendParams = {
            "broadcast_id": "49a3999c-0ce1-4ea6-ab68-afcd6dc2e794",
        }
        broadcast = resend.Broadcasts.send(params)
        assert broadcast["id"] == "49a3999c-0ce1-4ea6-ab68-afcd6dc2e791"

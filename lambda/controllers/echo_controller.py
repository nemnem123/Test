import json
from core.responses import build_response
from services.echo_service import EchoService

class EchoController:
    def __init__(self):
        self.service = EchoService()

    def handle_post(self, event):
        try:
            body = json.loads(event.get("body", "{}"))
        except json.JSONDecodeError:
            return build_response(400, {"message": "Invalid JSON format"})
        
        item_id, item = self.service.create_echo(body)
        return build_response(201, {"message": "Created", "id": item_id, "data": body})

    def handle_get(self, event):
        items = self.service.get_all_echos()
        return build_response(200, {"items": items})

    def handle_delete(self, event):
        try:
            body = json.loads(event.get("body", "{}"))
        except json.JSONDecodeError:
            return build_response(400, {"message": "Invalid JSON format"})
        
        item_id = body.get("id")
        if not item_id:
            return build_response(400, {"message": "Missing 'id' in request body"})
        
        self.service.delete_echo(item_id)
        return build_response(200, {"message": f"Deleted item {item_id}"})
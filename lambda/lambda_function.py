from core.responses import build_response
from controllers.echo_controller import EchoController

# Khởi tạo controller ở ngoài handler để tận dụng warm-start của Lambda
echo_controller = EchoController()

def lambda_handler(event, context):
    try:
        # Xử lý prefix /dev
        path = event.get("rawPath", "")
        if path.startswith("/dev"):
            path = path.replace("/dev", "", 1)
            
        method = event.get("requestContext", {}).get("http", {}).get("method", "")

        # Router cho /hello
        if method == "GET" and path == "/hello":
            return build_response(200, {"message": "Hello from API"})

        # Router cho /echo
        if path == "/echo":
            if method == "POST":
                return echo_controller.handle_post(event)
            elif method == "GET":
                return echo_controller.handle_get(event)
            elif method == "DELETE":
                return echo_controller.handle_delete(event)

        # Fallback
        return build_response(404, {"message": "Endpoint not found"})

    except Exception as e:
        return build_response(500, {"error": "Internal Server Error", "details": str(e)})
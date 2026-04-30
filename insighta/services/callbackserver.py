from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class OAuthHandler(BaseHTTPRequestHandler):
    auth_code = None
    auth_state = None

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed.query)

        OAuthHandler.auth_code = query.get("code", [None])[0]
        OAuthHandler.auth_state = query.get("state", [None])[0]

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Login successful. You can close this window.")

def start_server(port=8000):
    server = HTTPServer(("localhost", port), OAuthHandler)
    print(f"Listening on http://localhost:{port}/callback")
    server.handle_request()  # handle one request only
    return OAuthHandler.auth_code, OAuthHandler.auth_state
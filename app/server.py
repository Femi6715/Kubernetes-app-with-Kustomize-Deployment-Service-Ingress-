from http.server import BaseHTTPRequestHandler, HTTPServer
import socket, os, json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps({
            "app":"k8s-python-app",
            "host": socket.gethostname(),
            "path": self.path,
            "env": {k:v for k,v in os.environ.items() if k.startswith("APP_")}
        }).encode()
        self.send_response(200)
        self.send_header("Content-Type","application/json")
        self.end_headers()
        self.wfile.write(body)

if __name__ == "__main__":
    port = int(os.getenv("PORT","8080"))
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()

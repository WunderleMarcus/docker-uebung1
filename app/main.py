from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os


HOST = "0.0.0.0"
PORT = int(os.getenv("PORT", "8000"))


class RequestHandler(BaseHTTPRequestHandler):

    def send_json_response(self, status_code, data):
        response = json.dumps(
            data,
            ensure_ascii=False
        ).encode("utf-8")

        self.send_response(status_code)

        self.send_header(
            "Content-Type",
            "application/json; charset=utf-8"
        )

        self.send_header(
            "Content-Length",
            str(len(response))
        )

        self.end_headers()

        self.wfile.write(response)

    def send_html_file(self):
        try:
            with open(
                "app/index.html",
                "rb"
            ) as file:

                content = file.read()

            self.send_response(200)

            self.send_header(
                "Content-Type",
                "text/html; charset=utf-8"
            )

            self.send_header(
                "Content-Length",
                str(len(content))
            )

            self.end_headers()

            self.wfile.write(content)

        except FileNotFoundError:

            self.send_json_response(
                500,
                {
                    "error": "index.html wurde nicht gefunden"
                }
            )

    def do_GET(self):

        if self.path == "/":

            self.send_html_file()

        elif self.path == "/health":

            self.send_json_response(
                200,
                {
                    "status": "ok",
                    "application": "python-docker-app"
                }
            )

        else:

            self.send_json_response(
                404,
                {
                    "error": "Not Found"
                }
            )

    def log_message(
        self,
        format,
        *args
    ):

        print(
            f"{self.address_string()} - "
            f"{format % args}"
        )


def main():

    server = HTTPServer(
        (HOST, PORT),
        RequestHandler
    )

    print(
        f"Server läuft auf "
        f"http://localhost:{PORT}"
    )

    server.serve_forever()


if __name__ == "__main__":

    main()
import BaseHTTPServer
import cases

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    Cases = [cases.case_no_file(),
            cases.case_cgi_file(),
            cases.case_existing_file(),
            cases.case_directory_index_file(),
            cases.case_directory_no_index_file(),
            cases.case_always_fail()
			]

    # How to display an error.
    Error_Page = """\
        <html>
        <body>
        <h1>Error accessing {path}</h1>
        <p>{msg}</p>
        </body>
        </html>
        """

    # Classify and handle request.
    def do_GET(self):
        try:

            # Figure out what exactly is being requested.
            self.full_path = os.getcwd() + self.path
			print os.getcwd()
			print self.path
            # Figure out how to handle it.
            for case in self.Cases:
                if case.test(self):
                    case.act(self)
                    break

        # Handle errors.
        except Exception as msg:
            self.handle_error(msg)

    # Handle unknown objects.
    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content, 404)

    # Send actual content.
    def send_content(self, content, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

if __name__=="__main__":
	server_address=('',8080)
	server=BaseHTTPServer.HTTPServer(server_address,RequestHandler)
	server.serve_forever()

import BaseHTTPServer
import os.path
    
class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    
##    def __init__(self, page):
##        self.page=page
    Page = '''\
<html>
<body>
<table>
<tr>  <td>Header</td>         <td>Value</td>          </tr>
<tr>  <td>Date and time</td>  <td>{date_time}</td>    </tr>
<tr>  <td>Client host</td>    <td>{client_host}</td>  </tr>
<tr>  <td>Client port</td>    <td>{client_port}s</td> </tr>
<tr>  <td>Command</td>        <td>{command}</td>      </tr>
<tr>  <td>Path</td>           <td>{path}</td>         </tr>
</table>
</body>
</html>
'''

    Error_Page = '''\
<html>
<body>
<h1>Error accessing {path}</h1>
<p>{msg}</p>
</body>
</html>
'''
 
    def create_Page(self):
        values={'date_time':self.date_time_string(),
                'client_host':self.client_address[0],
                'client_port':self.client_address[1],
                'command':self.command,
                'path':self.path

            }
        page=self.Page.format(**values)
        return page
    def send_Page(self,page):
        self.send_response(200)
        self.send_header("Content-Type","text/html")
        self.send_header("Content-Length",str(len(page)))
        self.end_headers()
        self.wfile.write(page)
        
    def handle_error(self,msg):
         
        content=self.Error_Page.format(path=self.path,msg=msg)
        self.send_content(content,404)
        
    def send_content(self,content,status=200):
        self.send_response(status)
        self.send_header("Content-Type","text/html")
        self.send_header("Content-Length",str(len(content)))
        self.end_headers()
        self.wfile.write(content)
        
    def do_GET(self):
##        page = self.create_Page()
##        self.send_Page(page)
##
            try:
                full_path=os.getcwd()+self.path.replace("/","\\")
                print self.path
                print full_path
                if not os.path.exists(full_path):
                    raise ServerException("%s not exists",full_path)
                elif os.path.isfile(full_path):
                    self.handle_file(full_path)
                else:
                    raise ServerException ("Unknown object {0}".format(self.path))
            except Exception as msg:
                self.handle_error(msg)
                
if __name__=='__main__':

        serverAddress=('',8087)
        server = BaseHTTPServer.HTTPServer(serverAddress,RequestHandler)
        server.serve_forever()

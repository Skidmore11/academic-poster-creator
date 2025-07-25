import http.server
import socketserver
import webbrowser
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

if __name__ == '__main__':
    with socketserver.TCPServer(('', PORT), MyHTTPRequestHandler) as httpd:
        print(f' Landing page server started at http://localhost:{PORT}')
        print(f' Serving: {os.getcwd()}')
        print(f' Open your browser and go to: http://localhost:{PORT}/landing_page.html')
        print('Press Ctrl+C to stop the server')
        
        try:
            # Open browser automatically
            webbrowser.open(f'http://localhost:{PORT}/landing_page.html')
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('\n Server stopped')

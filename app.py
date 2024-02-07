import http.server
import socketserver

# Specify the port you want to use
port = 8000

# Create a simple HTTP server
handler = http.server.SimpleHTTPRequestHandler

# Start the server
with socketserver.TCPServer(("", port), handler) as httpd:
    print(f"Serving on port {port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
        print("Server stopped.")

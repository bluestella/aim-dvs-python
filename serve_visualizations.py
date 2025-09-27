#!/usr/bin/env python3
"""
Enhanced HTTP Server for Visualizations

This script starts a local web server to view HTML visualizations
with directory listing and dynamic file access.
"""

import http.server
import socketserver
import webbrowser
import os
import argparse
import urllib.parse
import html

class EnhancedHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Enhanced HTTP request handler with directory listing capabilities."""
    
    def list_directory(self, path):
        """Helper to produce a directory listing (absent index.html).

        Return value is either a file object, or None (indicating an
        error).  In either case, the headers are sent, making the
        interface the same as for send_head().
        """
        try:
            list_dir = os.listdir(path)
        except OSError:
            self.send_error(404, "No permission to list directory")
            return None
        
        list_dir.sort(key=lambda a: a.lower())
        
        # Filter for HTML files
        html_files = [x for x in list_dir if x.endswith('.html')]
        other_files = [x for x in list_dir if not x.endswith('.html')]
        
        # Sort HTML files first, then other files
        list_dir = html_files + other_files
        
        r = []
        try:
            displaypath = urllib.parse.unquote(self.path, errors='surrogatepass')
        except UnicodeDecodeError:
            displaypath = urllib.parse.unquote(path)
        
        r.append('<!DOCTYPE HTML>')
        r.append('<html>\n<head>')
        r.append('<meta charset="utf-8">')
        r.append('<title>Directory listing for %s</title>' % displaypath)
        r.append('<style>')
        r.append('body { font-family: Arial, sans-serif; margin: 20px; }')
        r.append('h1 { color: #333; }')
        r.append('.container { max-width: 800px; margin: 0 auto; }')
        r.append('ul { list-style-type: none; padding: 0; }')
        r.append('li { margin: 5px 0; padding: 8px; border-radius: 4px; }')
        r.append('li:hover { background-color: #f5f5f5; }')
        r.append('li.html-file { background-color: #e6f7ff; }')
        r.append('a { text-decoration: none; color: #0366d6; display: block; }')
        r.append('a:hover { text-decoration: underline; }')
        r.append('.file-info { color: #666; font-size: 0.9em; margin-left: 10px; }')
        r.append('</style>')
        r.append('</head>\n<body>')
        r.append('<div class="container">')
        r.append('<h1>Directory listing for %s</h1>' % displaypath)
        r.append('<hr>')
        r.append('<ul>')
        
        # Add parent directory link
        if displaypath != '/':
            r.append('<li><a href="../">../</a></li>')
        
        for name in list_dir:
            fullname = os.path.join(path, name)
            displayname = linkname = name
            
            # Append / for directories or @ for symbolic links
            if os.path.isdir(fullname):
                displayname = name + "/"
                linkname = name + "/"
                file_class = "directory"
            elif os.path.islink(fullname):
                displayname = name + "@"
                file_class = "symlink"
            elif name.endswith('.html'):
                file_class = "html-file"
            else:
                file_class = "regular-file"
                
            # Quote the name for URL
            linkname = urllib.parse.quote(linkname, errors='surrogatepass')
            
            # Create list item with appropriate class
            r.append('<li class="%s"><a href="%s">%s</a>' % 
                    (file_class, linkname, html.escape(displayname)))
            
            # Add file size for non-directories
            if not os.path.isdir(fullname):
                file_size = os.path.getsize(fullname)
                size_str = self._format_file_size(file_size)
                r.append('<span class="file-info">%s</span>' % size_str)
                
            r.append('</li>')
            
        r.append('</ul>')
        r.append('<hr>')
        r.append('</div>')
        r.append('</body>\n</html>')
        
        encoded = '\n'.join(r).encode('utf-8', 'surrogateescape')
        
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        
        # Write the encoded content directly to wfile
        self.wfile.write(encoded)
        return None
    
    def _format_file_size(self, size):
        """Format file size in a human-readable format."""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.1f} {unit}"
            size /= 1024.0
        return f"{size:.1f} TB"
    
    def end_headers(self):
        # Add CORS headers to allow embedding in other sites
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

def start_server(port=8000, directory=None, open_browser=True, default_file=None):
    """Start an enhanced HTTP server to serve visualization files.
    
    Args:
        port: Port number to use (default: 8000)
        directory: Directory to serve files from (default: current directory)
        open_browser: Whether to automatically open the browser (default: True)
        default_file: Default file to open in browser (default: None)
    """
    # Use the directory parameter if provided, otherwise use current directory
    if directory:
        os.chdir(directory)
    
    # Create the server with the enhanced handler
    Handler = EnhancedHTTPRequestHandler
    
    # Create the server
    with socketserver.TCPServer(("", port), Handler) as httpd:
        server_address = f"http://localhost:{port}"
        print(f"Server started at {server_address}")
        print(f"You can access any HTML file by typing its path in the address bar")
        
        # Open the browser if requested
        if open_browser:
            # Open the specified default file if it exists
            if default_file and os.path.exists(default_file):
                webbrowser.open(f"{server_address}/{default_file}")
            # Otherwise open the visualization file if it exists
            elif os.path.exists("altair_visualization.html"):
                webbrowser.open(f"{server_address}/altair_visualization.html")
            # Otherwise just open the server root
            else:
                webbrowser.open(server_address)
        
        # Keep the server running until interrupted
        try:
            print("Press Ctrl+C to stop the server")
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Start an enhanced HTTP server for visualizations")
    parser.add_argument("-p", "--port", type=int, default=8000, help="Port to run the server on (default: 8000)")
    parser.add_argument("-d", "--directory", type=str, help="Directory to serve files from")
    parser.add_argument("--no-browser", action="store_true", help="Don't open the browser automatically")
    parser.add_argument("--default-file", type=str, help="Default file to open in browser")
    
    args = parser.parse_args()
    
    # Start the server
    start_server(
        port=args.port,
        directory=args.directory,
        open_browser=not args.no_browser,
        default_file=args.default_file
    )
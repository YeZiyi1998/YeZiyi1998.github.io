#!/usr/bin/env python3
"""Dependency-free static-site preview and optional distribution packaging."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / '_site'
FILES = ('index.html', 'about.html', 'about', 'assets/css/academic.css', 'images', 'files', 'CNAME', '.nojekyll')
RELOAD = b'''<script>
(() => {
  let version;
  setInterval(async () => {
    try {
      const response = await fetch('/__dev_version', {cache: 'no-store'});
      if (!response.ok) return;
      const next = await response.text();
      if (version !== undefined && next !== version) location.reload();
      version = next;
    } catch (_) {}
  }, 1000);
})();
</script>'''


def version():
    paths = [ROOT / 'index.html', ROOT / 'about.html', ROOT / 'about/index.html']
    paths += list((ROOT / 'assets/css').glob('*.css'))
    paths += [p for p in (ROOT / 'images').rglob('*') if p.is_file()]
    return str([(str(p.relative_to(ROOT)), p.stat().st_mtime_ns) for p in paths if p.exists()]).encode()


class Preview(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

    def do_GET(self):
        path = self.path.split('?', 1)[0]
        if path == '/__dev_version':
            self.send_bytes(version(), 'text/plain')
        elif path in ('/', '/index.html'):
            self.send_bytes((ROOT / 'index.html').read_bytes().replace(b'</body>', RELOAD + b'</body>'), 'text/html; charset=utf-8')
        else:
            super().do_GET()

    def send_bytes(self, data, content_type):
        self.send_response(200)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('serve', 'build'))
    parser.add_argument('--port', type=int, default=4000)
    args = parser.parse_args()
    if args.command == 'build':
        if OUTPUT.exists():
            shutil.rmtree(OUTPUT)
        OUTPUT.mkdir()
        for name in FILES:
            source, dest = ROOT / name, OUTPUT / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            if source.is_dir():
                shutil.copytree(source, dest, ignore=shutil.ignore_patterns('.DS_Store'))
            else:
                shutil.copy2(source, dest)
        print(f'Static files copied to {OUTPUT}; no compilation required.')
    else:
        server = ThreadingHTTPServer(('127.0.0.1', args.port), partial(Preview, directory=str(ROOT)))
        print(f'Preview: http://127.0.0.1:{args.port}/ (auto refresh enabled)', flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            server.server_close()


if __name__ == '__main__':
    main()

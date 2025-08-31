from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

from forecast import forecast_trend

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>Trend Forecasting</title></head>
<body>
<h1>Trend Forecasting</h1>
<form method="GET">
  <label>Data (comma separated): <input name="data" value="{data}"></label><br>
  <label>Steps ahead: <input name="steps" type="number" value="{steps}"></label><br>
  <button type="submit">Forecast</button>
</form>
{forecast_section}
</body>
</html>
"""


class ForecastHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)
        data_input = params.get("data", [""])[0]
        steps = int(params.get("steps", ["1"])[0] or 1)
        forecast_section = ""
        if data_input:
            try:
                data = [float(x.strip()) for x in data_input.split(",") if x.strip()]
                forecast = forecast_trend(data, steps)
                forecast_section = f"<h2>Forecast</h2><p>{forecast}</p>"
            except Exception as e:
                forecast_section = f"<p>Error: {e}</p>"
        html = HTML_TEMPLATE.format(data=data_input, steps=steps, forecast_section=forecast_section)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())


def run(server_class=HTTPServer, handler_class=ForecastHandler):
    server_address = ("", 8000)
    httpd = server_class(server_address, handler_class)
    print("Serving on port 8000...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()

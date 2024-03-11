import http.server
import socketserver
import json
import time
import pijuice

pj = pijuice.PiJuice(1, 0x14)

# Function to get battery charge level
def get_battery_charge():
    return pj.status.GetChargeLevel()

# Function to get solar panel input power
def get_solar_power():
    return pj.status.GetIoVoltage()

# Custom handler to serve JSON data
class DataHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/data':
            battery_charge = get_battery_charge()
            solar_power = get_solar_power()
            data = {'charge': battery_charge, 'power': solar_power}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        else:
            super().do_GET()

if __name__ == "__main__":
    PORT = 8080

    with socketserver.TCPServer(("", PORT), DataHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()

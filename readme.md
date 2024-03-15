# Solarserver scripts #

Collection of scripts used for the Raspberry Pi solar server. A lot of it is unfinished / very experimental / very specific for this situation. Everything in `./server` needs to be run in a venv on the Pi. See `./server/requirements.txt`.

- [`./server/`](server) contains script related to getting information related to the webserver to the website over Tinc. See the readme in the directory.
- [`battery.py`](battery.py) gets PiJuice battery status information and prints it to the terminal.
- [`flightmode.py`](flightmode.py) attempts to put the SIM7600X 4G HAT in flightmode, here for future reference.
- [`readme.md`](readme.md) this document
- [`shutdown_gsm.py`](shutdown_gsm.py) attempt to power down the SIM7600X over serial
- [`status.sh`](status.sh) gets the data from the other scripts and prints it to the terminal on request and login 
import requests

def get_bus_list(td):
    url = "http://ikuass.kuas.edu.tw/Bus/GetTimetable"
    payload = {
    "apiKey":"87vGou@pHO9nhk2",
    "drivedate":td
    }
    r = requests.post(url, data=payload)
    r = r.text
    return r

import network

def connect(ssid, password=None):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print(f"Connecting to WiFi network '{SSID}'... ", end='')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print("connected!")
    print("IP address:", sta_if.ifconfig()[0])
    print()
    

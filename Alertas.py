import os
import time
import telepot

# Token Telegram
token = '8484006372:AAG-uXnEGTe82E3yQkXFpP3eEKp4hEIzY84'
# ID del chat
chat_id = '5310820188'
# Declaración del BOT en el python
bot = telepot.Bot(token)

# Diccionario que almacena las IPs ROUTER & PC
ips = {
    "Router GNS": {"ip": "192.168.188.10", "estado": True},
    "PC1": {"ip": "192.168.10.10", "estado": True},
    "PC2": {"ip": "192.168.10.20", "estado": True}
}

# Verificar si una dirección IP responde al ping
def vivo(ip):
    return os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1") == 0

# Realiza el monitoreo continuo de los dispositivos en la red
def monitoreo():
    print("EL MONITOREO SE ENCUENTRA ACTIVO")
    while True:
        for nombre, datos in ips.items():
            ip = datos["ip"]
            estado_previo = datos["estado"]
            en_linea = vivo(ip)
            # Caso 1: si el dispositivo volvió a estar en línea
            if en_linea and not estado_previo:
                bot.sendMessage(chat_id, f"*{nombre}* volvió a estar en línea.", parse_mode = "Markdown")
            # Caso 2: si el dispositivo dejó de responder
            elif not en_linea and estado_previo:
                bot.sendMessage(chat_id, f"*{nombre}* está caído.", parse_mode = "Markdown")
            datos["estado"] = en_linea
        time.sleep(3)
monitoreo()
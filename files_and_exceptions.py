def read_file_to_dict(filename):
    ventas = {}
    with open(filename, "r") as file:
        line = file.readline().strip()
        items = line.split(";")
        for item in items:
            if not item:
                continue
            producto , valor = item.split(":")
            valor = float(valor)

            if producto not in ventas:
                ventas[producto]=[]
            ventas[producto].append(valor)
        return ventas

def process_dict(data):
    for producto, valores in data.items():
        total = (sum(valores))
        promedio = (total/len(valores))
        print(f"{producto}: ventas totales ${total}0, promedio ${promedio}0")

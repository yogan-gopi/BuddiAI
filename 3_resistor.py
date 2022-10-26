#3_resistor.py

def calcResistance(ring1, ring2, ring3):
    res = (color[ring1]*10 + color[ring2]) * (10**color[ring3])

    print("{} Ω ±5%".format(res))
    print("{} KΩ ±5%".format(res/(10**3)))
    print("{} MΩ ±5%".format(res/(10**6)))
    


if __name__ == '__main__':
    color = {"black": 0, "brown":1, "red":2, "orange":3, "yellow":4, 
             "green":5, "blue":6, "purple":7, "grey":8, "white":9}
    code = ["blue", "white", "red"]
    print("Resistance for the color code: '{}' is ".format(", ".join(code)))
    calcResistance(*code)
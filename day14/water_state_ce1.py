def water_state(temperature, solid=0, gas=100):
    if temperature <= solid:
        return "Solid"
    elif solid < temperature < gas:
        return "Liquid"
    else:
        return "Gas"

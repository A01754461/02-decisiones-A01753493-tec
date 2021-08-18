# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    ["2020"],
    ["100"],
    ["1993"],
    ["1600"],
    ["-1"]
    ]

# List of lists, where each inner list has all the output/prints that end in the terminal
output_values = [
    ["Año:", True],
    ["Año:", False],
    ["Año:", False],
    ["Año:", True],
    ["Año:", "Dato incorrecto"]
    ]

# List of hints for each test, in case of an error
error_messages = [
    ["Este caso es cuando Si es un año bisiesto"], 
    ["Este caso es cuando No es un año bisiesto (es múltiplo de 100 pero no de 400)"],
    ["Este caso es cuando No es un año bisiesto, ¿ya revisaste todos los casos que se pueden presentar?"],
    ["Este caso es cuando Si es un año bisiesto (es múltiplo de 400)"],
    ["¿Cuando nos debe salir el mensaje: Dato incorrecto?"]
    ]
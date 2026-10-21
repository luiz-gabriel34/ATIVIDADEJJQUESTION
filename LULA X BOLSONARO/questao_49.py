contador_global = 0

def incrementar():
    global contador_global
    contador_global += 1

incrementar()
print(contador_global)
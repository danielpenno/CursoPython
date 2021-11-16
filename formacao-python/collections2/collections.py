""" usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
print(assistiram)

print(set(assistiram))

usuarios = {1, 5, 76, 34, 52, 13, 17}
print(len(usuarios))

usuarios.add(765)
print(len(usuarios))

print(usuarios) """

aparicoes = {
    "Guilherme": 1,
    "cachorro": 2,
    "nome": 2,
    "vindo": 1
}

print(type(aparicoes))

print(aparicoes["Guilherme"])

import pennylane

device = pennylane.device("lightning.qubit", wires=1, shots=8192)

@pennylane.qnode(device)
def random():
    pennylane.Hadamard(wires=0)
    return pennylane.sample(wires=0)

bits = ''.join(str(b[0]) for b in random())
print(int(bits, 2))

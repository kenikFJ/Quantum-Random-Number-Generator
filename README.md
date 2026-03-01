# Quantum Random Number Generator (QRNG)

**Generation of truly random numbers powered by quantum computing**

## How it works

- One qubit is placed in superposition using a Hadamard gate
- The qubit is measured 8192 times (for 1 KiB)
- Results are concatenated into a binary string
- Binary string is converted to integer

(it wouldn't generate true random numbers if it works not on a real quantum computer)

## Installation

```bash
git clone https://github.com/kenikFJ/Quantum-Random-Number-Generator
cd Quantum-Random-Number-Generator
pip install -r requirements.txt
py qrng.py
```

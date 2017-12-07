from qiskit import QuantumProgram

qp = QuantumProgram()

try:
    qr = qp.create_quantum_register("qr", 2)
    cr = qp.create_classical_register("cr", 2)
    qc = qp.create_circuit("entangle", [qr], [cr])

    # H[0]|00> = (|00> + |01>)/sqrt(2)
    qc.h(qr[0])

    # CX[0,1](|00> + |01>)/sqrt(2)
    # = (CX[0,1]|00> + CX[0,1]|01>)/sqrt(2)
    # = (|00> + |11>)/sqrt(2)
    qc.cx(qr[0], qr[1])

    qc.measure(qr, cr)

    result = qp.execute(["entangle"], backend='local_qasm_simulator', shots=1024)

    print(result)
    print(result.get_data("entangle"))

except QISKitError as ex:
    print('Error in circuit: {}'.format(ex))
except RegisterSizeError as ex:
    print('Register error: {}'.format(ex))

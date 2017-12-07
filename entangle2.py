from qiskit import QuantumProgram

qp = QuantumProgram()

try:
    qr = qp.create_quantum_register("qr", 3)
    cr = qp.create_classical_register("cr", 3)
    qc = qp.create_circuit("entangle", [qr], [cr])

    # H[0]|000> = (|000> + |001>)/sqrt(2)
    qc.h(qr[0])

    # X[1](|000> + |001>)/sqrt(2) = (|010> + 011>)/sqrt(2)
    qc.x(qr[1])

    # X[2](|010> + |011>)/sqrt(2) = (|110> + |111>)/sqrt(2)
    qc.x(qr[2])

    # CX[0,1](|110> + |111>)/sqrt(2) = (|110> + |101>)/sqrt(2)
    qc.cx(qr[0], qr[1])

    # CX[0,2](|110> + 101>)/sqrt(2) = (|110> + |001>)/sqrt(2)
    qc.cx(qr[0], qr[2])

    qc.measure(qr, cr)

    result = qp.execute(["entangle"], backend='local_qasm_simulator', shots=1024)

    print(result)
    print(result.get_data("entangle"))

except QISKitError as ex:
    print('Error in circuit: {}'.format(ex))
except RegisterSizeError as ex:
    print('Register error: {}'.format(ex))

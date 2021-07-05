def calcularSapata():
    BPilar = int(input('Digite o menor lado do pilar(cm): '))
    LPilar = int(input('Digite o maior lado do pilar(cm): '))
    tensaoAdmSolo = float(input('Digite a tensão admissível do solo(kPa): '))
    cargaPilar = float(input('Digite a carga no pilar(kn): '))
    
    # usado para calcular a área de uma sapata
    area = (cargaPilar / tensaoAdmSolo)*10000
    B = 0.5*(BPilar - LPilar) + ((0.25*(BPilar - LPilar)**2) + area)**(1/2)
    L = B + (LPilar - BPilar)

    metroB = B/100
    metroL = L/100
    print()
    print(f'A área da sapata é {area} cm²')
    print(f'O lado B da sapata é {metroB:.2f} m')
    print(f'O lado L da sapata é {metroL:.2f} m')

calcularSapata()

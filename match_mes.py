mes = int(input("Digite um número corespondente a um mês (1-12):"))

match mes:
    case 1: print(f"Mês {mes}: Janeiro")
    case 2: print(f"Mês {mes}: Fevereiro")
    case 3: print(f"Mês {mes}: Março")
    case 4: print(f"Mês {mes}: Abril")
    case 5: print(f"Mês {mes}: Maio")
    case 6: print(f"Mês {mes}: Junho")
    case 7: print(f"Mês {mes}: Julho")
    case 8: print(f"Mês {mes}: Agosto")
    case 9: print(f"Mês {mes}: Setembro")
    case 10: print(f"Mês {mes}: Outubro")
    case 11: print(f"Mês {mes}: Novembro")
    case 12: print(f"Mês {mes}: Dezembro")
    case _: 
        print(f"Mês inválido")
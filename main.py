print("Bem vindo ao bot da Manu :)")
opcao = input("Digite um valor de 1 a 10: ")

match opcao:
    case "1":
        print("[Setor de Atendimento]")
        atendente = input("Qual atendimento vc quer? SAC ou RH: ")
        if atendente == "SAC":
            print("vai ser direcionado para o SAC")
        elif atendente == "RH":
            print("vai ser direcionado para o RH")
        else:
            print("nao existe esse atendimento")

    case "2":
        print("Segunda via do Boleto")
        pagamento = input("Forma de Pagamento? Cartao, PIX, Qrcode: ")
        if pagamento == "Cartao":
            print("voce vai pagar em cartao")
        elif pagamento == "PIX":
            print("voce vai pagar no PIX")
        elif pagamento == "Qrcode":
            print("voce vai pagar no Qrcode")
        else:
            print("nao tem essa forma de pagamento")
    case "3":
        print("Rastrear pedido")
        codigo = input("digita o codigo do pedido: ")
        if codigo == "123":
            print("seu pedido ta a caminho")
        elif codigo == "456":
            print("pedido ainda ta sendo preparado")
        else:
            print("codigo nao encontrado")
    case "4":
        print("Cancelar compra")
        motivo = input("por que quer cancelar? defeito ou desistiu: ")
        if motivo == "defeito":
            print("vamos cancelar e devolver seu dinheiro")
        elif motivo == "desistiu":
            print("compra cancelada")
        else:
            print("invalido")
    case "5":
        print("Troca e devolucao")
        dias = input("faz quantos dias que comprou? ")
        if dias == "7":
            print("ainda da pra trocar")
        elif dias == "10":
            print("ja passou do prazo")
        else:
            print("tem que ver com o SAC")
    case "6":
        print("Horario de atendimento")
        dia = input("hoje e segunda ou sabado? ")
        if dia == "segunda":
            print("aberto das 8 as 18")
        elif dia == "sabado":
            print("aberto das 8 as 12")
        else:
            print("hoje estamos fechados")
    case "7":
        print("Falar com humano")
        setor = input("quer falar com vendas ou suporte? ")
        if setor == "vendas":
            print("chamando o pessoal de vendas")
        elif setor == "suporte":
            print("chamando o suporte")
        else:
            print("setor nao existe")
    case "8":
        print("Reclamacao")
        nota = input("sua nota e 1 ou 2? ")
        if nota == "1":
            print("poxa desculpa, vamos melhorar")
        elif nota == "2":
            print("obrigado pela nota")
        else:
            print("nota invalida")
    case "9":
        print("Trabalhe conosco")
        vaga = input("vaga de estagio ou vendedor? ")
        if vaga == "estagio":
            print("manda curriculo pro rh")
        elif vaga == "vendedor":
            print("manda curriculo pra vaga de vendedor")
        else:
            print("no momento nao temos essa vaga")
    case "10":
        print("Sair")
        sair = input("quer sair mesmo? sim ou nao: ")
        if sair == "sim":
            print("valeu, ate mais :)")
        elif sair == "nao":
            print("beleza, continuamos aqui")
        else:
            print("nao entendi")

    case _:
        print("opcao invalida, digita de 1 a 10")
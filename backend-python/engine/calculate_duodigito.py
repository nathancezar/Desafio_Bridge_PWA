import argparse
import time


class Duodigit:

    def __init__(self, number):
        self._number = float(number)
        self._counter = 2

    def check_duodigit(self):
        """
        Função responsável por procurar o multiplo duodigito.
        O algoritmo funciona convetendo os números em strings e
        comparando o primeiro dígito com os demais.
        Ao encontrar o primeiro dígito diferente ele também passa a ser comparado.

        Returns: um dicionário contendo o resultado e o tempo de execução

        """
        start_time = time.time()
        try:
            while True:
                diferent_chars = 1
                multiple = str(self._number * self._counter).replace(".0", "").replace(".", "")
                # remove o '.0' ou só o '.' do final da string
                first_char = multiple[0]
                # seleciona o primeiro digito
                dif_char = ""
                # variável usada para verificar um segundo caracter diferente.
                # já que verificar apenas o primeiro gera um erro ao não validar
                # números com dígitos repetidos, como 1122.

                # O laço percorre cada string começando do segundo digito
                for i in range(1, len(multiple)):
                    if first_char != multiple[i] and dif_char != multiple[i]:
                        diferent_chars += 1
                        dif_char = multiple[i]
                        # a variável vai ser atualizada no caso de um terceiro digito diferente,
                        # mas isso não gera erro pois 'diferent_chars' será implementado
                        # inpedindo mais de

                # Caso a quantidade de digitos diferentes seja menor que 3, finaliza a busca
                if diferent_chars < 3:
                    break

                self._counter += 1

        # Tratamento de exceção simples
        except Exception as erro:
            print(erro)
            return {"duodigit": 0, "time": 0}
        # Caso entre em loop infinito e o usuário resolva interromper a execução
        except KeyboardInterrupt:
            print("Execução interrompida")
            return {"duodigit": 0, "time": 0}

        process_time = (time.time() - start_time)
        return {"duodigit": multiple, "time": process_time}


if __name__ == '__main__':
    """
    Para usar o algoritmo isoladamente.
    $ python calculate_duodigito.py -n 290
    """
    ap = argparse.ArgumentParser()
    ap.add_argument("-n", "--number", required=True,
                    help="numero desejado para encontrar um multiplo duodigito")

    args = vars(ap.parse_args())
    duodigit = Duodigit(args['number'])
    print(duodigit.check_duodigit())

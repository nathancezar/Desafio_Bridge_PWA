import argparse
import time


class Duodigit:
    def __init__(self, number):
        self._number = float(number)
        self._counter = 2

    def check_duodigit(self):
        start_time = time.time()
        try: 
            while True:
                diferent_chars = 1
                multiple = str(self._number * self._counter).replace(".0", "").replace(".", "")
                first_char = multiple[0]
                dif_char = ""
                
                for i in range(1,len(multiple)):
                    if first_char != multiple[i] and dif_char != multiple[i]:
                        diferent_chars += 1
                        dif_char = multiple[i]
                    
                if diferent_chars < 3:
                    break

                self._counter += 1
        
        except Exception as erro:
            print(erro)
            return {"duodigit": 0, "time": 0}
        except KeyboardInterrupt:
            print("Execução interrompida")
            return {"duodigit": 0, "time": 0}

        process_time = (time.time() - start_time)
        return {"duodigit": multiple, "time": process_time}

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-n", "--number", required=True,
                    help="numero desejado para encontrar um multiplo duodigito")

    args = vars(ap.parse_args())
    duodigit = Duodigit(args['number'])
    print(duodigit.check_duodigit())

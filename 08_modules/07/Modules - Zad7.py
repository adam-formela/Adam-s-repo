import fibonnaci

def main():
    value = int(input('Podaj wartość dla jakiej chcesz stworzyć ciąg fibbonaciego 1 -20 ->'))
    fibonnaci.generate_fibbonaci_seq(value)

if __name__ == '__main__':
    main()
import logging

def sum():
    logging.debug("This is the debug message")
    num1 = 5
    num2 = 10
    sum = num1 + num2
    print(f'Sum:{sum}')

def main():

    fmtstr = "  %(asctime)s: (%(filename)s): %(levelname)s: %(funcName)s  Line: %(lineno)d - %(message)s"
    datestr = "%m/%d/%Y %I:%M:%S %p "

    #custom logging config
    logging.basicConfig(
        filename="custom_log_output.log",
        level=logging.DEBUG,
        filemode="w",
        format=fmtstr,
        datefmt=datestr,
    )

    logging.info("Info messages")
    logging.warning("Warning message")
    sum()

if __name__ == '__main__':
    main()


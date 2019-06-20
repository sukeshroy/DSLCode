import logging

def main():

    # printing all the message
    logging.basicConfig(level=logging.DEBUG,filename="output.log",filemode="w")

    #logging levels
    logging.debug("Debug message")
    logging.info("Info mesage")
    logging.warning("Warning message")
    logging.error("Error message")
    logging.critical("Critical Message")

if __name__ == '__main__':
    main()



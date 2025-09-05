import logging


logging.basicConfig(
    level=logging.INFO,
    filename='web_app.log',
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def login(name):
    logging.info(f"User {name} logged in ")



def process_data(data):
    try:
        if data== 'bad_data':
            raise ValueError("Invalid data")
        logging.info(f"Data processed: {data}")

    except ValueError as e:
        logging.error(f"Error processing data: {e}",exc_info=False)


def logout(name):
    logging.info(f"User {name} logged out")


if __name__=="__main__":
    name="Harsh Chauhan"
    data="bad_data"
    login(name)
    process_data(data)
    logout(name)






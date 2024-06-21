from dotenv import load_dotenv
from src.form.Login_form import Login


def main():


    Login(db_key='1')

if __name__ == '__main__':
    load_dotenv()
    main()

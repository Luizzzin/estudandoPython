from stages import model_leads
import repo

def add_lead():
    name = input("nome: ")
    company = input("empresa: ")
    email = input("email: ")

    repo.create_lead(model_leads(name, company, email))
    print("LEAD ADICIONADO")


def list_lead():
    print("LISTAR LEADS")


def main():
    while True:
        print_menu()
        op = input("Escolha: ")
        if op == "1":
            add_lead()
        elif op == "2":
            list_lead()
        elif op == "0":
            print("ate mais")
            break
        else:
            print("invalido")

def print_menu():
    print("\n mini CRM de leads - (adicionar/listar)")
    print("[1] adicionar lead")
    print("[2] listar leads")
    print("[0] Sair do programa")

if __name__ == "__main__":
    main()
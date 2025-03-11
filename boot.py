import pywhatkit as kit
import time
import keyboard


def enviar_mensagem():
    numero = input("Digite o número com DDD (ex: +55 11 999999999): ")
    mensagem = input("Digite a mensagem: ")
    hora = int(input("Digite a hora para enviar (formato 24horas): "))
    minuto = int(input("Digite os minutos: "))

    print(f"Agendando mensagem para {numero} às {hora}:{minuto}...")
    kit.sendwhatmsg(numero, mensagem, hora, minuto)


def enviar_mensagem_automatica():
    numero = input("Digite o número com DDD (ex: +55 11 999999999): ")
    mensagem = input("Digite a mensagem: ")

    print("\nAbrindo WhatsApp Web e enviando a mensagem automaticamente...")
    kit.sendwhatmsg_instantly(numero, mensagem,

                              wait_time=15)  # Aguarda 15s para garantir o carregamento do WhatsApp Web

    print(f"\n✅ Mensagem enviada para {numero} com sucesso!")


def menu():
    while True:
        print("\n🔹 MENU DO BOT WHATSAPP 🔹")
        print("1️⃣ - Enviar mensagem agendada")
        print("2️⃣ - Enviar mensagem imediatamente")
        print("3️⃣ - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            enviar_mensagem()
        elif opcao == "2":
            enviar_mensagem_automatica()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()

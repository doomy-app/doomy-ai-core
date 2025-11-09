import os
from openai import OpenAI
from dotenv import load_dotenv
from modules.agent_core import DoomyAgent

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def main():
    print("🤖 DOOMY IA - Núcleo Inteligente de Asesoramiento Inmobiliario")
    print("Escribe 'salir' para terminar.\n")

    agent = DoomyAgent(client)

    while True:
        user_input = input("👤 Tú: ")
        if user_input.lower() in ["salir", "exit", "quit"]:
            print("👋 Hasta luego, gracias por usar Doomy.")
            break
        response = agent.chat(user_input)
        print(f"🏠 Doomy: {response}\n")

if __name__ == "__main__":
    main()

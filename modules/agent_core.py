class DoomyAgent:
    def __init__(self, client):
        self.client = client
        self.role = "Doomy, asistente inmobiliario y legal para compra/venta de vivienda."

    def chat(self, user_input):
        response = self.client.responses.create(
            model="gpt-5-mini",
            input=f"{self.role} {user_input}"
        )
        return response.output_text

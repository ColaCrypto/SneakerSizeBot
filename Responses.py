from datetime import datetime


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("ciao"):
        return "Ciao"

    return "❌Scusami, ma non ti ho capito❌\n \nPer capire come utilizzarmi al meglio schiaccia su questa scritta---> /aiuto !"
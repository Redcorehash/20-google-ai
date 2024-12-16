from google.cloud import translate_v2 as translate

def translate_text(text, target="es"):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target)
    print(f"Original: {text}")
    print(f"Translated: {result['translatedText']}")

if __name__ == "__main__":
    text = "Hello, how are you?"
    translate_text(text)

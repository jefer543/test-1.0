from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

import re
from email_validator import validate_email, EmailNotValidError

def is_valid_email_regex(email):
    """Verifica se um endereço de e-mail é válido usando expressão regular."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

def is_valid_email_library(email):
    """Verifica se um endereço de e-mail é válido usando a biblioteca email_validator."""
    try:
        validate_email(email, check_deliverability=True)
        return True
    except EmailNotValidError:
        return False

# Exemplo de uso
email_valido = "exemplo@dominio.com"
email_invalido = "invalido.com"

print(f"'{email_valido}' é válido (regex): {is_valid_email_regex(email_valido)}")
print(f"'{email_invalido}' é válido (regex): {is_valid_email_regex(email_invalido)}")
print(f"'{email_valido}' é válido (biblioteca): {is_valid_email_library(email_valido)}")
print(f"'{email_invalido}' é válido (biblioteca): {is_valid_email_library(email_invalido)}")
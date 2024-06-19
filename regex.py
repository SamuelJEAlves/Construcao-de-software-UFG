import re

def validar_login(login):
    login_regex = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{5,30}$')
    return bool(login_regex.match(login))

def validar_senha(password):
    password_regex = re.compile(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,12}$')
    return bool(password_regex.match(password))

# Testes
login = "User@123"
senha = "Passw0rd!"

print(f"Login válido? {validar_login(login)}")  # True
print(f"Senha válida? {validar_senha(senha)}")  # True

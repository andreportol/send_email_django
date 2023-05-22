# Para utilizar este formulário de contato, é necessário clonar o projeto.
# Após, clonar, é uma boa prática criar um ambiente virtual para instalação das bibliotecas.
# No mesmo diretório do manage.py, crie um arquivo .env para ocultar as variáveis de ambiente e dentro 
# do arquivo .env digite as seguintes variáveis. OBS. Não esqueça de escrever .env no arquivo .gitignore para que não fique visível no github.
DEBUG=
SECRET_KEY=
ALLOWED_HOSTS=

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_PORT=587
EMAIL_USE_TLS=True

POSTGRES_DB= 
POSTGRES_USER= 
POSTGRES_PASSWORD=
DB_HOST=
PORT=
# Agora seu projeto está pronto para funcionar na sua máquina. 
# Para que funcione no servidor da aplicação (railway) copie essas variáveis de ambiente para dentro servidor que irá rodar a aplicação.

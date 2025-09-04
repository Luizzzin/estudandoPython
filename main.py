# Importa o módulo 'os' para interagir com o sistema operacional e acessar variáveis de ambiente.
import os 
# Importa a biblioteca principal do Google Gemini para usar os modelos de IA.
import google.generativeai as genai
# Importa a função 'load_dotenv' para carregar variáveis de ambiente de um arquivo .env.
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env. Isso é útil para manter sua chave de API segura.
load_dotenv()

# Pega o valor da variável de ambiente 'GEMINI_API_KEY' e a armazena na variável CHAVE_API_KEY.
CHAVE_API_KEY = os.getenv("GEMINI_API_KEY")
# Configura a biblioteca do Gemini com a sua chave de API.
genai.configure(api_key=CHAVE_API_KEY)
# Define o nome do modelo que você quer usar. O "gemini-1.5-flash" é rápido e eficiente.
MODELO_ESCOLHIDO = "gemini-1.5-flash"

# Define uma instrução inicial para o modelo.
# Isso guia o comportamento do modelo, garantindo que a resposta siga um formato específico.
prompt_sistema = "Liste apenas os nomes e ofereça uma breve descrição de cada um"

# Cria uma instância do modelo de IA.
# O 'model_name' especifica qual modelo usar, e o 'system_instruction' aplica o prompt inicial.
llm = genai.GenerativeModel(
    model_name=MODELO_ESCOLHIDO,
    system_instruction=prompt_sistema
)

# Define a pergunta que você quer fazer ao modelo.
pergunta = "melhores carros para comprar no brasil com 28mil reais"
# Envia a pergunta para o modelo e armazena a resposta na variável 'resposta'.
resposta = llm.generate_content(pergunta)
# Imprime o texto da resposta gerada pelo modelo.
print(f'Resposta gerada:{resposta.text}')
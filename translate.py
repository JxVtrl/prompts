import os
from deep_translator import GoogleTranslator

# Configurações do caminho
input_folder = "./"
output_folder = "./translated"

# Inicializa o tradutor
translator = GoogleTranslator(source='en', target='pt')

# Função para traduzir o conteúdo do arquivo
def translate_file(file_path, output_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Dividir o conteúdo em pedaços menores se necessário
        translated = ""
        chunk_size = 5000  # Define o tamanho do chunk
        for i in range(0, len(content), chunk_size):
            chunk = content[i:i+chunk_size]
            translated_chunk = translator.translate(chunk)
            translated += translated_chunk
        
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(translated)
        
        print(f"Tradução concluída para {file_path.encode('utf-8', errors='ignore').decode('utf-8', errors='ignore')}")
    except Exception as e:
        print(f"Erro ao traduzir {file_path.encode('utf-8', errors='ignore').decode('utf-8', errors='ignore')}: {str(e).encode('utf-8', errors='ignore').decode('utf-8', errors='ignore')}")

# Função para traduzir o nome do arquivo
def translate_filename(filename):
    try:
        name, ext = os.path.splitext(filename)
        translated_name = translator.translate(name)
        return translated_name + ext
    except Exception as e:
        print(f"Erro ao traduzir o nome do arquivo {filename.encode('utf-8', errors='ignore').decode('utf-8', errors='ignore')}: {str(e).encode('utf-8', errors='ignore').decode('utf-8', errors='ignore')}")
        return filename

# Cria a pasta de saída se não existir
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Extensões de arquivo suportadas
supported_extensions = ('.txt', '.md', '.html', '.xml', '.json')

# Processa todos os arquivos suportados na pasta de entrada
for filename in os.listdir(input_folder):
    if filename.lower().endswith(supported_extensions):
        input_file = os.path.join(input_folder, filename)
        translated_filename = translate_filename(filename)
        output_file = os.path.join(output_folder, translated_filename)
        translate_file(input_file, output_file)

print("Tradução completa!")

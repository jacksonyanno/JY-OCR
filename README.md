# JY-OCR for Images (JPG/JPEG/PNG)
# Introdução

O programa JY-OCR permite ao usuário indicar o caminho de pastas contendo aqruivos de imgens em formatos de imagem JPG/JPEG/PNG e extrai os textos delas por meio da tecnologia OCR (Optical Character Recognition; Reconhecimento Ótico de Caracteres em portugês), gerando um arquivo de editável em formato TXT (.txt) com os caracteres reconhecidos nas imagens processadas.
  
Esse aplicativo pode ser útil em um ambiente empresarial em que se precise buscar por imagens de documenntos (recibos, notas, ofícios) a partir de infromações contidas nessas imagens. Assim, após a geração dos arquivos de texto das imagens, é possível pesquisar por informações na barra de pesquisa do Windows Explore. O nome do arquivo de texto encontrado, será o mesmo da imagem que se procura.
> O arquivo de texto de nome `ofício_123.txt` será o correspondente da imagem nomeada `ofício_123.jpg` (ou .jpg/.png).
  
[BAIXE AQUI](https://github.com/jacksonyanno/JY-OCR/releases/tag/v1.0.0) o aplicativo deste projeto. Para usar, basta extrair o aquivo ZIP em um diretório de sua preferência e executar o programa `JY-OCR.exe`.
  
Desenvolvedores devem seguir os passos seguintes:

# Pré-requisitos
## Instalação e configuração de ambiente Python
1. Instalar o `python3` no Windows 10/11
```powershell
Basta digitar o comando `python` no Power Shell que ele automaticamente irá instalar
```
2. Atualizar o `PIP`
```powershell
 python.exe -m pip install --upgrade pip
 ```
3. Instalar o `virtualenv`
```powershell
pip.exe install virtualenv
```
4. Criar e selecionar o ambiente virtual python
```powershell
# criando o ambiente virtual
python.exe -m venv venv
# ativando o ambiente virtual
.\venv\Scripts\activate
```

## Instalar o `Tesseract-OCR` na raiz deste projeto
1. Baixar o instalador no repositório [tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
2. Executar o arquivo .exe baixado
3. Durante a instalção
- Adicionar a linguagem `português` no pacote de linguagens
- Escolher a raiz deste projeto no como pasta de instalação desta aplicação

# Executar o projeto localmente
1. Ativar o ambiente virtual Python
```powershell
# ativando o ambiente virtual
.\venv\Scripts\activate
```
2. Instalar os requisitos de software
```powershell
pip.exe install -r .\requirements.txt
``` 
```powershell
python.exe .\JY-OCR.py
```
 
# Gerar executável (.exe) e arquivos para distribuição do software
1. Execute o comando a seguir
```powershell
pyinstaller.exe --windowed --noconsole --clean JY-OCR.py
```

2. Os arquivos de distribuição do programa `JY-OCR.exe` estarão na pasta `dist` 

3. Por fim, copie a pasta `.\tesseract-ocr` para dentro do diretório da distribuição (`.\dist\JY-OCR\_internal\`) 

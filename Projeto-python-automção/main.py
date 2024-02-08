import os 
from tkinter.filedialog import askdirectory



pasta_oringem = askdirectory(title="pasta origem")

pasta_destino = askdirectory(title="pasta destino")


regras_arquivo = {
    "jan": "Janeiro",
    "fev": "Fereiro",
    "mar": "Farço",
    "abr": "Abril",
}
lista_arquivos = os.listdir(pasta_oringem)
print(lista_arquivos)
for nome_arquivo in lista_arquivos:
  
  
    
  
    for chave in regras_arquivo.keys():
       
      if chave in nome_arquivo:
       
       
        nova_pasta = regras_arquivo[chave]

        nome_completo_oringinal = os.path.join(pasta_oringem, nome_arquivo)
        nome_completo_final = os.path.join(pasta_destino, nova_pasta, nome_arquivo)
        caminho_nova_pasta = os.path.join(pasta_destino,nova_pasta)


        if not os.path.exists(caminho_nova_pasta):
         
          os.mkdir(caminho_nova_pasta)
        os.rename(nome_completo_oringinal,nome_completo_final)

    
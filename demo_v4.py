#importa as bibliotecas necessárias para o código
import shutil
import csv
import openpyxl as opx
import os
import random as r
import time as t
import pandas as pd

#faz com que o programa execute 12 vezes seguidas, gerando 1 resultado
#para cada mês

for i in range(1, 13):
    results = []
    
#limpa o terminal


#determina se ouve lucro ou prejuízo na venda de um determinado 
#produto no mês anterior
    class produto:
        
        def __init__(self, nome, lista_qtd_compra):
            self.nome = nome
            self.lista_qtd_compra = lista_qtd_compra
            
        def sorteia_venda(self):
            self.venda = r.randint(100, 1000)
            
            if self.venda <= 500:
                self.resultado = 'prejuizo'
            else:
                self.resultado = 'lucro'                
            self.qtd_compra = r.choice(self.lista_qtd_compra)
            return f".{self.nome}. .{self.resultado}. .{self.qtd_compra}."

#com base nas informações anteriores, determina a quantidade de  
#garrafas de 2L de coca-cola que foi comprada pelo vendedor no mês 
#e adiciona o resultado à lista "results"

    class coca(produto):
        def __init__(self):
            self.lista_qtd_compra = ["140", "150", "160", "170", "180", "190", "200", "210", "220"]
            super().__init__("Coca-Cola 2L", self.lista_qtd_compra)
          
        def sorteia_venda(self):
            resultado = super().sorteia_venda()
            results.append(resultado)
            if self.resultado == 'lucro':
                self.lista_qtd_compra = ["140", "150", "160", "170", "180", "190", "200"]
            else:
                self.lista_qtd_compra = ["150", "160", "170", "180"]
            return resultado
          
    Coca = coca()
    resultado = Coca.sorteia_venda()
    ##print(resultado)

#com base nas informações anteriores, determina a quantidade de caixas de 2L de   
#leite que foi comprada pelo vendedor no mês 
#e adiciona o resultado à lista "results"

    class leite(produto):
      
        def __init__(self):
            self.lista_qtd_compra = ["140", "150", "160", "170", "180", "190", "200", "210", "220"]
            super().__init__("Leite", self.lista_qtd_compra)
          
        def sorteia_venda(self):
            resultado = super().sorteia_venda()
            results.append(resultado)
            if self.resultado == 'lucro':
                self.lista_qtd_compra = ["160", "170", "180", "190", "200", "210", "220"]
            else:
                self.lista_qtd_compra = ["140", "150", "160", "170", "180"]
            return resultado
          
    Leite = leite()
    resultado = Leite.sorteia_venda()
    ##print(resultado)
  
#com base nas informações anteriores, determina a quantidade  
#de pacotes de pães de fatia que foi comprada pelo vendedorno 
#no mês e adiciona o resultado à lista "results"

    class pao(produto):

        def __init__(self):
            self.lista_qtd_compra = ["140", "150", "160", "170", "180", "190", "200", "210", "220"]
            super().__init__("Pão", self.lista_qtd_compra)
            
        def sorteia_venda(self):
            resultado = super().sorteia_venda()
            results.append(resultado)
            if self.resultado == 'lucro':
                self.lista_qtd_compra = ["140", "150", "160", "170", "180", "190", "200"]
            else:
                self.lista_qtd_compra = ["150", "160", "170", "180"]
            return resultado
          
    Pao = pao()
    resultado = Pao.sorteia_venda()
    ##print(resultado)

#com base nas informações anteriores, determina a quantidade de garrafas de 
#detergente que foi comprada pelo vendedor no mês 
#e adiciona o resultado à lista "results"

    class detergente(produto):
      
        def __init__(self):
            self.lista_qtd_compra = ["140", "150", "160", "170", "180", "190", "200", "210", "220"]
            super().__init__("Detergente", self.lista_qtd_compra)
            
        def sorteia_venda(self):
            resultado = super().sorteia_venda()
            results.append(resultado)
            if self.resultado == 'lucro':
                self.lista_qtd_compra = ["120", "125", "130", "135", "140", "145", "150"]
            else:
                self.lista_qtd_compra = ["120", "125", "130", "135", "140"]
            return resultado
          
    Detergente = detergente()
    resultado = Detergente.sorteia_venda()
    ##print(resultado)

#com base nas informações anteriores, determina a quantidade de pacotes de papel higiênico 
#que foi comprada pelo vendedor no mês e adiciona o resultado à lista "results"

    class papel_higienico(produto):
      
        def __init__(self):
            self.lista_qtd_compra = ["140", "150", "160", "170", "180", "190", "200", "210", "220"]
            super().__init__("Papel Higiênico", self.lista_qtd_compra)
            
        def sorteia_venda(self):
            resultado = super().sorteia_venda()
            results.append(resultado)
            if self.resultado == 'lucro':
                self.lista_qtd_compra = ["90", "100", "110", "120"]
            else:
                self.lista_qtd_compra = ["90", "100", "110"]
            return resultado
          
    Papel_higienico = papel_higienico()
    resultado = Papel_higienico.sorteia_venda()
    ##print(resultado)

#com base nas informações anteriores, determina a quantidade de pacotes de café que foi comprada pelo vendedor
#no mês e adiciona o resultado à lista "results"

    class cafe(produto):
      
        def __init__(self):
            self.lista_qtd_compra = ["140", "150", "160", "170", "180", "190", "200", "210", "220"]
            super().__init__("Café", self.lista_qtd_compra)
            
        def sorteia_venda(self):
            resultado = super().sorteia_venda()
            results.append(resultado)
            if self.resultado == 'lucro':
                self.lista_qtd_compra = ["170", "175", "180", "185", "190", "195", "200", "205", "210"]
            else:
                self.lista_qtd_compra = ["150", "155", "160", "165", "170"]
            return resultado
          
    Cafe = cafe()
    resultado = Cafe.sorteia_venda()
    ##print(resultado)

#com base nas informações anteriores, determina a quantidade de pacotes de miojo que foi comprada pelo vendedor
#no mês e adiciona o resultado à lista "results"
    
    class miojo(produto):
      
        def __init__(self):
            self.lista_qtd_compra = ["140", "150", "160", "170", "180", "190", "200", "210", "220"]
            super().__init__("Miojo", self.lista_qtd_compra)
            
        def sorteia_venda(self):
            resultado = super().sorteia_venda()
            results.append(resultado)
            if self.resultado == 'lucro':
                self.lista_qtd_compra = ["110", "115", "120", "125", "130", "135", "140"]
            else:
                self.lista_qtd_compra = ["90", "95", "100", "105"]
            return resultado
          
    Miojo = miojo()
    resultado = Miojo.sorteia_venda()
    ##print(resultado)

#com base nas informações anteriores, determina a quantidade de macarrão que foi comprada pelo vendedor
#no mês e adiciona o resultado à lista "results"
    
    class macarrao(produto):
      
        def __init__(self):
            self.lista_qtd_compra = ["140", "150", "160", "170", "180", "190", "200", "210", "220"]
            super().__init__("Macarrão", self.lista_qtd_compra)
            
        def sorteia_venda(self):
            resultado = super().sorteia_venda()
            results.append(resultado)
            if self.resultado == 'lucro':
                self.lista_qtd_compra = ["95", "100" ,"105", "110", "115", "120", "125"]
            else:
                self.lista_qtd_compra = ["80", "85", "90", "95"]
            return resultado
          
    Macarrao = macarrao()
    resultado = Macarrao.sorteia_venda()
    ##print(resultado)

#com base nas informações anteriores, determina a quantidade de 
#peças de 1kg de carne que foi comprada pelo vendedor no mês 
#e adiciona o resultado à lista "results"

    class carne(produto):
      
        def __init__(self):
            self.lista_qtd_compra = ["140", "150", "160", "170", "180", "190", "200", "210", "220"]
            super().__init__("Carne", self.lista_qtd_compra)
            
        def sorteia_venda(self):
            resultado = super().sorteia_venda()
            results.append(resultado)
            if self.resultado == 'lucro':
                self.lista_qtd_compra = ["30", "35", "40", "45", "50"]
            else:
                self.lista_qtd_compra = ["20", "25", "30", "35", "40"]
            return resultado
          
    Carne = carne()
    resultado = Carne.sorteia_venda()
    ##print(resultado)

#com base nas informações anteriores, determina a quantidade de 
#peças de 1/2kg de frango que foi comprada pelo vendedor no mês 
#e adiciona o resultado à lista "results"
    
    class frango(produto):
      
        def __init__(self):
            self.lista_qtd_compra = ["140", "150", "160", "170", "180", "190", "200", "210", "220"]
            super().__init__("Frango", self.lista_qtd_compra)
            
        def sorteia_venda(self):
            resultado = super().sorteia_venda()
            results.append(resultado)
            if self.resultado == 'lucro':
                self.lista_qtd_compra = ["15", "20", "25", "30", "45", "50"]
            else:
                self.lista_qtd_compra = ["10", "15", "20", "25"]
            return resultado
            
    Frango = frango()
    resultado = Frango.sorteia_venda()
    ##print(resultado)


#com base nas informações anteriores, determina a quantidade de pacotes de 1kg  
# de farinha que foi comprada pelo vendedor no mês 
#e adiciona o resultado à lista "results"

    class farinha(produto):
      
        def __init__(self):
            self.lista_qtd_compra = ["140", "150", "160", "170", "180", "190", "200", "210", "220"]
            super().__init__("Farinha", self.lista_qtd_compra)
            
        def sorteia_venda(self):
            resultado = super().sorteia_venda()
            results.append(resultado)
            if self.resultado == 'lucro':
                self.lista_qtd_compra = ["90", "100", "110", "120"]
            else:
                self.lista_qtd_compra = ["80", "90" , "100", "110"]
            return resultado
          
    Farinha = farinha()
    resultado = Farinha.sorteia_venda()
    ##print(resultado)

#com base nas informações anteriores, determina a quantidade de  
#pacotes de 500g de queijo que foi comprada pelo vendedor no mês 
#e adiciona o resultado à lista "results"

    class queijo(produto):
      
        def __init__(self):
            self.lista_qtd_compra = ["140", "150", "160", "170", "180", "190", "200", "210", "220"]
            super().__init__("Queijo", self.lista_qtd_compra)
            
        def sorteia_venda(self):
            resultado = super().sorteia_venda()
            results.append(resultado)
            if self.resultado == 'lucro':
                self.lista_qtd_compra = ["145", "150", "155", "160", "165", "170", "175", "180", "185", "180", "195"]
            else:
                self.lista_qtd_compra = ["90", "95" , "100", "105"]
            return resultado

    Queijo = queijo()
    resultado = Queijo.sorteia_venda()
    ##print(resultado)

#com base nas informações anteriores, determina a quantidade de 
#pacotes de 500g de presunto que foi comprada pelo vendedor no mês 
#e adiciona o resultado à lista "results"

    class presunto(produto):
      
        def __init__(self):
            self.lista_qtd_compra = ["140", "150", "160", "170", "180", "190", "200", "210", "220"]
            super().__init__("Presunto", self.lista_qtd_compra)
            
        def sorteia_venda(self):
            resultado = super().sorteia_venda()
            results.append(resultado)
            if self.resultado == 'lucro':
                self.lista_qtd_compra = ["145", "150", "155", "160", "165", "170", "175", "180", "185", "180", "195"]
            else:
                self.lista_qtd_compra = ["90", "95" , "100", "105"]
            return resultado
          
    Presunto = presunto()
    resultado = Presunto.sorteia_venda()  
    #print(resultado)

#com base nas informações anteriores, determina a quantidade de 
#pacotes de 1kg de arroz que foi comprada pelo vendedor no mês 
#e adiciona o resultado à lista "results"

    class arroz(produto):
      
        def __init__(self):
            self.lista_qtd_compra = ["140", "150", "160", "170", "180", "190", "200", "210", "220"]
            super().__init__("Arroz", self.lista_qtd_compra)
            
        def sorteia_venda(self):
            resultado = super().sorteia_venda()
            results.append(resultado)
            if self.resultado == 'lucro':
                self.lista_qtd_compra = ["95", "100" ,"105", "110", "115", "120", "125"]
            else:
                self.lista_qtd_compra = ["80", "85", "90", "95"]
            return resultado
          
    Arroz = arroz()
    resultado = Arroz.sorteia_venda()
    #print(resultado)

#com base nas informações anteriores, determina a quantidade de 
#pacotes de 1kg de feijão que foi comprada pelo vendedor no mês 
#e adiciona o resultado à lista "results"

    class feijao(produto):
      
        def __init__(self):
            self.lista_qtd_compra = ["140", "150", "160", "170", "180", "190", "200", "210", "220"]
            super().__init__("Feijão", self.lista_qtd_compra)
            
        def sorteia_venda(self):
            resultado = super().sorteia_venda()
            results.append(resultado)
            if self.resultado == 'lucro':
                self.lista_qtd_compra = ["90", "95" ,"100", "105", "110", "115", "120"]
            else:
                self.lista_qtd_compra = ["75", "80", "85", "90"]
            return resultado
          
    Feijao = feijao()
    resultado = Feijao.sorteia_venda()
    #print(resultado)

#com base nas informações anteriores, determina a quantidade de 
#barras de chocolate que foi comprada pelo vendedor no mês 
#e adiciona o resultado à lista "results"

    class chocolate(produto):
      
        def __init__(self):
            self.lista_qtd_compra = ["140", "150", "160", "170", "180", "190", "200", "210", "220"]
            super().__init__("Chocolate", self.lista_qtd_compra)
            
        def sorteia_venda(self):
            resultado = super().sorteia_venda()
            results.append(resultado)
            if self.resultado == 'lucro':
                self.lista_qtd_compra = ["45", "50", "55", "60"]
            else:
                self.lista_qtd_compra = ["40", "45", "50", "55"]
            return resultado
          
    Chocolate = chocolate()
    resultado = Chocolate.sorteia_venda()
    #print(resultado)

#com base nas informações anteriores, determina a quantidade de 
#pacotes de ruffles que foi comprada pelo vendedor no mês 
#e adiciona o resultado à lista "results"

    class ruffles(produto):
      
        def __init__(self):
            self.lista_qtd_compra = ["140", "150", "160", "170", "180", "190", "200", "210", "220"]
            super().__init__("Ruffles", self.lista_qtd_compra)
            
        def sorteia_venda(self):
            resultado = super().sorteia_venda()
            results.append(resultado)
            if self.resultado == 'lucro':
                self.lista_qtd_compra = ["40", "45", "50", "55"]
            else:
                self.lista_qtd_compra = ["35", "40", "45", "50"]
            return resultado
          
    Ruffles = ruffles()
    resultado = Ruffles.sorteia_venda()
    #print(resultado)

#com base nas informações anteriores, determina a quantidade de  
#embalagens com uma dúzia de ovos que foi comprada pelo vendedor no mês 
#e adiciona o resultado à lista "results"

    class duzia_ovo(produto):
      
        def __init__(self):
            self.lista_qtd_compra = ["140", "150", "160", "170", "180", "190", "200", "210", "220"]
            super().__init__("Dúzia de Ovos", self.lista_qtd_compra)
            
        def sorteia_venda(self):
            resultado = super().sorteia_venda()
            results.append(resultado)
            if self.resultado == 'lucro':
                self.lista_qtd_compra = ["175", "180", "185", "190", "195", "200", "205"]
            else:
                self.lista_qtd_compra = ["160", "175", "180", "185"]
            return resultado
            
    Duzia_ovo = duzia_ovo()
    resultado = Duzia_ovo.sorteia_venda()
    #print(resultado)

#com base nas informações anteriores, determina a quantidade de  
#garrafas de 2L de sabão líquido que foi comprada pelo vendedor no mês 
#e adiciona o resultado à lista "results"

    class sabao_liquido(produto):
      
        def __init__(self):
            self.lista_qtd_compra = ["140", "150", "160", "170", "180", "190", "200", "210", "220"]
            super().__init__("Sabão Líquido 2L", self.lista_qtd_compra)
            
        def sorteia_venda(self):
            resultado = super().sorteia_venda()
            results.append(resultado)
            if self.resultado == 'lucro':
                self.lista_qtd_compra = ["80", "90", "100", "110", "120"]
            else:
                self.lista_qtd_compra = ["90", "100", "110"]
            return resultado
          
    Sabao_liquido = sabao_liquido()
    resultado = Sabao_liquido.sorteia_venda()
    #print(resultado)

#com base nas informações anteriores, determina a quantidade de  
#garrafas de água de 250ml que foi comprada pelo vendedor no mês 
#e adiciona o resultado à lista "results"

    class agua(produto):
      
        def __init__(self):
            self.lista_qtd_compra = ["140", "150", "160", "170", "180", "190", "200", "210", "220"]
            super().__init__("Garrafa D'Água 250ml", self.lista_qtd_compra)
            
        def sorteia_venda(self):
            resultado = super().sorteia_venda()
            results.append(resultado)
            if self.resultado == 'lucro':
                self.lista_qtd_compra = ["140","160", "170", "180", "190", "200", "210", "220", "240"]
            else:
                self.lista_qtd_compra = ["150", "160", "170", "180", "190", "200"]
            return resultado
          
    Agua = agua()
    resultado = Agua.sorteia_venda()
    #print(resultado)

#dá uma pausa de 1 segundo no código

    t.sleep(1)

#junta todos os resultados de todos os produtos em um arquivo de texto 
#que será gerado na mesma pasta em que o código foi executado, verificando 
#se já há um arquivo com os resultados e, caso houver, cria um novo com outro
#nome para facilitar a identificação do(s) arquivo(s)

    def save_results(results):
        filename = "resultados_{}.txt".format(i)
        with open(filename, "a") as f:
            for result in results:
                f.write(str(result) + '\n')
                
    save_results(results)
                
    def txt_to_dataframe():
        filename = "resultados_{}.txt".format(i)
        if not os.path.exists(filename):
            return None
        with open(filename, "r") as file:
            lines = file.readlines()
            dados = ".".join(lines)
            el = dados.split(".")
            data = []
            x = 0
            for j, _ in enumerate(range(1, 20)):
                produto = el[1 + x].strip()
                resultado = el[3 + x].strip()
                qtd_comp = el[5 + x].strip()
                data.append([produto, resultado, qtd_comp])
                df = pd.DataFrame(data, columns=["PRODUTO", "RESULTADO", "QTD. COMP."])
                x = x + 7
            return df

    meses = ['Janeiro', 'Fevereiro', 'Março',
         'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro',
         'Outubro', 'Novembro', 'Dezembro']

count = 0
for i, mes in enumerate(meses, start=1):
    count += 1
    print(f"Executando iteração {count}")
    save_results(results)
    df = txt_to_dataframe()
    if df is not None:
        nome_arquivo = f"Vendas {mes}.xlsx"
        with pd.ExcelWriter(nome_arquivo) as writer:
            df.to_excel(writer, index=False, sheet_name="Vendas")

    def txt_files():
        diretorio_atual = os.getcwd()
        pasta_txt = os.path.join(diretorio_atual, "txt")
        if not os.path.exists(pasta_txt):
            os.mkdir(pasta_txt)
        for nome_arquivo in os.listdir(diretorio_atual):
            caminho_arquivo = os.path.join(diretorio_atual, nome_arquivo)
            if os.path.isfile(caminho_arquivo) and nome_arquivo.endswith(".txt"):
                shutil.move(caminho_arquivo, pasta_txt)

    def xlsx_files():
        diretorio_atual = os.getcwd()
        pasta_planilhas = os.path.join(diretorio_atual, "planilhas")
        if not os.path.exists(pasta_planilhas):
            os.mkdir(pasta_planilhas)
        for nome_arquivo in os.listdir(diretorio_atual):
            caminho_arquivo = os.path.join(diretorio_atual, nome_arquivo)
            if os.path.isfile(caminho_arquivo) and nome_arquivo.endswith(".xlsx"):
                shutil.move(caminho_arquivo, pasta_planilhas)

os.system('cls')
txt_files()
xlsx_files()

import csv
import os
import Util
lista=[]
aux= {}
caminho='C:/Users/joao.almeida/Desktop/Dados/Ativos'
arquivos=list(os.listdir(caminho))
for arquivo in arquivos:
    if arquivo.find('Rioprev_Ativo_Civil_')!=-1:
        data=data=(arquivo.split('_')[-1].split(".")[0])
        data = "0" + "1" + "/" + data[0] + data[1] + '/' + data[2] + data[3] + data[4] + data[5]
        with open(caminho+'/'+arquivo) as f:
            reader = csv.reader(f, delimiter='|')
            verdade=True
            for row in reader:
                if verdade:
                    verdade=False
                else:
                    if (row[48]=='PROVENTO' and row[3]=="Mensal"and row[17]=="ATIVO" and row[49]==data):#pegar a data pelo nome do arquivo
                        lista.append(tuple(row))
        f.close()
        lista=list(set(lista))#virar um for dentro de for para verificar se é duplicada
        aux= Util.returnaDicionarioCivil(lista)
        if 'AtivosRP'+data[3]+data[4]+data[6]+data[7]+data[8]+data[9]+'.csv' in os.listdir(caminho+'/concluido'):
            with open(caminho+'/concluido/'+'AtivosRP'+data[3]+data[4]+data[6]+data[7]+data[8]+data[9]+'.csv', mode='a', newline='') as w:
                escritor_csv = csv.writer(w,delimiter=';')
                for chave,valor in aux.items():
                    for key,val in valor.items():
                        if key in ['Dados', 'Mutaveis']:
                            pass
                        else:
                            escritor_csv.writerow(Util.printarDadosCivis({'Dados':valor['Dados'],'Mutaveis':val['Mutaveis'],'VINCULO':key,'Valor':str(format(val["Valor"], ".2f"))}))
            w.close()
        else:
            with open(caminho+'/concluido/'+'AtivosRP'+data[3]+data[4]+data[6]+data[7]+data[8]+data[9]+'.csv', mode='w', newline='') as w:
                escritor_csv = csv.writer(w,delimiter=';')
                for chave,valor in aux.items():
                    for key,val in valor.items():
                        if key in ['Dados', 'Mutaveis']:
                            pass
                        else:
                            escritor_csv.writerow(Util.printarDadosCivis({'Dados':valor['Dados'],'Mutaveis':val['Mutaveis'],'VINCULO':key,'Valor':str(format(val["Valor"], ".2f"))}))
            w.close()
        lista.clear()
        aux.clear()
    elif arquivo.find('Rioprev_Ativo_Militar_')!=-1:
        data = data = (arquivo.split('_')[-1].split(".")[0])
        data = "0" + "1" + "/" + data[0] + data[1] + '/' + data[2] + data[3] + data[4] + data[5]
        with open(caminho + '/' + arquivo) as f:
            reader = csv.reader(f, delimiter='|')
            verdade = True
            i = 0
            for row in reader:
                i += 1
                if verdade:
                    verdade = False
                else:
                    if (row[48] == 'PROVENTO' and row[3] == "Mensal" and row[17] == "ATIVO" and row[49] == data):
                        lista.append(tuple(row))
        f.close()
        lista = list(set(lista))
        aux = Util.returnaDicionarioMilitar(lista)
        if 'AtivosRP' + data[3] + data[4] + data[6] + data[7] + data[8] + data[9] + '.csv' in os.listdir(
                caminho + '/concluido'):
            with open(caminho + '/concluido/' + 'AtivosRP' + data[3] + data[4] + data[6] + data[7] + data[8] + data[
                9] + '.csv', mode='a', newline='') as w:
                escritor_csv = csv.writer(w, delimiter=';')
                for chave, valor in aux.items():
                    for key, val in valor.items():
                        if key in ['Dados', 'Mutaveis']:
                            pass
                        else:
                            escritor_csv.writerow(Util.printarDadosMilitar({'Dados': valor['Dados'], 'Mutaveis': val['Mutaveis'], 'VINCULO': key,'Valor': str(format(val["Valor"], ".2f"))}))
            w.close()
        else:
            with open(caminho + '/concluido/' + 'AtivosRP' + data[3] + data[4] + data[6] + data[7] + data[8] + data[
                9] + '.csv', mode='w', newline='') as w:
                escritor_csv = csv.writer(w, delimiter=';')
                for chave, valor in aux.items():
                    for key, val in valor.items():
                        if key in ['Dados', 'Mutaveis']:
                            pass
                        else:
                            escritor_csv.writerow(Util.printarDadosMilitar(
                                {'Dados': valor['Dados'], 'Mutaveis': val['Mutaveis'], 'VINCULO': key,
                                 'Valor': str(format(val["Valor"], ".2f"))}))
            w.close()
        lista.clear()
        aux.clear()
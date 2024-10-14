from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
def returnaDicionarioCivil(lista,aux={}):
    for i in lista:
        if i[8] in aux:
            if i[1] in aux[i[8]]:

                aux[i[8]][i[1]]["Valor"] += round(float(i[47]), 2)
            else:
                aux[i[8]][i[1]] = {'Valor':round(float(i[47]), 2),"Mutaveis":{"DATA DE INGRESSO": i[24], "TEMPO DE CONTRIBUIÇÃO": abs((datetime.strptime(i[24], "%d/%m/%Y") - datetime.today()).days)-1,  "MATRICULA": i[12]}}
                if datetime.strptime(i[24], "%d/%m/%Y") > datetime.strptime('21/05/2012', "%d/%m/%Y"):
                    aux[i[8]][i[1]]["Mutaveis"]['COMPOSIÇÃO DA MASSA'] = 1
                else:
                    aux[i[8]][i[1]]["Mutaveis"]['COMPOSIÇÃO DA MASSA'] = 2
        else:
            aux[i[8]] = {'Dados':{'CNPJ': '03.066.219/0001-81' , 'NOME SECRETARIA': i[7] , 'IDENTIFICAÇÃO DO SEGURADO (MATRICULA)': i[12], 'CPF': i[8], 'PIS': '12154487582', 'SEXO': i[11], "ESTADO CIVIL": i[63], "DATA DE NASCIMENTO": i[10], "SITUAÇÃO FUNCIONAL": '1', "CATEGORIA": i[13], "NOME CARGO": i[19], "DEPENDENTE": '0', "DATA DE NASCIMENTO DO CÔNJUGE": i[64], 'DATA DE NASCIMENTO DO DEPENDENTE':i[66]}}
            aux[i[8]][i[1]] = {'Valor':round(float(i[47]), 2),"Mutaveis":{"DATA DE INGRESSO": i[24], "TEMPO DE CONTRIBUIÇÃO": abs((datetime.strptime(i[24], "%d/%m/%Y") - datetime.today()).days)-1,  "MATRICULA": i[12]}}
            #Inicio coluna Sexo
            if aux[i[8]]["Dados"]['SEXO'] == 'F':
                aux[i[8]]["Dados"]['SEXO'] = 1
            else:
                aux[i[8]]["Dados"]['SEXO'] = 2
            #Fim coluna Sexo
            #Inicio Coluna ESTADO CIVIL
            if aux[i[8]]["Dados"]['ESTADO CIVIL'] == 'S':
                aux[i[8]]["Dados"]['ESTADO CIVIL'] = 2
                aux[i[8]]["Dados"]['CONDIÇÃO DO CONJUGE'] = 1
            else:
                aux[i[8]]["Dados"]['ESTADO CIVIL'] = 1
                aux[i[8]]["Dados"]['CONDIÇÃO DO CONJUGE'] = ""
            #Fim Coluna ESTADO CIVIL
            #INICIO Coluna CONDIÇÃO DO DEPENDENTE(1)
            if i[66]:
                aux[i[8]]["Dados"]['CONDIÇÃO DO DEPENDENTE'] = 2
            else:
                aux[i[8]]["Dados"]['CONDIÇÃO DO DEPENDENTE'] = ""
            #FIM Coluna CONDIÇÃO DO DEPENDENTE(1)
            #INICIO Coluna CONDIÇÃO DO DEPENDENTE(2)
                if i[66]:
                    aux[i[8]]["Dados"]['CONDIÇÃO DO DEPENDENTE'] = 2
                else:
                    aux[i[8]]["Dados"]['CONDIÇÃO DO DEPENDENTE'] = ""
            #FIM Coluna CONDIÇÃO DO DEPENDENTE(2)
            #Coluna A - POPULACAO COBERTA
            if i[14] in ['CONCURSO PUBLICO', 'EFETIVO', 'REQUISICAO EXTERNA','REQUISICAO INTERNA']:
                aux[i[8]]["Dados"]['A - POPULACAO COBERTA'] = 1
            elif i[7] == 'PCERJ':
                aux[i[8]]["Dados"]['A - POPULACAO COBERTA'] = 4
            elif i[14] in ['CONTR PRZ INDETERM', 'CONTR TEMPORARIO',	'PENSAO ESPECIAL', 'PENSAO INST N IDENT']:
                aux[i[8]]["Dados"]['A - POPULACAO COBERTA'] = 5
            else:
                aux[i[8]]["Dados"]['A - POPULACAO COBERTA'] = ""
            #Fim da Coluna A - POPULACAO COBERTA
            #Inicio COluna COMPOSIÇÃO DA MASSA
            if datetime.strptime(i[24], "%d/%m/%Y") > datetime.strptime('21/05/2012', "%d/%m/%Y"):
                aux[i[8]][i[1]]["Mutaveis"]['COMPOSIÇÃO DA MASSA'] = 1
            else:
                aux[i[8]][i[1]]["Mutaveis"]['COMPOSIÇÃO DA MASSA'] = 2
            # FIM COluna COMPOSIÇÃO DA MASSA
            #Inicio Coluna B - POPULACAO COBERTA
            if i[19].find('PROFESSOR')!= -1:
                aux[i[8]]["Dados"]['B - POPULACAO COBERTA'] = 2
            else:
                aux[i[8]]["Dados"]['B - POPULACAO COBERTA'] = 4
            #FIM Coluna B - POPULACAO COBERTA
            # Inicio Coluna C - POPULACAO COBERTA
            if i[19].find('PROFESSOR')!= -1:
                aux[i[8]]["Dados"]['C - POPULACAO COBERTA'] = 3
            else:
                aux[i[8]]["Dados"]['C - POPULACAO COBERTA'] = 1
            # FIM Coluna C - POPULACAO COBERTA
            #Inicio Coluna CARGA HORÁRIA
            if i[23]:
                j = i[23].replace('HS', "")
                aux[i[8]]["Dados"]['CARGA HORÁRIA']=j.replace('MAGIST', "")
            else:
                aux[i[8]]["Dados"]['CARGA HORÁRIA'] =""
            #FIM Coluna Carga Horaria
            #Inicio Coluna TIPO DE VÍNCULO
            if i[14] in ['CONCURSO PUBLICO', 'EFETIVO']:
                aux[i[8]]["Dados"]['TIPO DE VÍNCULO']='1'
            elif i[14]=="CARGO COMISSAO":
                aux[i[8]]["Dados"]['TIPO DE VÍNCULO'] = '2'
            else:
                aux[i[8]]["Dados"]['TIPO DE VÍNCULO'] = '4'
            #FIM Coluna TIPO DE VÍNCULO
            #inicio coluna CONDIÇÃO DO CONJUGE
            if i[63]=='S':
                aux[i[8]]["Dados"]['CONDIÇÃO DO CONJUGE']='1'
            else:
                aux[i[8]]["Dados"]['CONDIÇÃO DO CONJUGE'] = ''
            #fim coluna CONDIÇÃO DO CONJUGE
    return aux
def printarDadosCivis(dict):
    #disct[Dados]=dicionario dados | disct[Mutaveis]=dicionario Mutaveis| disct[VINCULO]= numero vinculo | disct[Valor]= Valor
    aux = []
    aux.append('2')
    aux.append(dict['Mutaveis']['COMPOSIÇÃO DA MASSA'])
    aux.append(dict['Dados']['CNPJ'])
    aux.append(dict['Dados']['NOME SECRETARIA'])
    aux.append('1')
    aux.append('1')
    aux.append(dict['Dados']['A - POPULACAO COBERTA'])
    aux.append(dict['Dados']['B - POPULACAO COBERTA'])
    aux.append(dict['Dados']['C - POPULACAO COBERTA'])
    aux.append(dict['Mutaveis']['MATRICULA'])
    aux.append(dict['Dados']['CPF'])
    aux.append(dict['Dados']['PIS'])
    aux.append(dict['Dados']['SEXO'])
    aux.append(dict['Dados']['ESTADO CIVIL'])
    aux.append(dict['Dados']['DATA DE NASCIMENTO'])
    aux.append('1')
    aux.append(dict['Dados']['TIPO DE VÍNCULO'])
    aux.append(dict['Mutaveis']['DATA DE INGRESSO'])
    aux.append(dict['Mutaveis']['DATA DE INGRESSO'])
    aux.append(dict['Dados']['CATEGORIA'])
    aux.append(dict['Mutaveis']['DATA DE INGRESSO'])
    aux.append(dict['Dados']['NOME CARGO'])
    aux.append(locale.format_string("%.2f", float(dict['Valor']), grouping=True))
    aux.append(locale.format_string("%.2f", float(dict['Valor']), grouping=True))
    aux.append(dict['Mutaveis']['TEMPO DE CONTRIBUIÇÃO'])
    aux.append(dict['Mutaveis']['TEMPO DE CONTRIBUIÇÃO'])
    aux.append("0")
    aux.append(dict['Dados']['DATA DE NASCIMENTO DO CÔNJUGE'])
    aux.append(dict['Dados']['CONDIÇÃO DO CONJUGE'])
    aux.append(dict['Dados']['DATA DE NASCIMENTO DO DEPENDENTE'])
    aux.append(dict['Dados']['CONDIÇÃO DO DEPENDENTE'])
    aux.append(dict['Dados']['DATA DE NASCIMENTO DO DEPENDENTE'])
    aux.append(dict['Dados']['CONDIÇÃO DO DEPENDENTE'])
    aux.append('')
    aux.append('')
    aux.append(dict['Dados']['CARGA HORÁRIA'])

    return aux

def returnaDicionarioMilitar(lista,aux={}):
    for i in lista:
        if i[8] in aux:
            if i[1] in aux[i[8]]:

                aux[i[8]][i[1]]["Valor"] += round(float(i[47]), 2)
            else:
                aux[i[8]][i[1]] = {'Valor':round(float(i[47]), 2),"Mutaveis":{"DATA DE INGRESSO": i[24], "TEMPO DE CONTRIBUIÇÃO": abs((datetime.strptime(i[24], "%d/%m/%Y") - datetime.today()).days)-1,  "MATRICULA": i[12]}}
                if datetime.strptime(i[24], "%d/%m/%Y") > datetime.strptime('21/05/2012', "%d/%m/%Y"):
                    aux[i[8]][i[1]]["Mutaveis"]['COMPOSIÇÃO DA MASSA'] = 1
                else:
                    aux[i[8]][i[1]]["Mutaveis"]['COMPOSIÇÃO DA MASSA'] = 2
        else:
            aux[i[8]] = {'Dados':{'CNPJ': '03.066.219/0001-81' , 'NOME SECRETARIA': i[7] , 'IDENTIFICAÇÃO DO SEGURADO (MATRICULA)': i[12], 'CPF': i[8], 'PIS': '12154487582', 'SEXO': i[11], "ESTADO CIVIL": i[63], "DATA DE NASCIMENTO": i[10], "SITUAÇÃO FUNCIONAL": '1', "CATEGORIA": i[13], "NOME CARGO": i[19], "DEPENDENTE": '0', "DATA DE NASCIMENTO DO CÔNJUGE": i[64], 'DATA DE NASCIMENTO DO DEPENDENTE':i[66]}}
            aux[i[8]][i[1]] = {'Valor':round(float(i[47]), 2),"Mutaveis":{"DATA DE INGRESSO": i[24], "TEMPO DE CONTRIBUIÇÃO": abs((datetime.strptime(i[24], "%d/%m/%Y") - datetime.today()).days)-1,  "MATRICULA": i[12]}}
            #Inicio coluna Sexo
            if aux[i[8]]["Dados"]['SEXO'] == 'F':
                aux[i[8]]["Dados"]['SEXO'] = 1
            else:
                aux[i[8]]["Dados"]['SEXO'] = 2
            #Fim coluna Sexo
            #Inicio Coluna ESTADO CIVIL
            if aux[i[8]]["Dados"]['ESTADO CIVIL'] == 'S':
                aux[i[8]]["Dados"]['ESTADO CIVIL'] = 2
                aux[i[8]]["Dados"]['CONDIÇÃO DO CONJUGE'] = 1
            else:
                aux[i[8]]["Dados"]['ESTADO CIVIL'] = 1
                aux[i[8]]["Dados"]['CONDIÇÃO DO CONJUGE'] = ""
            #Fim Coluna ESTADO CIVIL
            #INICIO Coluna CONDIÇÃO DO DEPENDENTE(1)
            if i[66]:
                aux[i[8]]["Dados"]['CONDIÇÃO DO DEPENDENTE'] = "1"
            else:
                aux[i[8]]["Dados"]['CONDIÇÃO DO DEPENDENTE'] = ""
            #FIM Coluna CONDIÇÃO DO DEPENDENTE(1)
            #INICIO Coluna CONDIÇÃO DO DEPENDENTE(2)
                if i[66]:
                    aux[i[8]]["Dados"]['CONDIÇÃO DO DEPENDENTE'] = '1'
                else:
                    aux[i[8]]["Dados"]['CONDIÇÃO DO DEPENDENTE'] = ""
            #FIM Coluna CONDIÇÃO DO DEPENDENTE(2)
            #Coluna A - POPULACAO COBERTA
            if i[14] in ['CONCURSO PUBLICO', 'EFETIVO', 'REQUISICAO EXTERNA','REQUISICAO INTERNA']:
                aux[i[8]]["Dados"]['A - POPULACAO COBERTA'] = 1
            elif i[7] == 'PCERJ':
                aux[i[8]]["Dados"]['A - POPULACAO COBERTA'] = 4
            elif i[14] in ['CONTR PRZ INDETERM', 'CONTR TEMPORARIO',	'PENSAO ESPECIAL', 'PENSAO INST N IDENT']:
                aux[i[8]]["Dados"]['A - POPULACAO COBERTA'] = 5
            else:
                aux[i[8]]["Dados"]['A - POPULACAO COBERTA'] = ""
            #Fim da Coluna A - POPULACAO COBERTA
            #Inicio COluna COMPOSIÇÃO DA MASSA
            if datetime.strptime(i[24], "%d/%m/%Y") > datetime.strptime('21/05/2012', "%d/%m/%Y"):
                aux[i[8]][i[1]]["Mutaveis"]['COMPOSIÇÃO DA MASSA'] = 1
            else:
                aux[i[8]][i[1]]["Mutaveis"]['COMPOSIÇÃO DA MASSA'] = 2
            # FIM COluna COMPOSIÇÃO DA MASSA
            #Inicio Coluna B - POPULACAO COBERTA
            if i[19].find('PROFESSOR')!= -1:
                aux[i[8]]["Dados"]['B - POPULACAO COBERTA'] = 2
            else:
                aux[i[8]]["Dados"]['B - POPULACAO COBERTA'] = 4
            #FIM Coluna B - POPULACAO COBERTA
            # Inicio Coluna C - POPULACAO COBERTA
            if i[19].find('PROFESSOR')!= -1:
                aux[i[8]]["Dados"]['C - POPULACAO COBERTA'] = 3
            else:
                aux[i[8]]["Dados"]['C - POPULACAO COBERTA'] = 1
            # FIM Coluna C - POPULACAO COBERTA
            #Inicio Coluna CARGA HORÁRIA
            if i[23]:
                j = i[23].replace('HS', "")
                aux[i[8]]["Dados"]['CARGA HORÁRIA']=j.replace('MAGIST', "")
            else:
                aux[i[8]]["Dados"]['CARGA HORÁRIA'] =""
            #FIM Coluna Carga Horaria
            #Inicio Coluna TIPO DE VÍNCULO
            if i[14] in ['CONCURSO PUBLICO', 'EFETIVO']:
                aux[i[8]]["Dados"]['TIPO DE VÍNCULO']='1'
            elif i[14]=="CARGO COMISSAO":
                aux[i[8]]["Dados"]['TIPO DE VÍNCULO'] = '2'
            else:
                aux[i[8]]["Dados"]['TIPO DE VÍNCULO'] = '4'
            #FIM Coluna TIPO DE VÍNCULO
            #inicio coluna CONDIÇÃO DO CONJUGE
            if i[63]=='S':
                aux[i[8]]["Dados"]['CONDIÇÃO DO CONJUGE']='1'
            else:
                aux[i[8]]["Dados"]['CONDIÇÃO DO CONJUGE'] = ''
            #fim coluna CONDIÇÃO DO CONJUGE
    return aux
def printarDadosMilitar(dict):
    #disct[Dados]=dicionario dados | disct[Mutaveis]=dicionario Mutaveis| disct[VINCULO]= numero vinculo | disct[Valor]= Valor
    aux = []
    aux.append('2')
    aux.append(dict['Mutaveis']['COMPOSIÇÃO DA MASSA'])
    aux.append(dict['Dados']['CNPJ'])
    aux.append(dict['Dados']['NOME SECRETARIA'])
    aux.append('1')
    aux.append('1')
    aux.append("3")
    aux.append("5")
    aux.append("6")
    aux.append(dict['Mutaveis']['MATRICULA'])
    aux.append(dict['Dados']['CPF'])
    aux.append(dict['Dados']['PIS'])
    aux.append(dict['Dados']['SEXO'])
    aux.append(dict['Dados']['ESTADO CIVIL'])
    aux.append(dict['Dados']['DATA DE NASCIMENTO'])
    aux.append('1')
    aux.append(dict['Dados']['TIPO DE VÍNCULO'])
    aux.append(dict['Mutaveis']['DATA DE INGRESSO'])
    aux.append(dict['Mutaveis']['DATA DE INGRESSO'])
    aux.append(dict['Dados']['CATEGORIA'])
    aux.append(dict['Mutaveis']['DATA DE INGRESSO'])
    aux.append(dict['Dados']['NOME CARGO'])
    aux.append(locale.format_string("%.2f", float(dict['Valor']), grouping=True))
    aux.append(locale.format_string("%.2f", float(dict['Valor']), grouping=True))
    aux.append(dict['Mutaveis']['TEMPO DE CONTRIBUIÇÃO'])
    aux.append(dict['Mutaveis']['TEMPO DE CONTRIBUIÇÃO'])
    aux.append("0")
    aux.append(dict['Dados']['DATA DE NASCIMENTO DO CÔNJUGE'])
    aux.append(dict['Dados']['CONDIÇÃO DO CONJUGE'])
    aux.append(dict['Dados']['DATA DE NASCIMENTO DO DEPENDENTE'])
    aux.append(dict['Dados']['CONDIÇÃO DO DEPENDENTE'])
    aux.append(dict['Dados']['DATA DE NASCIMENTO DO DEPENDENTE'])
    aux.append(dict['Dados']['CONDIÇÃO DO DEPENDENTE'])
    aux.append('')
    aux.append('')
    aux.append(dict['Dados']['CARGA HORÁRIA'])

    return aux
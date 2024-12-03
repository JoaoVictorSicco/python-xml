import re

pml_string = """


<?xml version="1.0" encoding="ISO-8859-1"?><pnml>
<net id="Net-One" type="P/T net">
<token id="Default" enabled="true" red="0" green="0" blue="0"/>
<labels x="121" y="234" width="104" height="36" border="false">
<text>autonomous mode</text>
</labels>
<labels x="394" y="57" width="104" height="20" border="false">
<text>faul operation</text>
</labels>
<labels x="667" y="227" width="104" height="36" border="false">
<text>grid-connected mode</text>
</labels>
<labels x="418" y="372" width="104" height="36" border="false">
<text>synchonization operation</text>
</labels>
<place id="P0">
<graphics>
<position x="615.0" y="210.0"/>
</graphics>
<name>
<value>P0</value>
<graphics>
<offset x="0.0" y="0.0"/>
</graphics>
</name>
<initialMarking>
<value>Default,1</value>
<graphics>
<offset x="0.0" y="0.0"/>
</graphics>
</initialMarking>
<capacity>
<value>0</value>
</capacity>
</place>
<place id="P1">
<graphics>
<position x="210.0" y="210.0"/>
</graphics>
<name>
<value>P1</value>
<graphics>
<offset x="0.0" y="0.0"/>
</graphics>
</name>
<initialMarking>
<value>Default,0</value>
<graphics>
<offset x="0.0" y="0.0"/>
</graphics>
</initialMarking>
<capacity>
<value>0</value>
</capacity>
</place>
<place id="P2">
<graphics>
<position x="405.0" y="90.0"/>
</graphics>
<name>
<value>P2</value>
<graphics>
<offset x="0.0" y="0.0"/>
</graphics>
</name>
<initialMarking>
<value>Default,0</value>
<graphics>
<offset x="0.0" y="0.0"/>
</graphics>
</initialMarking>
<capacity>
<value>0</value>
</capacity>
</place>
<place id="P3">
<graphics>
<position x="420.0" y="315.0"/>
</graphics>
<name>
<value>P3</value>
<graphics>
<offset x="0.0" y="0.0"/>
</graphics>
</name>
<initialMarking>
<value>Default,0</value>
<graphics>
<offset x="0.0" y="0.0"/>
</graphics>
</initialMarking>
<capacity>
<value>0</value>
</capacity>
</place>
<transition id="T0">
<graphics>
<position x="540.0" y="90.0"/>
</graphics>
<name>
<value>T0</value>
<graphics>
<offset x="-5.0" y="35.0"/>
</graphics>
</name>
<orientation>
<value>0</value>
</orientation>
<rate>
<value>1.0</value>
</rate>
<timed>
<value>false</value>
</timed>
<infiniteServer>
<value>false</value>
</infiniteServer>
<priority>
<value>1</value>
</priority>
</transition>
<transition id="T1">
<graphics>
<position x="495.0" y="165.0"/>
</graphics>
<name>
<value>T1</value>
<graphics>
<offset x="-5.0" y="35.0"/>
</graphics>
</name>
<orientation>
<value>0</value>
</orientation>
<rate>
<value>1.0</value>
</rate>
<timed>
<value>false</value>
</timed>
<infiniteServer>
<value>false</value>
</infiniteServer>
<priority>
<value>1</value>
</priority>
</transition>
<transition id="T2">
<graphics>
<position x="330.0" y="135.0"/>
</graphics>
<name>
<value>T2</value>
<graphics>
<offset x="-5.0" y="35.0"/>
</graphics>
</name>
<orientation>
<value>0</value>
</orientation>
<rate>
<value>1.0</value>
</rate>
<timed>
<value>false</value>
</timed>
<infiniteServer>
<value>false</value>
</infiniteServer>
<priority>
<value>1</value>
</priority>
</transition>
<transition id="T4">
<graphics>
<position x="270.0" y="315.0"/>
</graphics>
<name>
<value>T4</value>
<graphics>
<offset x="-5.0" y="35.0"/>
</graphics>
</name>
<orientation>
<value>0</value>
</orientation>
<rate>
<value>1.0</value>
</rate>
<timed>
<value>false</value>
</timed>
<infiniteServer>
<value>false</value>
</infiniteServer>
<priority>
<value>1</value>
</priority>
</transition>
<transition id="T5">
<graphics>
<position x="330.0" y="255.0"/>
</graphics>
<name>
<value>T5</value>
<graphics>
<offset x="-5.0" y="35.0"/>
</graphics>
</name>
<orientation>
<value>0</value>
</orientation>
<rate>
<value>1.0</value>
</rate>
<timed>
<value>false</value>
</timed>
<infiniteServer>
<value>false</value>
</infiniteServer>
<priority>
<value>1</value>
</priority>
</transition>
<transition id="T6">
<graphics>
<position x="525.0" y="270.0"/>
</graphics>
<name>
<value>T6</value>
<graphics>
<offset x="-5.0" y="35.0"/>
</graphics>
</name>
<orientation>
<value>0</value>
</orientation>
<rate>
<value>1.0</value>
</rate>
<timed>
<value>false</value>
</timed>
<infiniteServer>
<value>false</value>
</infiniteServer>
<priority>
<value>1</value>
</priority>
</transition>
<transition id="T8">
<graphics>
<position x="405.0" y="210.0"/>
</graphics>
<name>
<value>T8</value>
<graphics>
<offset x="-5.0" y="35.0"/>
</graphics>
</name>
<orientation>
<value>0</value>
</orientation>
<rate>
<value>1.0</value>
</rate>
<timed>
<value>false</value>
</timed>
<infiniteServer>
<value>false</value>
</infiniteServer>
<priority>
<value>1</value>
</priority>
</transition>
<arc id="P0 to T0" source="P0" target="T0">
<graphics/>
<inscription>
<value>Default,1</value>
<graphics/>
</inscription>
<tagged>
<value>false</value>
</tagged>
<arcpath id="000" x="619" y="209" curvePoint="false"/>
<arcpath id="001" x="556" y="102" curvePoint="false"/>
<type value="normal"/>
</arc>
<arc id="P0 to T8" source="P0" target="T8">
<graphics/>
<inscription>
<value>Default,1</value>
<graphics/>
</inscription>
<tagged>
<value>false</value>
</tagged>
<arcpath id="000" x="612" y="222" curvePoint="false"/>
<arcpath id="001" x="421" y="222" curvePoint="false"/>
<type value="normal"/>
</arc>
<arc id="P1 to T5" source="P1" target="T5">
<graphics/>
<inscription>
<value>Default,1</value>
<graphics/>
</inscription>
<tagged>
<value>false</value>
</tagged>
<arcpath id="000" x="235" y="227" curvePoint="false"/>
<arcpath id="001" x="336" y="267" curvePoint="false"/>
<type value="normal"/>
</arc>
<arc id="P2 to T1" source="P2" target="T1">
<graphics/>
<inscription>
<value>Default,1</value>
<graphics/>
</inscription>
<tagged>
<value>false</value>
</tagged>
<arcpath id="000" x="428" y="111" curvePoint="false"/>
<arcpath id="001" x="501" y="177" curvePoint="false"/>
<type value="normal"/>
</arc>
<arc id="P2 to T2" source="P2" target="T2">
<graphics/>
<inscription>
<value>Default,1</value>
<graphics/>
</inscription>
<tagged>
<value>false</value>
</tagged>
<arcpath id="000" x="404" y="110" curvePoint="false"/>
<arcpath id="001" x="346" y="147" curvePoint="false"/>
<type value="normal"/>
</arc>
<arc id="P3 to T4" source="P3" target="T4">
<graphics/>
<inscription>
<value>Default,1</value>
<graphics/>
</inscription>
<tagged>
<value>false</value>
</tagged>
<arcpath id="000" x="417" y="327" curvePoint="false"/>
<arcpath id="001" x="286" y="327" curvePoint="false"/>
<type value="normal"/>
</arc>
<arc id="P3 to T6" source="P3" target="T6">
<graphics/>
<inscription>
<value>Default,1</value>
<graphics/>
</inscription>
<tagged>
<value>false</value>
</tagged>
<arcpath id="000" x="445" y="320" curvePoint="false"/>
<arcpath id="001" x="531" y="282" curvePoint="false"/>
<type value="normal"/>
</arc>
<arc id="T0 to P2" source="T0" target="P2">
<graphics/>
<inscription>
<value>Default,1</value>
<graphics/>
</inscription>
<tagged>
<value>false</value>
</tagged>
<arcpath id="000" x="546" y="102" curvePoint="false"/>
<arcpath id="001" x="431" y="102" curvePoint="false"/>
<type value="normal"/>
</arc>
<arc id="T1 to P0" source="T1" target="P0">
<graphics/>
<inscription>
<value>Default,1</value>
<graphics/>
</inscription>
<tagged>
<value>false</value>
</tagged>
<arcpath id="000" x="511" y="177" curvePoint="false"/>
<arcpath id="001" x="613" y="216" curvePoint="false"/>
<type value="normal"/>
</arc>
<arc id="T2 to P1" source="T2" target="P1">
<graphics/>
<inscription>
<value>Default,1</value>
<graphics/>
</inscription>
<tagged>
<value>false</value>
</tagged>
<arcpath id="000" x="336" y="147" curvePoint="false"/>
<arcpath id="001" x="234" y="213" curvePoint="false"/>
<type value="normal"/>
</arc>
<arc id="T4 to P1" source="T4" target="P1">
<graphics/>
<inscription>
<value>Default,1</value>
<graphics/>
</inscription>
<tagged>
<value>false</value>
</tagged>
<arcpath id="000" x="282" y="312" curvePoint="false"/>
<arcpath id="001" x="230" y="234" curvePoint="false"/>
<type value="normal"/>
</arc>
<arc id="T5 to P3" source="T5" target="P3">
<graphics/>
<inscription>
<value>Default,1</value>
<graphics/>
</inscription>
<tagged>
<value>false</value>
</tagged>
<arcpath id="000" x="346" y="267" curvePoint="false"/>
<arcpath id="001" x="419" y="318" curvePoint="false"/>
<type value="normal"/>
</arc>
<arc id="T6 to P0" source="T6" target="P0">
<graphics/>
<inscription>
<value>Default,1</value>
<graphics/>
</inscription>
<tagged>
<value>false</value>
</tagged>
<arcpath id="000" x="541" y="282" curvePoint="false"/>
<arcpath id="001" x="614" y="230" curvePoint="false"/>
<type value="normal"/>
</arc>
<arc id="T8 to P1" source="T8" target="P1">
<graphics/>
<inscription>
<value>Default,1</value>
<graphics/>
</inscription>
<tagged>
<value>false</value>
</tagged>
<arcpath id="000" x="411" y="222" curvePoint="false"/>
<arcpath id="001" x="236" y="222" curvePoint="false"/>
<type value="normal"/>
</arc>
</net>
</pnml>

"""


places = re.findall(
    r"<place id=\"(.*?)\">.*?<name>\s*<value>(.*?)</value>.*?<initialMarking>\s*<value>Default,(\d+)</value>.*?<capacity>\s*<value>(\d+)</value>",
    pml_string,
    re.DOTALL
)


transitions = re.findall(
    r"<transition id=\"(.*?)\">.*?<name>\s*<value>(.*?)</value>",
    pml_string,
    re.DOTALL
)

# Armazenar lugares e transições em listas de dicionários
elementos = []
for place_id, name, default, capacity in places:
    elementos.append({
        "Type": "Place",
        "ID": place_id,
        "Name": name,
        "Default": default,
        "Capacity": capacity
    })

for trans_id, name in transitions:
    elementos.append({
        "Type": "Transition",
        "ID": trans_id,
        "Name": name,
        "Default": "N/A",  # Sem valor padrão na transição
        "Capacity": "N/A"  # Sem capacidade na transição
    })

# Captura os arcos usando regex
arcos = re.findall(
    r"<arc id=\"(.*?)\" source=\"(.*?)\" target=\"(.*?)\">.*?<inscription>\s*<value>(.*?)</value>",
    pml_string,
    re.DOTALL
)

# Armazenar arcos em lista de dicionários
lista_arcos = []
for arc_id, source, target, inscription in arcos:
    lista_arcos.append({
        "ID": arc_id,
        "Source": source,
        "Target": target,
        "Inscription": inscription
    })

# Função para imprimir os arcos
def valida_estado_inicial():
    # Solicita entrada do usuário
    estado = input("Digite o estado (P0, P1, P2 ou P3): ").upper()
    
    # Verifica se o estado existe na rede
    if estado not in ["P0", "P1", "P2", "P3"]:
        print("Estado inexistente")
        return None
    
    # Verifica se é o estado inicial (Default = 1)
    for elem in elementos:
        if elem['Type'] == 'Place' and elem['ID'] == estado:
            if elem['Default'] == "1":
                print(f"Estado inicial: {estado} - Default: {elem['Default']}")
                print(f"\nArcos da Rede de Petri para o estado {estado}:")
                print("------------------------")
                
                # Procura arcos que partem do estado inicial
                for arco in lista_arcos:
                    if arco['Source'] == estado:
                        print(f"ID: {arco['ID']}")
                        print(f"De: {arco['Source']}")
                        print(f"Para: {arco['Target']}")
                        print(f"Inscrição: {arco['Inscription']}")
                        print("------------------------")
                
                return estado  # Retorna o estado válido
            else:
                print(f"Estado inválido: {estado} - Default: {elem['Default']}")
                return None
    
    return None

def mapear_transicoes():
    # Dicionário que vai armazenar as transições possíveis para cada estado
    transicoes_possiveis = {}
    # Dicionário que vai armazenar o estado destino para cada par estado-transição
    mapa_destinos = {}
    
    # Primeiro, inicializa o dicionário de transições para cada lugar (estado)
    for elem in elementos:
        if elem['Type'] == 'Place':
            transicoes_possiveis[elem['ID']] = []
    
    # Para cada arco, mapeia as transições possíveis
    for arco in lista_arcos:
        source = arco['Source']
        target = arco['Target']
        
        # Se o source é um Place (estado), então target é uma transição possível
        if source.startswith('P'):
            transicoes_possiveis[source].append(target)
        
        # Se o source é uma Transition, então estamos mapeando o destino da transição
        if source.startswith('T'):
            mapa_destinos[source] = target
    
    print("\nMapeamento de transições:")
    for estado, transicoes in transicoes_possiveis.items():
        print(f"\nEstado {estado} pode fazer as seguintes transições:")
        for transicao in transicoes:
            destino = mapa_destinos[transicao]
            print(f"- {transicao} -> {destino}")
    
    return transicoes_possiveis, mapa_destinos

# Modifica a função transicao_estado para usar o mapeamento automático
def transicao_estado(estado, transicoes_possiveis, mapa_destinos):
    print(f"\nTransições possíveis a partir do estado {estado}:")
    for transicao in transicoes_possiveis[estado]:
        print(f"- {transicao} -> {mapa_destinos[transicao]}")
    
    while True:
        transicao = input("\nDigite a transição desejada: ").upper()
        if transicao in transicoes_possiveis[estado]:
            print(f"Executando transição {transicao}")
            
            novo_estado = mapa_destinos[transicao]
            
            # Atualiza os valores Default
            for elem in elementos:
                if elem['Type'] == 'Place' and elem['ID'] == estado:
                    elem['Default'] = "0"
                    break
            
            for elem in elementos:
                if elem['Type'] == 'Place' and elem['ID'] == novo_estado:
                    elem['Default'] = "1"
                    break
            
            print(f"Transição concluída. Novo estado: {novo_estado}")
            return novo_estado
        else:
            print(f"Transição inválida. Escolha uma das transições possíveis.")

# Modifica o loop principal para usar o novo mapeamento
while True:
    # Gera o mapeamento de transições
    transicoes_possiveis, mapa_destinos = mapear_transicoes()
    
    estado_atual = valida_estado_inicial()
    if estado_atual:
        novo_estado = transicao_estado(estado_atual, transicoes_possiveis, mapa_destinos)
    
    continuar = input("\nDeseja verificar outro estado? (S/N): ").upper()
    if continuar != 'S':
        break


#TODO: Buscar o parametro / Orientação
#TODO: Buscar peso do arco (seta)
#TODO: Refazer todo o processo de transição olhando apenas o XML e não a imagem


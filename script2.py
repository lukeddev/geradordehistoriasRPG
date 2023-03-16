import openai
import random

openai.api_key = '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'

quantos = int(input('Quantos herois participarão dessa aventura? digite um número inteiro de 1 a 10: '))

locais = [
    'floresta',
    'acampamento de bandidos',
    'labirinto subterrâneo',
    'cidade flutuante nas nuves',
    'navio fantasma amaldiçoado',
    'fortaleza de gelo nas montanhas',
    'pântano assombrado',
    'Iiha com um vulcão acordado',
    'cidade abandonada no deserto',
    'masmorra mágica, onde as paredes se movem, o tempo corre de maneira diferente e os aventureiros devem resolver quebra-cabeças para encontrar o caminho certo.'
]
onde = random.choice(locais)

missão = [
    'Investigar um mistério sombrio',
    'Proteger um comerciante',
    'Proteger um nobre',
    'Encontrar um objeto mágico poderoso a pedido de um bruxo',
    'Resgatar um refém importante',
    'Defender um caravana de comerciantes',
    'Descobrir um segredo antigo escondido',
    'Escoltar um emissário ou líder político importante para uma conferência de paz',
    'Impedir um ritual mágico malévolo',
    'Ajudar uma figura importante a restaurar a justiça ou a vingar uma injustiça',
]
fazer = random.choice(missão)
chefão = [
    'dragão antigo e poderoso',
    'Um lich malévolo',
    'demônio das profundezas',
    'titã colérico que foi despertado de um sono milenar',
    'necromante obscuro',
    'deus antigo e esquecido',
    'rei tirânico, com um exercito poderoso',
    'Um gênio maligno',
    'Um arquimago insano',
    'Um golem gigante',
]
boss = random.choice(chefão)
aventura = ('Crie uma aventura de rpg para {} aventureiro, ele deve ir até {}, e fazer {} O '
            'inimigo final será um {}.A historia deve ser balanceada de acordo com a quantidade de aventureiros descrito a cima' .format(quantos, onde, fazer, boss))

completion = openai.Completion.create(
    engine = "text-davinci-003",
    prompt = aventura,
    max_tokens=2018,
    n=1,
    temperature=1.0)
reponse = completion.choices[0].text
print(reponse)

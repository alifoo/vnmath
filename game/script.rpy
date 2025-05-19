define Player = Character("Você")
define Reiji = Character("Reiji", color="#c62828")
define Aika = Character("Aika", color="#f48fb1")
define AikaSpirit = Character("Espírito de Aika", color="#e1bee7")
define Sayu = Character("Sayu", color="#9575cd")
define Shizuru = Character("Shizuru", color="#90a4ae")
define Captain = Character("Capitão", color="#ffb300")
default went_to_aika_room = False
default went_to_interviews = False
default Hidden = Character("???", color="#8e6666")


label start:
    play music "audio/default.ogg"
    scene bg nightship with fade

    "Certa noite, um navio com diversos passageiros passa por uma terrível tempestade."
    "Cercados pelas vastas trevas do oceano, uma presença intimidadora, abissal, se aproxima."
    
    "Você, que ainda estava acordado, nota a silhueta da criatura no mar."

    Player "Mas o que é aquilo?"
    play sound "audio/flash.ogg"
    scene bg white with fade
    "Em seguida, um clarão acontece seguido de um estrondo, e você se vê perdendo a consciência."

    "Uma voz ecoa em sua mente. Uma voz antiga, sem emoção, profunda."
    "{color=#f00}Quando a morte tocar sua carne, o fio será puxado...{/color}"
    "{color=#f00}O fio se curvará ao suspiro da morte...{/color}"
    "{color=#f00}A maldição...{/color}"
    "{color=#f00}Seu retorno trará a memória, o eco do futuro, o peso...{/color}"
    "{color=#f00}A língua que ousar revelar será selada pelo próprio fardo...{/color}"

    "A voz enfim cessa, o silêncio toma conta do ambiente."
    scene bg black with fade
    scene bg infirmary with fade
    "Depois de um breve momento, você finalmente acorda em um leito da enfermaria do navio. Tudo parece ter voltado ao normal."
    
    show aika normal 1 with fade
    Aika "Finalmente acordou. Você está bem?"
    Aika "Todos os outros envolvidos no incidente já acordaram, você foi o último."
    Aika "Eu sou Aika. Também acabei desmaiando durante o ocorrido noite passada."
    Player "Ah... você também viu aquele clarão?"
    Aika "Sim. Algum fenômeno causou aquilo. Porém, ao contrário do que estão dizendo, não foi um de nossos experimentos."
    Player "Ah, é verdade, você é está entre aqueles cientistas à bordo. Sabe se mais gente sofreu com isso?"
    Aika "Você, eu e mais 3 pessoas. Os outros já saíram, só você ainda não tinha acordado."
    Aika "Não se preocupe, vamos investigar o que aconteceu. É bom saber que está bem."
    Aika "Preciso voltar ao trabalho agora. Até mais."
    Player "Ok, até."
    hide aika with dissolve

    "Você retorna à sua cabine."
    scene bg cabin with fade

    Player "O que foi aquele clarão? Eu não mencionei a voz que ouvi para não soar estranho... mas será que os outros também a ouviram?"
    Player "Mas se sim, por que nada foi dito sobre?"
    Player "Tenho que investigar isso a fundo... Mas ainda me sinto estranhamente cansado."
    Player "Vou descansar um pouco antes disso."
    scene bg black with fade

    "Você acorda algumas horas depois e vai até o lado de fora."
    scene bg ship with fade
    "Gritos são ouvidos pelo navio. Algo anormal parece ter acontecido."
    "Parecem estar vindo de um dos laboratórios. Você vai até o local."

    scene bg shiplab with fade

    Player "O que aconteceu aqui?"
    show shizuru normal with fade
    Shizuru "Uma das pesquisadoras a bordo parece ter morrido no laboratório vítima de uma explosão."
    Shizuru "Ela esteve presente no acidente de anteontem. Não se sabe o que aconteceu, mas talvez estivesse cansada demais."
    Shizuru "Quando ouvimos a explosão, viemos ver. Reiji estava tentando ajudar, mas os danos foram fatais."
    Player "Me deixe ver o corpo."

    Shizuru "O local foi fechado pelo capitão para que não houvesse adulteração na cena do crime. Só pode ir até lá se for médico ou oficial de segurança."
    menu:
        "Eu sou um detetive.":
            Shizuru "É mesmo? Tudo bem. Nesse caso, me acompanhe."
        "Justamente por isso eu deveria ir até lá.":
            Shizuru "Certo, me acompanhe."
    hide shizuru normal with dissolve

    "Você chega na cena do crime."

    show captain normal with fade

    Captain "Os únicos que estiveram aqui hoje foram Reiji, Aika e Sayu, os 3 pesquisadores a bordo."
    Captain "Não há vestígios de assassinato, mas até onde eu a conhecia, tal descuido não é algo que Aika faria, senhor."
    Captain "Talvez hoje realmente fosse seu dia, pois justamente hoje ela veio trabalhar de manhã, quando não precisava."
    Captain "Como você é um detetive, te dou acesso a quaisquer informações que precisar para solucionar isso."
    Captain "Por conta da tempestade, ainda não pude contatar a central sobre o ocorrido."

    Player "{i}{color=#3cb371}Aika era muito cuidadosa. Se alguém como ela cometeu um erro, ou estava exausta... ou não foi um acidente.{/i}"
    Player "{i}{color=#3cb371}Ela até mesmo veio trabalhar antes do horário, então não estava exausta, portanto não foi um acidente.{/i}"

    menu:
        "Gostaria de analisar o quarto da vítima.":
            jump cena5_1
        "Gostaria de conversar com os outros que estiveram no laboratório.":
            jump cena5_2

    hide captain normal with dissolve
    return

label cena5_1:
    scene bg aikaroom with fade
    "O quarto de Aika parecia impecável. Em cima da escrivaninha, um diário, a única pista."

    "Você se aproxima da escrivaninha e abre o diário em sua última página escrita."

    "12 de abril de 2025"
    "'Depois do ocorrido de anteontem, aquele cara vem me fazendo muitas perguntas.'"
    "'Eu acordei com meus sentidos muito mais aguçados que o normal, como se fosse um superpoder, e sinto muita hostilidade vindo dele.'"
    "'Ele disse que também teve o sonho.'"
    "{i}{color=#3cb371}'Se todos os envolvidos naquilo tiveram o sonho, e os que tiveram o sonho ganharam superpoderes, então como ele teve o sonho, ganhou superpoderes, assim como eu!{/color}{/i} Mas qual?'"

    Player "Superpoderes... então sua morte realmente pode ter sido um assassinato, mas encoberto por algo sobrenatural!"

    $ went_to_aika_room = True

    if went_to_interviews is True:
        Player "{i}{color=#3cb371}Se Aika fala em seu diário que um homem que fazia perguntas também tinha poderes e Reiji diz ter conversado com ela, então ele deve ser quem ela se referiu no diário.{/color}{/i}"
        Player "O dia passou rápido e já está quase escurecendo. O refeitório é próximo ao laboratório, irei até lá para ver se encontro alguma pista."
        jump cena_7
    else:
        Player "O ideal agora é conversar com os outros presentes no laboratório."
        jump cena5_2

        

label cena5_2:
    scene bg shiplab2 with fade
    Player "Reiji, podemos conversar?"

    show reiji normal with fade
    
    Reiji "Sobre o ocorrido..."
    Reiji "Falei com Aika ontem. Ela estava... tensa. Comentou que achava estar sendo observada."
    Reiji "Hoje de manhã, eu estava no laboratório com ela e Sayu. Me afastei por alguns segundos, ouvi o som do vidro se partindo e, quando me virei, o becker tinha explodido nas mãos dela."
    Reiji "Se Sayu sabia de algo, escondeu de todos. Você devia conversar com ela."

    Player "Obrigado, irei conversar com Sayu."
    hide reiji normal with dissolve

    "Você se aproxima de Sayu e pergunta sobre o ocorrido."
    show sayu normal with fade
    Sayu "Hoje cedo, encostei nela acidentalmente e... tive uma visão."
    Sayu "Algo sombrio, uma explosão. Fiquei tensa durante toda a manhã. Queria alertá-la, mas Reiji estava sempre por perto."
    Sayu "Ele parecia nervoso demais."
    Sayu "Aika parecia estar congelada segundos antes da explosão, parecia que nada ao seu redor além do líquido no becker se mexia, como se o tempo tivesse parado para ela."

    "Você escuta o relato de Sayu e volta à sua cabine, enquanto reflete sobre os acontecimentos."
    hide sayu normal with dissolve

    Player "{i}{color=#3cb371}Se Reiji disse a verdade, então Sayu sabia de algo e escondeu de todos.{/i}"
    Player "{i}{color=#3cb371}Se Sayu disse a verdade, então a causa da morte realmente foi sobrenatural.{/i}"
    Player "{i}{color=#3cb371}Pelo seu tom e sua expressão, Sayu com certeza não mentia, então a morte foi um acidente forçado por um poder.{/i}"

    $ went_to_interviews = True

    if went_to_aika_room is False:
        Player "É melhor eu vasculhar a cabine de Aika em busca de informações."
        jump cena5_1
    else:
        Player "{i}Se Aika fala em seu diário que um homem que fazia perguntas também tinha poderes e Reiji diz ter conversado com ela, então ele deve ser quem ela se referiu no diário.{/i}"
        Player "O dia passou rápido e já está quase escurecendo. O refeitório é próximo ao laboratório, irei até lá para ver se encontro alguma pista."
        jump cena_7


label cena_7:
    scene bg refeitorio with fade
    "Você chega ao refeitório e olha ao redor. Está vazio."
    Player "Sem informações muito relevantes sobre o ocorrido. Será que foi realmente um assassinato? Preciso investigar melhor."
    scene bg black with fade
    "De repente, as luzes se apagam."
    "As trevas tomam conta do lugar, um silêncio mortal toma conta do já silencioso refeitório, e passos são ouvidos se aproximando."
    "O até então vazio refeitório não estava tão vazio assim."
    Player "Quem está aí?"
    Hidden "Você também estava envolvido no incidente, então também ganhou poderes, não é?"
    Hidden "Infelizmente para você, eu não quero nenhum de vocês no meu caminho, não importa qual seja o seu poder!"

    Player "É questão de tempo até virem aqui, e você será o único neste local!"
    Player "Alguém! O assassino está no refeitório!"

    Hidden "Ninguém vai te ouvir. Não percebeu ainda?"

    "Você tenta se mover, mas percebe que algo o impede."
    "De repente, nada pode ser ouvido, nada pode ser sentido."
    "O ar ao seu redor parece parado, e num instante, seu coração para também."

    Hidden "Menos um empecilho."

    "Tudo está escuro."
    "Você não consegue sentir nada."
    "Falar nada."
    "Ver nada."
    "Até que então um fio vermelho cruza seu campo de visão."

    "'Este é o seu destino.'"
    jump cena_8


label cena_8:
    scene bg refeitorio with fade
    "Você acorda de repente, novamente no refeitório."

    Player  "O-o que foi isso? Um sonho? Pareceu tão real."
    Player "Eu estou de volta no refeitório vazio... Isso pode estar relacionado ao meu poder."
    scene bg black with fade
    "De repente, as luzes se apagam."
    "As trevas tomam conta do lugar, um silêncio mortal toma conta do já silencioso refeitório, e passos são ouvidos se aproximando."
    "O até então vazio refeitório não estava tão vazio assim."

    Player "Eu já vivenciei isso antes!"

    menu:
        "Ficar parado, sem reagir.":
            jump cena_8_1
        "Tentar fugir":
            jump cena_8_2

label cena_8_1:
    scene bg black with fade
    Hidden "Achei que fosse tentar fugir."
    Player "Por que está fazendo isso?"

    Hidden "Você já vai morrer mesmo, então tanto faz."
    Hidden "Sabe... tem várias pessoas que ganharam poderes naquele incidente, e isso pode causar problemas não só para o mundo, mas para mim. Eu não quero nenhum de vocês no meu caminho."

    "Você tenta fugir, e, novamente, nada pode ser sentido, nada pode ser ouvido, sua voz já não sai. Seu coração para novamente."

    Hidden "Esse é o meu poder. Dessa vez, foi seu coração. Da última, foi o corpo de Aika."

    "Tudo fica preto. O fio vermelho aparece novamente"
    "A maldição..."
    "Seu retorno trará a memória, o eco do futuro, o peso..."

    jump cena_9

label cena_8_2:
    "Você tenta correr, mas assim que se levanta, algo estranho acontece: o ar ao seu redor parou. Você não consegue mais se mover."
    scene bg black with fade

    Hidden "Bem esperto de sua parte tentar fugir. É uma pena que não tenha dado tempo de descobrir o seu poder."

    menu:
        "Por que faz isso?":
            Hidden "Porque preciso de todos vocês, que também ganharam poderes, mortos."

    "Tudo fica preto. O fio vermelho aparece novamente"
    "A maldição..."
    "A língua que ousar revelar será selada pelo próprio fardo..."

label cena_9:
    scene bg refeitorio with fade
    "Você acorda de repente, novamente no refeitório."
    Player "Devo fugir o mais rápido possível."

    "Dessa vez, você consegue sair do refeitório e correr para os corredores do navio."

    Player "Preciso pensar! Qual deve ser o poder dele?"

    menu:
        "Parar o tempo":
            Player "Seu poder deve ser o de parar o tempo."
            Player "Porém, tem algo estranho... se seu poder não tivesse limites, ele teria parado o tempo antes de eu sair do refeitório, mas não fez isso."
            Player "Então seu poder deve ter limite de distância."
            Player "Além disso, se seu poder não tivesse limite de tempo de atuação, ele me deixaria preso o tempo todo enquanto conversávamos."
            Player "Ele não fez isso, então seu poder tem limite de tempo."
        "Controlar pessoas":
            Player "Talvez o poder dele seja controlar pessoas. Assim, ele poderia impedir os meus movimentos."
            Player "Mas não faz muito sentido... Ele não impediu que eu corresse dessa vez."
            Player "Seu poder deve ser algo ainda mais extraordinário, como parar o tempo. Mas deve ter limitações, como a distância."
            Player "Além disso, se seu poder não tivesse limite de tempo de atuação, ele me deixaria preso o tempo todo enquanto conversávamos."
            Player "Ele não fez isso, então seu poder tem limite de tempo."
    
    Player "A lista de todos os envolvidos no acidente deve ajudar a descobrir o assassino! O capitão pode me fornecer ela."

    "Você escapou com sucesso e foi até o capitão."
    show captain normal with fade

    Player "Capitão! Por favor, preciso da lista de envolvidos no acidente."
    Captain "Aqui está, detetive."

    "
    Lista de envolvidos no incidente do dia 10 de abril de 2025
    Player
    Reiji
    Aika
    Sayu
    Shizuru
    "

    Player "Reiji e Sayu já foram entrevistados."
    Player "Aika foi morta por possuir um poder, mas ainda não me comuniquei com Shizuru. Preciso ir até ele."

    jump cena_10

label cena_10:
    "Você procura por Shizuru no cruzeiro e o encontra."

    Shizuru "Já sei o que você quer, mas antes preciso confirmar algo: você também teve uma visão depois de perder a consciência?"

    menu:
        "Sim...":
            Shizuru "Quero ficar fora disso. Se tiver algo com que precise de ajuda, faça um pedido e não me incomode mais. Meu poder, para você saber, é me comunicar com os mortos."
        "Então você também...":
            Shizuru "Quero ficar fora disso. Se tiver algo com que precise de ajuda, faça um pedido e não me incomode mais. Meu poder, para você saber, é me comunicar com os mortos."
    
    Player "Se comunicar com os mortos? Como assim?"
    Shizuru "É como eu disse... ontem, encontrei um pássaro morto no convés. Ao chegar perto, consegui me comunicar com o seu espírito."
    Shizuru "Eu sou extremamente cético com essas coisas. Mas não havia engano. Eu realmente ouvi a 'voz daquele espírito' quando perguntei a ele 'o que aconteceu?'."
    Shizuru "Acredite se quiser."

    Player "Shizuku... Essa pode ser a solução que precisamos. Venha comigo."

    jump cena_11

label cena_11:
    "Você e Shizuru se aproximam do corpo da vítima, no local interditado."

    Shizuru "Preciso do máximo de informações possíveis para formular a pergunta. Só tenho direito a uma, e ela precisa ser certeira."
    "Você conta tudo que sabe a Shizuru."
    Shizuru "{i}Eu, Reiji e Sayu eram suspeitos.{/i}"
    Shizuru "{i}Provando minha inocência, eu deixarei de ser suspeito,{/i}"
    Shizuru "{i}Então Reiji e Sayu são.{/i}"

    Shizuru "Se Aika conversou tanto com Reiji e Sayu, então talvez tivesse usado seus poderes em algum deles e tivesse uma pista de sua morte."
    Shizuru "Esta será minha pergunta."

    "Shizuru se ajoelha próximo ao cadáver, fecha os olhos, e pergunta:"
    Shizuru "Tu, que sabes mais que todos sobre si mesma e que revelou aos outros seus poderes, responda-me:"
    Shizuru "O que seus poderes revelaram?"

    AikaSpirit "O perigo vinha de um único homem. O desespero vinha dela."

    Shizuru "É isso. Agora me deixe fora dessa história."

    Player "Se o perigo vinha de um homem e o único homem lá era Reiji, então o perigo vinha dele."
    Player "Aika já falou sobre ele em seu diário, então ele deve ser o assassino!"
    Player "Vou falar com Reiji sobre isso. Se fingir que já sei de tudo, posso fazê-lo confessar se for verdade."

    jump cena_12

label cena_12:
    "Ao sair procurando por Reiji, você decide passar novamente próximo ao refeitório. Dessa vez, com mais cuidado."

    "Sayu e Reiji estão conversando quando você chega. Você nota uma expressão de raiva no rosto de Reiji."

    menu:
        "Saia de perto dele, Reiji é o assassino!":
            "Ao dizer isso, você congela e logo percebe que Reiji não está mais ali."
        "Então você é o assassino de Aika, e também aquele que tentou me matar!":
            "Ao ouvir isso, Reiji te olha por um instante. Você congela e logo percebe que Reiji não está mais ali."
        
    Player "Droga! Temos que encontrá-lo."
    Player "{i}O refeitório só dá acesso ao convés e à proa. Ele não irá para onde não pode se esconder, então foi ao convés.{/i}"
    Player "{i}Se ele tem limitações quanto ao tempo de uso, então tem que esperar para usar novamente seu poder.{/i}"
    Player "{i}Ele acabou de o usar, então temos um intervalo até ele poder usá-lo de novo.{/i}"

    Player "Eu vou até o convés e vou encontrar formas de pará-lo."
    Sayu "Vou avisar Shizuru e o capitão."

    "Enquanto isso, no convés..."

    show reiji normal with fade
    Reiji "Preciso achar um jeito de matar esses dois o mais rápido possível. Assim que meu poder recarregar, o uso para isso. Só mais uma hora."
    Reiji "{i}Virão me procurar, mas se eu usar meu poder irei os matar, e com certeza irei usar. Logo, os matarei!{/i}"

    hide reiji normal with dissolve
    jump cena_13

label cena_13:
    "Algum tempo depois, no convés..."
    "O céu começava a ficar escuro. A noite chegava junto de um terrível aguaceiro, e o convés era iluminado apenas pelos relâmpagos: a eletricidade havia sido cortada por alguém, possivelmente Reiji."

    menu:
        "É questão de tempo até te encontrarem!"
        "Eu sei que você está aí. Se entregue!"

    "O convés está quieto a não ser pelo sereno so da chuva. Um relâmpago revela uma silhueta emergindo das trevas."
    "Você corre em direção a ela, que de perto se torna identificável: era Reiji!"
    "Enquanto você agarra um de seus braços, o cintilante brilho de uma lâmina corta o ar enquanto ele move o outro em direção ao seu pescoço..."
    "...uma terrível queimação o atinge enquanto seu corpo fifca cada vez mais pesado e sua visão se torna cada vez mais turva."
    "O fio vermelho aparece novamente."
    
    "Tudo está escuro..."
    "Quando a morte tocar sua carne, o fio será puxado..."
    "O fio se curvará ao suspiro da morte..."
    jump cena_14

label cena_14:
    "no convés..."
    "O céu começava a ficar escuro. A noite chegava junto de um terrível aguaceiro, e o convés era iluminado apenas pelos relâmpagos: a eletricidade havia sido cortada por alguém, possivelmente Reiji."
    Player "{i}Se eu for fireto até Reiji, ele vai sacar a lâmina. Se ele fizer isso, será para me apunhalar.{/i}"
    Player "{i}Então se eu for até ele, serei apunhalado.{/i}"
    Player "Não devo fazer isso."

    menu:
        "Não agir":
            "{i}Se eu for até ele, ele apunhalará alguém. Então não vou até ele, lógicamente ele não apunhalará ninguém.{/i}"
            jump cena_15_1
        "Contornar o local para ativar a iluminação de volta.":
            "{i}Se eu contornar o local, posso reativar a iluminação e deixar Reiji exposto. Farei isso, assim Reiji não poderá mais escapar.{/i}"
            jump cena_15_2

label cena_15_1:
    "De repente, uma porta se abre do outro lado do convés e de lá saem Sayu e o capitão"
    show sayu normal with fade
    Sayu "Eu trouxe o capitão! Vamos encontrar o assassino!"
    hide sayu normal with dissolve
    "Antes que você pudesse dizer qualquer coisa, o capitão corre em sua direção enquanto Sayu segue reto sem saber que naquela direção encontraria seu destino."
    "Uma sombra emerge do convés e a agarra por trás..."
    "Antes que ela tivesse tempo para reagir, uma lâmina atinge seu peito, e ela é atirada, já sem vida, ao chão."
    Player "Mais uma vítima!"
    Player "{i}Se eu ir até a sala de segurança, vou conseguir uma arma.{/i}"
    Player "{i}Se eu tiver uma arma, posso dar fim nesse pesadelo.{/i}"
    Player "{i}Então tenho que ir até a sala de segurança!{/i}"

    jump cena_16

label cena_15_2:
    "O local onde Reiji está é contornado e a iluminação é ligada novamente."
    "Reiji se vê desnorteado e sem ter para onde correr, e a chegada de Sayu e do capitão reforça este sentimento."
    
    show reiji normal with fade
    Reiji "Até parece que eu vou me render a vocês!"
    Reiji "Nem morto! Morto... Morto..."
    Reiji "Não vou conseguir matar todos eles, e meu poder não se recuperara a tempo. Não tenho para onde ir, e se eu me entregar, passarei o resto da minha vida na cadeia..."
    Reiji "Não... Não, não, não! não!"
    Reiji "Hahahahahahaha!"
    Reiji "Sim, eu parei o tempo para que Aika derramasse aquele produto em quantidade muito maior que o esperado para que ocorresse uma explosão e ela morresse,"
    Reiji "e iria ter matado cada um de vocês que tem poderes também."
    Reiji "Com estes poderes, vocês apresentam ao mundo uma ameaça muito maior que qualquer bandido, e eu preciso acabar com vocês um por um!"
    hide reiji normal with dissolve

    "Num acesso de loucura e frente à pressão criada por aqueles ao seu redor, Reiji exerce seu último ato de egoísmo contra o mundo"
    "Saca sua faca pela última vez, mas desta vez não contra Sayu, não contra você, não contra o capitão..."
    "Mas contra si mesmo."
    "Dentro de poucos segundos, o causador de toda a tragédia está no chão. Imóvel."
    "O pesadelo chegara ao fim, e o caso estava resolvido."

label cena_16:
    # não tem um cenário da sala de segurança?
    "Na sala de segurança..."

    "Você encontra uma espingarda, mas junto de você chega também Reiji, que tenta matá-lo antes que pegue a arma."
    "A faca é acertada em você uma vez, mas ao custo de ser jogada para longe."
    "Em questão de segundos a arma está em suas mãos, e dentro do mesmo tempo, o assassino está no chão. Imóvel."
    "O pesadelo chegara ao fim, e o caso estava resolvido."
    
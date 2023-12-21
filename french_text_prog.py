import string
import sys
import codecs


with codecs.open(sys.argv[0], encoding='latin1') as file:
 
    inStr = file.read()         
 
file.close()

with codecs.open(sys.argv[1], encoding='latin1') as engFile:
    engInStr = file.read()

##French = 'a reine était au bain, iIl y avait dans le temps un roi et une reine qui se répétaient chaque jour – Ah ! Si seulement nous avions un enfant ! Mais ils nen avaient toujours pas.Un jour que ll advint quune grenouille sauta de leau pour savancer vers elle et lui parler Ton vœu sera exaucé, lui annonça-t-elle ; avant un an, tu mettras une fille au monde. Ce que la grenouille avait dit se produisit, et la reine donna naissance à une fille. Lenfant était tellement jolie que le roi ne se tenait plus de joie et fit donner une grande fête. Il ne se contenta pas dy inviter ses parents, amis et connaissances, mais il voulut aussi que les fées y eussent part, afin quelles fussent favorables et bienveillantes à lenfant.On en comptait treize dans le royaume, mais comme il ny avait que douze assiettes dor au palais, pour leur servir le festin, il fallut en laisser une chez elle. Celle qui navait pas été invitée et qui voulait se venger. Sans un salut ni seulement un regard pour personne, elle lança à voix haute sur le berceau cette parole : « La princesse, quand elle aura quinze ans, se piquera avec un fuseau et tombera morte. Sans un mot de plus, elle fit demi-tour et quitta la chambre. Hier, avec Olivier, Leyla et deux de ses amis, Yann et Paol, on est allés passer un après-midi à laccrobranche de Morieux, pas très loin de Paimpol, en Bretagne. “Accrobranche” est une activité de plein air sportive qui consiste à se déplacer darbre en arbre dans une forêt spécialement aménagée avec des ponts, des obstacles déquilibre, des tyrolienne Voici comment ça sest passé Depuis longtemps, nous voulions faire cette activité avec les amis de Leyla qui sont de grands fans descalade, et comme la météo sannonçait très bonne quelques jours auparavant – mention spéciale pour le verbe “s’annoncer”, vous verrez pourquoi plus tard – nous avons lancé les invitations ! Le jour J, les amis de Leyla nous ont rejoints chez nous, puis nous avons pris la route. Nous sommes arrivés aux alentours de 13h30, et malheureusement il pleuvait déjà assez fort ! En fait, comme cest souvent le cas, la météo sétait complètement trompée et nous avons eu de la pluie toute la journée. Donc, nous sommes allés nous abriter pour manger nos sandwichs en se séchant. On était rassasiés et près pour laventure à 14h. On a commencé par mettre léquipement avec laide du moniteur, prénommé Louis. Au moment du briefing, on a (ré)appris lutilité de chaque élément du baudrier : les deux mousquetons pour être sûr de toujours être bien accroché et sécurisé, la poulie à nutiliser que sur les tyroliennes Puis linitiation, quon a passée avec aise car ce nétait pas la première fois quon faisait un parc de ce genre. on arrive au moment tant attendu : la grimpe ! On commence en séchauffant par un petit parcours, pas très haut, pas très compliqué, mais déjà très sympa ! On se tortille à travers les petits obstacles, minuscules pour nous car le parcours est accessible aux enfants dès 7 ans, en rigolant et en passant un bon temps. Accessoirement, en sortant de ce parcours-là, on a réalisé quil faisait quand même très chaud, malgré les averses régulières ! Cétait peut-être lié au fait quon commençait réellement à se dépenser. On fait suivre ce parcours par directement un autre, et puis encore un autre, progressivement de plus en plus complexe, et je constate avec plaisir que jarrive à suivre la cadence de Leyla et ses amis – jétais un peu anxieuse dêtre complètement à la traîne, voir de rester bloquée sur certains obstacles. Il y a aussi une autre raison pour laquelle on est allés à ce parc-là : Leyla avait vraiment envie de faire le, qui est un saut en chute libre de 17 mètres de haut ! Cest dingue ! Imaginez une grande tour en bois. On vous attache à un mécanisme qui va bien sûr freiner la chute. Enfin, cest ce que vous comprenez Mais entre comprendre et internaliser linformation  Après, vous marchez jusquau bord, vous vous tournez pour être dos au vide. Et vous vous laissez tomber en arrière Lhorreur totale'

punc_French = inStr.translate(str.maketrans('','',string.punctuation))
lower_French = punc_French.lower()
new_French = lower_French.casefold()
new_French = new_French.replace("’"," ")
new_French = new_French.replace("é", "e")
new_French = new_French.replace("è", "e")
new_French = new_French.replace("ê","e")
new_French = new_French.replace("ë","e")
new_French = new_French.replace("à", "a")
new_French = new_French.replace("â", "a")
new_French = new_French.replace("î", "i")
new_French = new_French.replace("ï", "i")
new_French = new_French.replace("ô", "o")
new_French = new_French.replace("û", "u")
new_French = new_French.replace("ï", "i")
new_French = new_French.replace("ç", "c")
new_French = new_French.replace("û", "u")
new_French = new_French.replace("œ", "oe")
new_French = new_French.replace("œ", "oe")

lower_English = str.casefold(engInStr)
New_English = lower_English.translate(str.maketrans('','',string.punctuation))

print(new_French)



#set up lists to hold the counts of the characters
alphabet = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
0 = a 
1 = b 
2 = c
3 = d 
4 = e 
5 = f 
6 = g
7 = h 
8 = i 
9 = j 
10 = k 
11 = l 
12 = m 
13 = n 
14 = o 
15 = p 
16 = q 
17 = r
18 = s 
19 = t 
20 = u 
21 = v 
22 = w 
23 = x 
24 = y
25 = z 

alphabet = '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)

counter_a = 0
 
for i in range(0,26):
    str.count(i) = counter_i + 1
    if str.count(i) == 0:
    counter_i == 1
    

print("Hello Conor")
total = len(string)

prob_a = str.count(a)/ len(string)
prob_b = str.count(b)/ len(string)
prob_c = str.count(c)/ len(string)
prob_d = str.count(d)/ len(string)
prob_e = str.count(e)/ len(string)
prob_f = str.count(f)/ len(string)
prob_g = str.count(g)/ len(string)
prob_h = str.count(h)/ len(string)
prob_i = str.count(i)/ len(string)
prob_j = str.count(j)/ len(string)
prob_k = str.count(k)/ len(string)
prob_l = str.count(l)/ len(string)
prob_m = str.count(m)/ len(string)
prob_n = str.count(n)/ len(string)
prob_o = str.count(o)/ len(string)
prob_p = str.count(p)/ len(string)
prob_q = str.count(q)/ len(string)
prob_r = str.count(r)/ len(string)
prob_s = str.count(s)/ len(string)
prob_t = str.count(t)/ len(string)
prob_u = str.count(u)/ len(string)
prob_v = str.count(v)/ len(string)
prob_w = str.count(w)/ len(string)
prob_x = str.count(x)/ len(string)
prob_y = str.count(y)/ len(string)
prob_z = str.count(z)/ len(string)


    


    for i in range(0,26):
	ENG[i] = 0

    for i in range(0, 26):
	FRE[i] = 0

#open the input file and read all the input chatracters
for i in range (0,len(new_French)):
    counter = counter + 1
	if i == a:
        FRE[0] = FRE[0] + 1
	 
outFile = open("out1.txt", 'w')
outFile.write("ow")
outFile.close();
Print("Hello Cloudy")

from random import randint

vnw = "         |  |"
vnww = "         ]  ["
w = "---------   |"
cw = "------------|"
rw = "---------    -----"
cwr = "------------------"
nw = "          [] "

karta1 = [vnw, vnww, w, cw]
karta2 = [cw, w, vnww, vnw]
karta3 = [vnww, w, w, vnww]
karta4 = [vnw, vnww, rw, cwr]
karta5 = [cwr, rw, vnww, vnw]
karta6 = [nw, cwr, cwr, nw]
karta7 = [vnww, rw, rw, vnww]

maps = [karta1, karta2, karta3, karta4, karta5, karta6, karta7]

room = 0
kakkomna = 0
prob = 0

sila = 20
hp = 100
zashita = 20

print("Вы открываете глаза и осматриваетесь.")
print("Вы куда-то летите головой вниз. Впереди только белое месиво, возможно, это облака. ")
print("Через мнгновение вы столкнётесь с этим веществом!")
print("Однако, это действительно облака. Вы пролетаете через них и вам открывается вид на поверхность планеты.")
print("Красивый вид не поможет вашему положению. Вы падаете в лес.")
print("    ")
print("Придя в себя, вы оказываетесь в новом месте.")
print("Всё хорошо видно, несмотря на то, что нет источников света.")
print("Надо как-то выбираться.")

while room < 7 and hp > 0 :
   prob = randint(0,6)
   kakkomna = maps[prob]
   print(kakkomna[0])
   print(kakkomna[1])
   print(kakkomna[2])
   print(kakkomna[3])
   room = room + 1

   if prob == 0 :
        print("Итак. Вы зашли в корридор и у вас есть путь только налево.")
        print("Пойдёте ли вы налево?")
        print("1 - Да/2 - Нет")
        otvet = int(input())
        if otvet == 1 :
             print("Пошли...")
             sila += randint(2,7)
             hp += randint(3,10)
             zashita += randint(0,2)
        else :
            print("Ты ещё не готов к этому испытанию.")

   elif prob == 1 :
       print("На пути вам встречается поворот направо.")
       print("Вы можете подобрать манускрипт, увеличивающий вашу силу.")
       print("Нажмите 1, чтобы подобрать.")
       otvet = int(input())
       if otvet == 1 :
            print("Ура! Вы подобрали, в отличии от других предшественников.")
            sila += randint(3,10)
            hp += randint(7,30)
            zashita += randint(0,7)
       else :
            print("Ну не судьба. Пусть этот манускрипт встретит кого-то более достойного.")

   elif prob == 2 :
       print("Вы можете пойти налево или направо.")
       print("Куда же пойти?")
       print("1 - налево, 2 - направо.")
       otvet = int(input())
       if otvet == 1 :
            print("Да, именно туда.")
       elif otvet == 2 :
            print("Оттуда доносятся страшные крики, но это всего лишь казино.")
            print("Вы спокойно проходите мимо...")
            sila += randint(3,10)
            hp += randint(7,30)
            zashita += randint(0,7)

   elif prob == 3 :
       print("Таааак. Развилка. Я думаю пойти вперёд, но можно и налево...")
       print("Куда же пойти?")
       print("1 - налево, 2 - вперёд.")
       otvet = int(input())
       if otvet == 1 :
            print("Вы просто проходите налево...")
            continue
       else :
            print("Вы идёте по корридору и изучаете надписи на стенах")
            sila += randint(3,10)
            hp += randint(7,30)
            zashita += randint(0,7)

   elif prob == 4 :
       print("Развилки  - это круто!")
       print("Давай пойдём вперёд, нууууу или направо.")
       print("1 - вперёд, 2 - направо.")
       otvet = int(input())
       if otvet == 1 :
            print("Вас затоптала убегающая толпа.")
            hp -= randint(20, 30)
       else :
            print("Вы слышите топот мнежества людей, они куда-то бежали.")

   elif prob == 5 :
       print("Эх, можно идти только вперёд.")
       print("В окно влетает стопка книг!")
       print("Нажмите 1, чтобы подобрать.")
       otvet = int(input())
       if otvet == 1 :
            print("Ура! Вы подобрали, в отличии от других предшественников.")
            sila += randint(7,30)
            hp += randint(7,30)
            zashita += randint(3,7)
       else :
            print("Ну не судьба. Пусть этот манускрипт встретит кого-то более достойного.")

   elif prob == 6 :
       print("Опа! Развилка! Вы можете пойти налево, вперёд или направо.")
       print("Куда же пойти?")
       print("1 - налево, 2 - вперёд, 3 - направо.")
       otvet = int(input())
       if otvet == 1 :
            print("Неплохой выбор.")
            sila += randint(2,3)
            hp += randint(2,3)
            zashita += randint(1,2)
       elif otvet == 2 :
            print("Ну впереди ничего не видно, можно пойти.")
            sila += randint(3,10)
            hp += randint(7,30)
            zashita += randint(0,7)
       elif otvet == 3 :
            print("Самое время пойти направо!")
            sila += randint(-10,30)
            hp += randint(-10,40)
            zashita += randint(-10,30)

print("      ")
print("Вы слышете приближающиеся звуки ударов сверху.")
print("Вы делаете буквально 2 шага назад и перед вами с треском ломается потолок. Из пыли поднимается потрепаный, но всё ещё живой таратект.")
print("За пауком падает меч.")
print("      ")
print("Нужно победить Бешеного таратека, чтобы выжить.")
print("      ")
hpt = 735
silat = 40
zat = 10
shkrittt = 20

crit = 3
shkrit = 20
while hpt > 0 and hp > 0:
     print("      ")
     print("Ваш уровень здоровья: ", hp)
     print("Ваш уровень силы: ", sila)
     print("Ваш уровень защиты: ", zashita)
     print("      ")
     print("    O     ")
     print("   /|\    ")
     print("  / | \   ")
     print("   / \    ")
     print("  /   \   ")
     print("      ")

     print("Здоровье таратекта:", hpt)
     print("Сила таратекта:", silat)
     print("Защита таратекта:", zat)
     print("      ")
     print(" \   \.--./   /")
     print("  \ /  __  \ /")
     print("    |      | ")
     print("  /  \()()/ \  ")
     print(" /  / '--' \  \ ")
     print("      ")
     print("Выберете чем атаковать его!")
     print("      ")
     print("1 - удар мечом, 2 - удар рукой, 3 - удар ногой.")
     udar = int(input())
     
     
     print("Таратект двигается!")
     print("      ")
     print("Он пытается ударить!")
     ydacht = randint(1,100)
     if ydacht <= shkrittt :
          print("Критический удар!")
          bamttt = (randint((-10+silat)*crit,(15+silat)*crit) - zashita)
          if bamttt >= 0:
               hp -= bamttt
          else:
               bamttt = 0
               hp -= bamttt
               print("Враг не пробил!")
          print("Нанесенный ВАМ урон:", bamttt)
     else :
          bamttt = (randint((-10+silat),(15+silat)) - zashita)
          if bamttt >= 0:
               hp -= bamttt
          else:
               bamttt = 0
               hp -= bamttt
               print("Враг не пробил!")
          print("Нанесенный ВАМ урон:", bamttt)
     
     
     if udar == 1:
          print("Вы берёте меч и со всей своеё силой бьёте противника.")
          print("      ")
          print("   /\ ")
          print("  /  \ ")
          print(" |    |")
          print(" |    |")
          print(" |    |")
          print(" |    |")
          print(" |    |")
          print(" |____|")
          print("   ||")
          print("   ||")
          print("   []")
          print("      ")
          ydach = randint(1,90)
          if ydach <= shkrit :
               print("Критический удар!")
               bam = (randint((0+sila)*crit,(20+sila)*crit) - zat)
               if bam >= 0:
                    hpt -= bam
               else:
                    bam = 0
                    hpt -= bam
                    print("ВЫ не пробили!")
               print("Нанесенный урон:", bam)
          elif ydach >= shkrit:
               bam = (randint((0+sila),(20+sila)) - zat)
               if bam >= 0:
                    hpt -= bam
               else:
                    bam = 0
                    hpt -= bam
                    print("ВЫ не пробили!")
               print("Нанесенный урон:", bam)
     elif udar == 2 :
          print("Вы ударили противника кулаком!")
          print("      ")
          print(" ____ ")
          print("|    |")
          print("|____|")
          print("|    |")
          print("|____|")
          print("      ")
          ydach = randint(1,100)
          if ydach <= shkrit :
               print("Критический удар!")
               bam = (randint((-6+sila)*crit,(30+sila)*crit) - zat)
               if bam >= 0:
                    hpt -= bam
               else:
                    bam = 0
                    hpt -= bam
                    print("ВЫ не пробили!")
               hp -= 7
               print("Нанесенный урон:", bam)
          else :
               bam = (randint((-6+sila),(30+sila))- zat)
               if bam >= 0:
                    hpt -= bam
               else:
                    bam = 0
                    hpt -= bam
                    print("ВЫ не пробили!")
               hp -= 7
               print("Нанесенный урон:", bam)
     elif udar == 3 :
          print("Вы ударили противника ногой!")
          print("      ")
          print("  || ")
          print("  || ")
          print("  || ")
          print(" /  \___ ")
          print("/_______) ")
          print("      ")
          ydach = randint(1,100)
          if ydach <= shkrit :
               print("Критический удар!")
               bam = (randint((-30+sila)*(crit*2),(10+sila)*(crit*2)) - zat)
               if bam >= 0:
                    hpt -= bam
               else:
                    bam = 0
                    hpt -= bam
                    print("ВЫ не пробили!")
               hp -= 4
               print("Нанесенный урон:", bam)
          else :
               bam = (randint((-30+sila),(10+sila)) - zat)
               if bam >= 0:
                    hpt -= bam
               else:
                    bam = 0
                    hpt -= bam
                    print("ВЫ не пробили!")
               hp -= 4
               print("Нанесенный урон:", bam)


if hp <= 0:
     print("      ")
     print("Вы умерли.")
else:
     hp += 150
     sila =+ 25
     zashita += 20
     print("      ")
     print("Победа!")
     print("Вы можете идти дальше.")
     print("Ваши характеристики повышены.")
     print("Здоровье - ", hp)
     print("Сила - ", sila)
     print("Защита - ", zashita)
     print("Вы видите 2 пути: лестница наверх и лестница вниз.")
     print("Но перед тем, как пойти дальше вы решаете отдохнуть.")
     print("Вы засыпаете.")
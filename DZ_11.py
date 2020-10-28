import random
import time
import os



min_health = 0
max_health = 30
player_health = max_health
bot_health = max_health

# spell = [spell_name, damage, healing]
simple_spells = [['fireball', 10, 0], ['metabolism', 0, 8], ['silence', 0, 0], ['snowball', 7, 0]]
complicated_spells = [['strength', 9, 3], ['vitality', 4, 8]]

name = 0
damage = 1
heal = 2

# Img to ASCII
start_ascii = '''
                                ______ ________  ______  _______ ________
                               /      |        \/      \|       |        |
                              |  $$$$$$\$$$$$$$|  $$$$$$| $$$$$$$\$$$$$$$$
                              | $$___\$$ | $$  | $$__| $| $$__| $$ | $$
                               _\$$$$$$\ | $$  | $$$$$$$| $$$$$$$\ | $$
                               \$$    $$ | $$  | $$  | $| $$  | $$ | $$
                                \$$$$$$   \$$   \$$   \$$\$$   \$$  \$$
 __       __ ______ ________  ______  _______  _______         _______  __    __ ________ __      ____
|  \  _  |  |      |        \/      \|       \|       \       |       \|  \  |  |        |  \    /    |
| $$ / \ | $$\$$$$$$\$$$$$$$|  $$$$$$| $$$$$$$| $$$$$$$\      | $$$$$$$| $$  | $| $$$$$$$| $$   |  $$$$|
| $$/  $\| $$ | $$     /  $$| $$__| $| $$__| $| $$  | $$      | $$  | $| $$  | $| $$__   | $$    \$$| $$
| $$ $$\$$\$$ | $$   /  $$  | $$$$$$$| $$$$$$$| $$  | $$      | $$  | $| $$  | $| $$$$$  | $$     |  $$
| $$$    \$$|   $$ |  $$    | $$  | $| $$  | $| $$    $$      | $$    $$\$$    $| $$     | $$     |  $|
 \$$      \$$\$$$$$$\$$$$$$$$\$$   \$$\$$   \$$\$$$$$$$        \$$$$$$$  \$$$$$$ \$$$$$$$$\$$$$$$$$\$$
'''
gameover_ascii = '''
  ______   ______  __       __ ________         ______  __     __ ________ _______
 /      \ /      \|  \     /  |        \       /      \|  \   |  |        |       |
|  $$$$$$|  $$$$$$| $$\   /  $| $$$$$$$$      |  $$$$$$| $$   | $| $$$$$$$| $$$$$$$|
| $$|    | $$    $| $$$$\  $$$| $$  \         | $$  | $$\$$\ /  $| $$  \  | $$    $$
| $$ \$$$| $$$$$$$| $$\$$ $$ $| $$$$$         | $$  | $$ \$$\  $$| $$$$$  | $$$$$$$|
| $$__| $| $$  | $| $$ \$$$| $| $$_____       | $$__/ $$  \$$ $$ | $$_____| $$  | $$
  \$$$$$$ \$$   \$$\$$      \$$\$$$$$$$$        \$$$$$$     \$    \$$$$$$$$\$$   \$$
'''
end_ascii = '''
 ________ __    __ ________        ________ __    __ _______
|        |  \  |  |        \      |        |  \  |  |       |
 \$$$$$$$| $$  | $| $$$$$$$$      | $$$$$$$| $$\ | $| $$$$$$$|
   | $$  | $$    $| $$  \         | $$  \  | $$$$\ $| $$  | $$
   | $$  | $$$$$$$| $$$$$         | $$$$$  | $$\$$ $| $$  | $$
   | $$  | $$  | $| $$_____       | $$_____| $$ \$$$| $$__/ $$
    \$$   \$$   \$$\$$$$$$$$       \$$$$$$$$\$$   \$$\$$$$$$$
'''
level_up_ascii = '''
 __       ________ __     __ ________ __              __    __ _______
|  \     |        |  \   |  |        |  \            |  \  |  |       \|
| $$     | $$$$$$$| $$   | $| $$$$$$$| $$            | $$  | $| $$$$$$$|
| $$     | $$  \   \$$\ /  $| $$  \  | $$            | $$  | $| $$    $$
| $$     | $$$$$    \$$\  $$| $$$$$  | $$            | $$  | $| $$$$$$$
| $$_____| $$_____   \$$ $$ | $$_____| $$_____       | $$__/ $| $$
 \$$$$$$$$\$$$$$$$$    \$    \$$$$$$$$\$$$$$$$$        \$$$$$$ \$$
'''
new_round_ascii = '''
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||..||||||||||||||||||||||||||||||
|||||||^-||||||||||||||||||||.&!&-.|..||||||||||...-!^^^.|||||
|-||!%@@@$!||||||||||...||||.^^&&&!&!.|||||||.$##@$$@@@$!!-.!.
|&$@$&!--&!||||||||||-&!&--^-!%%^&^-..!!.|||||.&%%&%!%$%!.-@@&
||%@^--!..&|.-^&^^^^^%%%%%&&%%%%^^&^&&^&&--&%^^&&!&!!&@$@##%.|
||||.!$@$@@@$$@$!.||.-&%!-.!^&%^&--!&&&&!.|-&&@$$$$@@@#####^||
|||!#@%!@##$^$$#!|||||-&-.&--!%^&!-...!...||||||-%@@@@#^.!&.||
|||^##@!#@#@^||..||||||||..|.!&-!.|||||||.!^^&||||^$##@&||||||
||^#%.|%#@@@$$.|||||||||||||||.||||||||||&&-.$!|!$$@#$@@.|||||
|^^%^|&##$@@@$@.|||||||||||||||||||||||||!$-...$$$@##@@#&|||||
|^^!!$##@%!..$$!&||||||||||||||||||||||||||-&%^$^!%&.$@@$.||||
||||||-.||||||||||||||||||||||||||||||||||||||||||||||||||||||
'''
win_ascii = '''
##########################################
################_||||#||||_###############
###########|||||||||||||||||||||##########
##########$|||||||||||||||||||||$#########
######|||||||||||||||||||||||||||||||#####
######|||||||||__-$$$$$$$$$$|||||||||#####
##$||||||||$|||$$$$$$$$$$$$$|||$||||||||##
###|||||||||$|||$$$$$$$$$$$@||$|||||||||##
####|||||||||$$||$$$$$$$$$|||$|||||||||###
#$||||||||||||||$$$$$$$$$$$@|||||||||||||#
#||||||||||||||||||$$$$$|||||||||||||||||@
###|||||||||||||||||$$$$|||||||||||||||@##
##|||||||||||||||||$$$$$||||||||||||||||$#
#||||||||||||||||||$$$$$$||||||||||||||||@
####-||||||||||||$$$$$$$$$||||||||||||-###
####|||||||||||||$$$$$$$$$||||||||||||-###
####|||||||||||||$$$$$$$$$|||||||||||||###
########||||||||@@||@@@@@@@||||||||#######
########||||||||||||||||||||||||||$#######
#############||||||||||||||||$############
##############||###$|||###$||#############
'''

racoon=  '''
     ``     `+
    .hs---:+od`
  `-+so/:/+shd:
 :myy+/-.-oydds
 .ys/:++:/sddmd`
 `yy/+yhyhhddmm/
 /mssydNNdddddNy
 ydhhddNmmNNhdmm`
.dmdNNNhmmmNddddhy
.hddmmNmdmNNdhddh+
./smmNNmmNNNNhhmh-                            `
  .mNNNNNNNNmyhmhyo   `-:-.``     ```   ``.-//.
  .mmmmNNNdhdydmysy.  .syssoso/:-:::::/:osydms.
  .mNddmNNddhyddyso-   sdmdsohdyoooooosssydmmo.
  -NMNNNNNNNdhddss.    `sdmdsyhyssoooosssosyho`
  ohhhhhyyysyhdhoo/`   `oyys+ossoooossyysoosss:`
  +oohddhhyyyhmyssd:   /sso++++//:/oo+oyyo:/o+/-.`
   `ymohNmmmmhNsosmo  `o++/-.....--:s-.oo+..o///+-`
    dh--NNdmmdmsosmh`///:/oo//+shddhd::so+++hmmmmy/`
    hh+ ymmdNmds+smms++osyhmmmmmmmmmmhss++sydmmmmdy:
    ohs -mmmmNhsoyNdysyddmmmmmmmmddhs/-..:/:-sdmhs/.
    -my. dmmmNdsssNdmmdmmmmmmmmmdhy+:-.:sdyso:++:.
     hy/ +mmmNNyssdmdNhdmmmmmmmdhhyyo+/smNmmdo/.
     sys`-NmmmNhyyhmdNdhdmdmNNNmmmmmmdhyhhhhdy/:-`       .
     +do+oddmmNmydymdNdddmmmNNNNNNNNNmmddddddhyyyos`    -.
     -NsyyydmmNNddhdmNddmNNNNmmmmmmmmmmmmmmmmmmho//::/-:`
     `sosshdhmmNNmmdmNmmNmNNNmdddhhhddmmmmmNNNNmmdhyhyo.
       -yyyhydmmmNNmmNNNNmNNNNdhyyyhyddmmNNNNNmmNmmdo++:.
     -yNMdhhhddmmNNmmNNmdmmNmNNmhhhdmmmmmmmNNNNNNNmy+/+++.
     dNmmmmmddhhmmNmmdhshmmddhddhdddhhhhhhdmNNNNNmyso++++/.
     smmmmmmddddddmmNmdsydmdyhyyyyyyyyyyyyyhdmNNmdyyssoooo/:
     -NNNmdmmmddddmmmNmhydmdyhhyyhhyyyyyyhhhhdNNmdddhyssoo+o+.
      dNy-hmddmmddmmmNmdymmhhhhmmhhhhhhhhhhhdmNNNmmmdhyosoooo+-.`
      -:`-NdhhNdNNNmmNNmmNmdyhshhshhhhhhhhddmNNNNNNmmddyhssssooo:.
         `mdhhddNNNNmNmmmmmdyssyhssyyyyyhhdNNNNNNmNmsshmmhyhysooo+-
         `dmhhddNNNNmmdhmdNmhssyhsssdhhddmmNmNNNmmNd/ `/hmdmhyo+oo+.
         .dmdddhdmNNNmmdmmNmdysyyysyhmmmmddddNNmmNmy.   `/ohddsoooo/`
         .hddmmdhdmh+dNNNNNmhysyyyyyhdhhyyyhdNNmmmds`      .hdhyoooo:`
          +hdmdyos/` .mNNNNNmhysyysyydhhddmmNNNNNmdy.       -:hdhsoso-
         `ohhhhms/    oNmNNNNNhyyyyyyhmmmmmdddmNNmdy-         .oshyss/.
         `yyshhmh/    +NNNNNNmhyyyyyhhmdhhyyhhhmNmmds-           :hyss/`
         `syyhmdm/    sNmNNmNNdhyyyyyhhdhddddmmNNNmmho:.          :dyyo:           ````` ``
         `oddhddmo   -mNNNNmNNNdhyyyyyhmmmmmmNNmmmNNmdyoo-        .yyso/`    `````.-://:-:///-`
          sddhdyhd+.:dNmmddmNmmmdddhhhhmmmmmNmmmhhmNNdo/+-       `ossoo+-```..:///++yhhhsoooshy+.
          :ddhhsymhdmmdhyhmNmhyyyhhddddddhhhdmmmmmdmNNmdyo-      -yyyoo++.`-/syyyyysshddddhyyyhdh-
          `ydddddNdhhhhdmmmhhhyhhhhhhhhhhhhhhhdmNNmNmNNNmdo-`    `/hhyyyy/:/+syyhddhhhhdmmdhhhhddds`
            -mNNNmmdmmmmdhyyhhhhhhhhhhhhhhddddhhhddNmmNNNNds:`     -+osyhsyyyssyydmmddhyhdmdyo--...
             sNmdmmmmmdhhhhhhhhhhhhhhhyyhhhhhhhhhhhhmNNNNNNmy/.  .:/+oshdmmdhhyyydmmmmhhyss:
             .yhhdhyyhhhhhdhhhhddmmNmmmmmmmmmmmdhhhhhdmNmNNmmyo-ohdhyysyhdmmmdhyyhdmmmdy:`
                `:syhhhdddhddmNNNNNmNmmdddmmmNNNNdhhhhhdmNNNmds/smmmdhhhhdmmNmdhyhhhdh:`
                :hdhdddddhdNNNmmdhys++/::oyhhhdddmNdhhhhhhdNmmmy/smmmdhhhhdmmmdhyso:.`
                ydmNNNmmmdmNdyo:-`       `+ydmmmdhhdmdhhhhhhmmmmdosmmmdhyyhdmmmy/-
                ymNNNMMMMNm-`              `:osyhhddhdmddddhhNNmNdsyNmmdyyyo//:`
                -dmNNNNNNmy`                 ```::+yhyhddddmmmmmmNmddhs/:.`
                 -ddmmmmmmd+                          `/hmNNNNNNmmNmso:
                  :yhdmmmmmh/                           `+dNNNNNNNmdhdy/.
                    .:sydmmmh+                            ./ydmmmmdmddhhs/`
                       .hmmmdh.                               `-/oosyhdddy+`
                      `ommmmms-                                   ``/odmmms.
                    `:ydmmmh/                                         oddds.
                   -shddmdo`                                          :yhhs-
                 `-shhdmd:                                            :hyso/.
           .-:/++osdydmd.                                             sdyss+:
        `:sdddhhhhhhdds-                                             .yhyyyso.
         `:`-+.`+::-`                                               .+dhhhhyy/
                                                                   ohmyddhhy+y.
                                                                   +:yy/yy+o ``
                                                                     .  -`
'''

# ------------- Start -------------
while True:
    # Player select
    print(start_ascii, '\n[Y] - Yes\n[N] - No\n')
    select = input('Start Wizard Duel? Your select: ')
    if select == 'N' or select == 'n':
        break
    elif (not select == 'Y') and (not select == 'y'):
        print('Error! Try again.')

    else:
        # --- create new list with spells ---
        os.system('cls')
        spells = simple_spells
        a = len(simple_spells)
        del spells[a:]
        print('''
==========================================
================ OPTIONS =================
         Spell           Damage  Healing''')
        count = 1
        for row in spells:
            print(f'\n{[count]}', end=' - ')
            count+=1
            for elem in row:
                print('\t', elem, end='')

        print('''
==========================================
       ------- WIZARD DUEL -------''')
        print(new_round_ascii)
        # Start new game
        for round in range(1, 6):
            # User select
            choice = True
            while choice:
                player_select = input('\nSelect spell ([i] - List of spells): ')
                if (player_select == 'i') or (player_select == 'I'):
                    print('''
==========================================
================ OPTIONS =================
         Spell           Damage  Healing''')
                    count = 1
                    for row in spells:
                        print(f'\n{[count]}', end=' - ')
                        count+=1
                        for elem in row:
                            print('\t', elem, end='')
                elif player_select > '0' and player_select <= str(len(spells)) and len(player_select)==1:
                    player_select = int(player_select)
                    player_select = player_select - 1
                    bot_select = random.randint(0, len(spells)-1)
                    choice = False
                else:
                    print('Error! Try again.')

            play_1 = spells[player_select][name]    # The spell selected by the player
            play_2 = spells[bot_select][name]    # The spell selected by the bot
            print(f'''
            ----ROUND № {round}----
    {play_1.upper()}    -----    {play_2.upper()}''')

            # Use spell
            if play_1 == 'silence' and play_2 == 'silence':
                continue
            elif play_1 == 'silence':
                player_select = bot_select
                player_health += spells[bot_select][damage]
            elif play_2 == 'silence':
                bot_select = player_select
                bot_health += spells[player_select][damage]

            player_health += spells[player_select][heal]
            player_health -= spells[bot_select][damage]
            bot_health += spells[bot_select][heal]
            bot_health -= spells[player_select][damage]

            # Max & min health
            if player_health > max_health and bot_health > max_health:
                player_health = max_health
                bot_health = max_health
            elif player_health > max_health:
                player_health = max_health
            elif bot_health > max_health:
                bot_health = max_health
            print(f'''
      PLAYER      vs      BOT
        {player_health}                {bot_health}
    ''')
            if player_health < min_health or bot_health < min_health:
                break

            # ----------- complicated spells ---------------
            # ------------ Level Up -----------------
            if round == 3:
                os.system('cls')
                print(f'''
                {level_up_ascii}
==========================================
============== NEW FEATUES ===============
        Spell           Damage  Healing''')
                spells += complicated_spells
                count = 1
                for row in spells:
                    print(f'\n{[count]}', end=' - ')
                    count+=1
                    for elem in row:
                        print('\t', elem, end='')
                print('\n==========================================')

        # ------------- The end -------------
        os.system('cls')
        print(gameover_ascii)
        if player_health > bot_health:
            print('Congratulations! You win!\n', win_ascii)
        elif player_health < bot_health:
            print('Sorry... The computer wins!')
        else:
            print('Draw!')

        print (racoon)
        time.sleep(5)
os.system('cls')
print(end_ascii)

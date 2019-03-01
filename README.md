# imprint

Convert images and videos to ASCII.  
![text totoro](/img/totoro_out.gif)

## Installation

```
$ git clone https://github.com/jacoblurye/imprint.git
$ cd imprint
$ pip install .
```

## Usage

### Command-Line Interface

Installing imprint gives you the `imprint` command, which takes a path to a media file and some configuration options.

```
$ imprint --max_width=100 img/flower.jpg
                                           :+*:
                                          :+++***
                                  :***    *+++:***                 :·
                                 :*+++*+ :*+++++**+            :****++
                                 ++++++++**++:+:***+      *++***++++**
                                 +++++++*+*::+::+***·  +**+*++*+++++**:
                   ***++:        :++:++++*++:*:+:**++:@*+*+++:*++++++**
                   *+++*+***     ·++:++:++*++*:+·+*+**+++++:++*:++:*++:
                   :++:++*+***+·  +++:++::++++::*:***+++*+:+:+:++:*+++·
                   ·+++:+++*+***+:++++:+:::+++::+:+*+++++++::+::*+++++
                    :++++:+++*+*++++:+:::::::+::++**:*+++:::+::*++:+:+   ·++*****@*+
          ·****+:·   :+:++:++++++++++:::::::::::::++++++:+:++:**+:*::::+:+++***+**+
           ·++++++::··:++:++:+++++:::::·::::::::::+:*+::+::+:+*+:+:::+::+****+**++:::+·
              :++:+:::··:::+:+:++++::::········:···:++::+:+::++:+:::::****++*++*:+++++*****
         ·:+*********++::::::++::+++::::·· ··:·: ·:·+::::+:·:+:++:::*****@***++*++++*******+
        +++++++++++****+++++++:++:::::··:·······:··:··: ·:··::+++++***@***+****+:+++*+++++:
         +:::::::+*+**+++***+:++:++·:·::+·: :::·+ · ::···:: ::+::+******+***++:+++:::::+:
          :+::::::::::+++**+++++:::::··:·:·:··· ····  ··· ··: :::****+****+++*+++::++:
            +++***********++++*+:·:··· ··:··· · ····· ·· ·· ····++++*****+**++++::++:::·
         ++++++++++***********+::+ ·:······· : ···:··  :·  :· ··::+***++*++++*+:::+++++****:
        ++++++++++++++++*++++++*:··· ·· ·······:·::·::::··+·· :·+·:+++**++**+··::::+:+++*****:
         ·::++::++++++*********+: ·:·:·   ···:::++++:+++::··:·+ ·::·+++**+:··::::+++++**+:+++
           ···:::++***++***++++++::··: ::···:·:++++++++:··::··:·+:···::::+:+++++++::::+:::+
        ·::::::::··::::++++****+··  ·::  :· ·::+++:+++++::···::: ·····*++++++++++++++*::
        ::······:::::::+++++++:···:·  ·······:::::·:::+::·:+:  ·· · ··******@@@*@*::::++:
        ·:::::::::*@@@@@@******:·::···· ··+····:::::::···++::· · · ··:·::::·········::::::+*·
            ·+**@@@@@******@****:···· ·· ····:··:········:·:  :······:*******@*+:·:::::+++:::::
           :*********@@@*******+· · :: · ·:+···:···:: ++··:::·:·· ··:*********@@@@+::++++*++*+:
         :***+******************+·::·: ··  :·::·+:++:+·· ·: ·   ·: ·+************@@@+···::::
       ·++++++++*+++***********+::····:·:···· :···::········: ·:·::+****************@@·
      ·++++:::+**++++********:+*+*++::::·: :···· ·: :·   · ··· ·:+************++*****+*·
       ··::::+++++***+++:·:++********+:··: ·····: ·:······: ·:****************+++++:++*+
          ::·········:::+++*@@@*********:·······:···· ·:··+:+********+****++++:++:++:··
         :···········::::*@@@@*@@@@**@**+++::·· · +:++:**+********@@@@++******++·+··:
           ···::::++::::**@***@@@@*@@@*++*@+****@@@*****@@*******@*@@@@*:+**+***+:::·:
                      ·*******@@*@@@**+*******+@@@@**@@@@@@***+******@@@*::++++**+::::
                      ***+***@*@****@++****@**+@@@@@@@@@@@@:****++*****@*:·+++:+:+++·:
                     **++**********+++***+*****@@@*@@@@@@@@·+****+++++****:·::+:+:::+·
                    ·++**+**++***::+++*+:******@*@*@@@*@@@@:··:****++:++++      · ·::
                    :+++++++**:·:++++*··+***++*@*@*@@@*@@@*+:· :::++*+++:::
                    ·:···:::::::::++:  :+++++++@*******@@@:::::·:::
                          :::::::+:    :++++++++******+**+::::+::::·
                          ·::·:::       +++++++++**+*****:+:·::+:++:
                           ··:·         ·+++++++·:+*++++ ·+::·:+:++:
                                         ·++:++· ··:++·    ++:·:+++
                                          :::: · ··:        ·++:+:+
                                            ·   ···           ·+::
```

### API

Create an instance of the `ASCIIMedia` class to access the same functionality as above (this is what the CLI uses internally).

```python
>>> from imprint import ASCIIMedia
>>> custom_symbols = 'X:. '  # You can substitute your own set of characters
>>> flower = ASCIIMedia('img/flower.jpg', custom_symbols)
>>> flower.print(max_width=75)
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX:..XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.....XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXX.. XX.......XXXXXXXXXXX:.:XXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXX.....:....:. :XXXXXXX:.....:XXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXX.......:.:....XXX..........:XXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXX.:XXXXXXXXX....:...::....:X ...........XXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXX....  :XXXX..:..:.....: .. :..:....... XXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXX:.:...  .XX:....:....:... :....::......XXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXX..:.......X..:..:...:.: ....::.:. ....XXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXX:...........:::::::.:........:.: ...::XX:....  .XXXXXXXXXXXX
XXXXXXXX ....:XX:...:...:...:::::::::.....::......::..:.......XXXXXXXXXXXXX
XXXXXXXXX:.:..::X:..::....::.::::::::::..:.:.:..:::::..........  .XXXXXXXXX
XXXXXXXXXXXX.::.:::.:..:...:::X:::::X...:::.::.:.:::.  .     .....  .XXXXXX
XXXXXX...............::.:::::X:::X:::X:X:XX::::.:..     ... .:......XXXXXXX
XXXXXX.::::....... .....:.::::X:X:::.:X::XX:.:....    .  ..:..::::.XXXXXXXX
XXXXXXX:.::::.::. .......:::X::::XXXX:XXX:XXX:::. ...  ..:...::.:XXXXXXXXXX
XXXXXXXXX:....    ......::X:X::::XXXX:X:XXXXX::::..  .......::..:XXXXXXXXXX
XXXXXXX.:...............:.XXX:X::X::XX:XX::X:X:X::.........::........XXXXXX
XXXXXX.:....:.........:.:XXX:XX:XXX:::.::::X.:X::X.. ... ::::::::.... :XXXX
XXXXXXX::...:...........XXXXXXX:::::....:X::XX::XX:...:::::......:::.:XXXXX
XXXXXXX::::X::::.......::X::::::::.......::::::X::X:...........::..XXXXXXXX
XXXXXX.:::::XX::::......::X:XX:XX::..::::::X::.XX:XX:.......   .:XXXXXXXXXX
XXXXXX.:::::::.       ..XXX:XXX::X:.::::.:::::XXXXX:::...:XX:::::::.XXXXXXX
XXXXXXXXX...          ..:::XX::X:X:X:::X:X:::XXXX::::      ::::::::::..XXXX
XXXXXXXXX    .       ...XXX.X:X:::X:XX:::.::::X::X::.....     .....::.:XXXX
XXXXXXX....     .  .    ::::X::X::.:.:::::XXXXXX:X:. ...   .   .::..:XXXXXX
XXXXX:..........  ..   ..::X:XX:X::X::.XXXX:XXX:X:    ...   . .  XXXXXXXXXX
XXXXX.:::.........  .:.... ::::XXXXXXX::::X:::X:..  .  ...... ....XXXXXXXXX
XXXXXXXX:......:X::..      ..:X:X:XX:::::X::X:.   ... ... ........XXXXXXXXX
XXXXXXX:::XXX::::::.          ::XXXX::XXX.:....     . .....X.::XXXXXXXXXXXX
XXXXXXXX:::::...::.          .. ...          ... .   ........:X:XXXXXXXXXXX
XXXXXXXXXXXXXXXXX.  .        .  .           . ....    .:......:::XXXXXXXXXX
XXXXXXXXXXXXXXXX:....       .  .  .         . .....    :....:..::XXXXXXXXXX
XXXXXXXXXXXXXXXX...  .    ... .  .:         :. ....... .:::.:::.XXXXXXXXXXX
XXXXXXXXXXXXXXX:....... .:....:...:         ::X.  ..::..XXXXXX::XXXXXXXXXXX
XXXXXXXXXXXXXXX:......:::...::....:         :::X::::...:XXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXX.::::..XX:.....        .:::X:::XXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXX..::.XXXXX.....:  .....::::..::XXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXX::::XXXXXX:.....X.....X.:::.:..XXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX..:.:XX...XXX.::.:.:XXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX:::XXX:XXXXXX:::..XXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX:XX:XXXXXXXXXX.::XXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

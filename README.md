# imprint

Convert images and videos to string representations.    
![text flower](/img/flower_out.png)

## Installation
```
$ git clone https://github.com/jacoblurye/imprint.git
$ cd imprint
$ pip install .
```

## Usage
### As A CLI
```
Usage: imprint [options] file
```
Point the `imprint` command at any image or video file. For example:
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
### As A Module
 The module implements the following classes:
* `ImgPrinter`: for stringifying and displaying image files (excluding gifs).
* `VidPrinter`: for stringifying and displaying video files (and gifs).

These classes support flexible use in other Python scripts. For example:
```
>>> from imprint import ImgPrinter
>>> symbols = u' \u25A0'
>>> imprinter = ImgPrinter(symbols)
>>> str_repr = imprinter.str_to_img('img/flower.jpg')  # get the string representation without printing
>>> imprinter('img/flower.jpg', max_width=75)          # print the string representation directly

                                ■■■
                           ■    ■  ■■
                         ■■■■■ ■■■■■■■          ■■■■
                         ■■■■■■■ ■  ■■■    ■■■■■■■■■
                         ■■■■ ■■■  ■■■■  ■■■■■■■■■■■■
              ■■■■■■■    ■■ ■■ ■■■■  ■■■■ ■■ ■■ ■■■■■
               ■■■■■■■■■  ■■ ■  ■■  ■■■■■■■■■  ■ ■■■■
               ■■■ ■■■■■■■■■■    ■■ ■■■ ■■■■ ■  ■■■ ■    ■■■■■
        ■■■■    ■  ■■■■■■■■■         ■■■■    ■ ■■■   ■ ■■■■■■■
          ■ ■■    ■   ■■■   ■          ■■ ■ ■ ■■     ■■■■■■■■■■■■
            ■■■■   ■  ■ ■■■            ■   ■  ■ ■  ■■■■■■■■■■■■■■■■■■
      ■■■■■■■■■■■■■■■■ ■■                      ■■■■■■■■■■■■■ ■■■■■■■
       ■      ■■■■■■■■■■■                       ■■■■■■■■■■ ■■   ■■
         ■   ■ ■■■■■■■■■■                      ■ ■■■■■■■■■■■  ■
       ■■■■■■■■■■■■■■■■■■                         ■■■■■■■■■  ■■■■■■■■
      ■ ■■■■■■■■■■■■■■■■              ■            ■■■■■■        ■■■■■
           ■■■■■■■■■■■■■       ■   ■■■■■■      ■  ■■■■    ■■■■■    ■
                 ■■■■■■■          ■■■■■■■■           ■■■■■■■■■■■■
      ■        ■■■■■■■■                              ■■■■■■■■■
         ■■■■■■■■■■■■■■■                             ■■■■■■          ■■
         ■■■■■■■■■■■■■■■   ■    ■  ■   ■ ■         ■■■■■■■■■■■  ■■■■■■■
       ■■■■■■■■■■■■■■■■■■ ■        ■ ■■■           ■■■■■■■■■■■■■■■■
     ■■■ ■■■■■■■■■■■■■■■■                        ■■■■■■■■■■■■■■■■
          ■■■■■■■■  ■■■■■■■■                  ■■■■■■■■■■■■■■■■ ■■■
                    ■■■■■■■■■■             ■■■■■■■■■■■■■■■  ■
              ■■  ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
                 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ■■■■■
                ■■■■■■■■■■■ ■■■■■■■■■■■■■■■■ ■■■■■■■■■■  ■■ ■ ■
                ■■■■■■■■■ ■■■■ ■■■ ■■■■■■■■■   ■■■■■■■■    ■■■
               ■■■■■■■■  ■■■■ ■■■■ ■■■■■■■■■      ■■■■■■
                    ■    ■    ■■■■■■■■■■■■■■
                              ■■■■■ ■■■■■■■    ■■■
                               ■■ ■■  ■■■■  ■  ■ ■■
                                ■            ■  ■■
                                               ■
```
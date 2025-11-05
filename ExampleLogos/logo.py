# noinspection PyUnresolvedReferences
from stv_utils import process

highlight = "\x1b[1m"

redhat = (
    "               .MMM..:MMMMMMM           \n" +
    "          MMMMMMMMMMMMMMMMMM            \n" +
    "          MMMMMMMMMMMMMMMMMMMM.         \n" +
    "         MMMMMMMMMMMMMMMMMMMMMM         \n" +
    "        ,MMMMMMMMMMMMMMMMMMMMMM:        \n" +
    "        MMMMMMMMMMMMMMMMMMMMMMMM        \n" +
    "  .MMMM'  MMMMMMMMMMMMMMMMMMMMMM        \n" +
    " MMMMMM    `MMMMMMMMMMMMMMMMMMMM.       \n" +
    "MMMMMMMM      MMMMMMMMMMMMMMMMMM .      \n" +
    "MMMMMMMMM.       `MMMMMMMMMMMMM' MM.    \n" +
    "MMMMMMMMMMM.                     MMMM   \n" +
    "`MMMMMMMMMMMMM.                 ,MMMMM. \n" +
    " `MMMMMMMMMMMMMMMMM.          ,MMMMMMMM.\n" +
    "    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n" +
    "      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM:\n" +
    "         MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM \n" +
    "            `MMMMMMMMMMMMMMMMMMMMMMMM:  \n" +
    "                ``MMMMMMMMMMMMMMMMM'    \n"
)

ubuntu = (
    "                             ./+o+- \n" +
    "                  yyyyy- -yyyyyy++  \n" +
    "               ://+//////-yyyyyyo   \n" +
    "           .++ .:/++++++/-.+sss/`   \n" +
    "         .:++o:  /++++++++/:--:/-   \n" +
    "        o:+o+:++.`..```.-/oo+++++/  \n" +
    "       .:+o:+o/.          `+sssoo+/ \n" +
    "  .++/+:+oo+o:`             /sssooo.\n" +
    " /+++//+:`oo+o               /::--:.\n" +
    " \\+/+o+++`o++o               ++////.\n" +
    "  .++.o+++oo+:`             /dddhhh.\n" +
    "       .+.o+oo:.          `oddhhhh+ \n" +
    "        \\+.++o+o``-````.:ohdhhhhh+  \n" +
    "         `:o+++ `ohhhhhhhhyo++os:   \n" +
    "           .o:`.syhhhhhhh/.oo++o`   \n" +
    "               /osyyyyyyo++ooo+++/  \n" +
    "                   ````` +oo+++o\\:  \n" +
    "                          `oo++.    \n"
)

windows = (
    ';D2042D;        ,.=:!!t3Z3z.,               \n'
    ';D2042D;       :tt:::tt333EE3               \n'
    ';D2042D;       Et:::ztt33EEEL ;00A36C;@Ee.,      ..,\n'
    ';D2042D;      :tt:::tt333EE7 ;00A36C;;EEEEEEttttt33#\n'
    ';D2042D;     :Et:::zt333EEQ. ;00A36C;$EEEEEttttt33QL\n'
    ';D2042D;     it::::tt333EEF ;00A36C;@EEEEEEttttt33F \n'
    ';D2042D;    :3=*^```"*4EEV ;00A36C;:EEEEEEttttt33@. \n'
    ';0096FF;    ,.=::::!t=., ` ;00A36C;@EEEEEEtttz33QF  \n'
    ';0096FF;   :::::::::zt33)   ;00A36C;"4EEEtttji3P*   \n'
    ';0096FF;  :t::::::::tt33.;FFBF00;:Z3z..  `` ,..g.   \n'
    ';0096FF;  i::::::::zt33F ;FFBF00;AEEEtttt::::ztF    \n'
    ';0096FF; ::::::::::t33V ;FFBF00;:EEEttttt::::t3     \n'
    ';0096FF; E::::::::zt33L ;FFBF00;@EEEtttt::::z3F     \n'
    ';0096FF;{3=*^```"*4E3) ;FFBF00;:EEEtttt:::::tZ`     \n'
    ';0096FF;             ` ;FFBF00;:EEEEtttt::::z7      \n'
    ';FFBF00;                 "VEzjt:::z>*`      \n'
)

centos = (
    "               /AAAA\\                 \n"
    "              /MKKKKM\\             \n"
    "             /AAAAAAAA\\          \n"
    "     KKSSV' /KK| LJ |KK\\ 'VSSKK     \n"
    "     KKV'  /KKK| LJ |KKK\\  'VKK     \n"
    "     V' '  \\KKK| LJ |KKK/  ' 'V     \n"
    "     .4MA.' \\VK| LJ |KV/ '.4AA.     \n"
    "   . KKKKKA. \\V| LJ |V/ '.4KKKKK .   \n"
    " .4D KKKKKKKA.\\| LJ |/.4KKKKKKK FA. \n"
    "<QDD ++++++++++++  ++++++++++++ GFD>\n"
    " 'VD KKKKKKKK'/| LJ |\\'KKKKKKKK FV  \n"
    "   ' VKKKKK'./4| LJ |4\\.'KKKKKV '   \n"
    "      'VK'. /KK| LJ |KA\\ .'KV'      \n"
    "     A. . ./KKK| LJ |KKA\\  . .4     \n"
    "     KKA. '\\KKK| LJ |KKK/  .4KK     \n"
    "     KKSSA. \\KK| LJ |KK/ .4SSKK     \n"
    "             \\<><><><>/              \n"
    "              \\MKKKKM/               \n"
    "               \\VVVV/                \n"
)
# print(centos)

debian = (
    "           _,met$$$$$gg.   \n"
    "    ,g$$$$$$$$$$$$$$$P.    \n"
    '  ,g$$P"     """Y$$.".     \n'
    " ,$$P'              `$$$.  \n"
    "',$$P       ,ggs.     `$$b:\n"
    "`d$$'     ,$P\"'   .    $$$\n"
    " $$P      d$'     ,    $$P \n"
    " $$:      $$.   -    ,d$$' \n"
    " $$;      Y$b._   _,d$P    \n"
    ' Y$$.    `.`"Y$$$$P"\'     \n'
    ' `$$b      "-.__           \n'
    '  `Y$$                     \n'
    '   `Y$$.                   \n'
    '     `$$b.                 \n'
    '       `Y$$b.              \n'
    '          `"Y$b._          \n'
    '              `"""         \n'
)

arch = (
    "                   /\\                 \n" +
    "                  /oo\\                \n" +
    "                 /oooo\\                \n" +
    "                /oooooo\\               \n" +
    "               /oooooooo\\              \n" +
    "              /oooooooooo\\             \n" +
    "             /oooooooooooo\\            \n" +
    "            /oooooooooooooo\\           \n" +
    "           /oooooooooooooooo\\          \n" +
    "          /oooooooooooooooooo\\        \n" +
    "         /oossssssoooossssssoo\\       \n" +
    "        /osssssso/''''\\osssssso\\      \n" +
    "       /osssssso:      :ssssssso\\     \n" +
    "      /ossssssso        ossssoooo\\    \n" +
    "     /ossssssss+        +ssssooooo\\    \n" +
    "    /ossssso+/:-        -:\\+ossssoo\\  \n" +
    "   /+sso+:-`                `.ooooso\\ \n" +
    "  /++-`                          `-++\\ \n" +
    "  \\`                                `/  \n"
)

android = (
    "             █    █            \n" +
    "          ████████████          \n" +
    "        M███████████████M        \n" +
    "       ████ █████████ ████      \n" +
    "      ████████████████████      \n" +
    " /██\\ ████████████████████ /██\\ \n" +
    " ████ ████████████████████ ████  \n" +
    " ████ ████████████████████ ████ \n" +
    " ████ ████████████████████ ████ \n" +
    " ████ ████████████████████ ████ \n" +
    " ████ ████████████████████ ████ \n" +
    " ████ ████████████████████ ████ \n" +
    " \██/ ████████████████████ \\██/ \n" +
    "      ████████████████████      \n" +
    "          ████    ████          \n" +
    "          ████    ████          \n" +
    "          ████    ████          \n" +
    "          ████    ████          \n"
)

logo = {
    "redhat": "\n".join(process(";FA8072;" + highlight + x) for x in redhat.split("\n")),
    "ubuntu": "\n".join(process(";F88379;" + highlight + x) for x in ubuntu.split("\n")),
    "windows": "\n".join(process(highlight + x) for x in windows.split("\n")),
    "debian": "\n".join(process(";E0002C;" + highlight + x) for x in debian.split("\n")),
    "centos": "\n".join(process(";BB409B;" + highlight + x) for x in centos.split("\n")),
    "arch": "\n".join(process(";00A4FF;" + highlight + x) for x in arch.split("\n")),
    "android": "\n".join(process(";007F2E;" + highlight + x) for x in android.split("\n")),
}


## Export
#
# import json
#
# with open("test.json", "w", encoding="utf-8") as f:
#     json.dump(logo, f, ensure_ascii = False, indent = 4)

## Preview
#
# with open("test.json", "r", encoding="utf-8") as f:
#     data = json.load(f)
#     for k, v in data.items():
#         print(k)
#         print(v)
#

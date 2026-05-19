# form_* split for fx-9860GIII (<=300 lines/editor)
from form_ui import *

def termo_tryck():
    p(
"== Tryck\n"
"p = F/A\n"
"Vatsketryck:\n"
" p = p0 + rho*g*h\n"
"Arkimedes:\n"
" F = rho_v*V*g\n"
"Ideala gaslagen:\n"
" pV/T = konst\n"
" pV = nRT\n"
" R=8.314 J/(mol*K)"
    )


def termo_varme():
    p(
"== Varme\n"
"E = c*m*dT\n"
"Smaltvarme: E = l_s*m\n"
"Angb.varme: E = l_a*m\n"
"Metod:\n"
" temp.andring och\n"
" fasbyte separat"
    )


def termo_huvudsats():
    p(
"== Termodynamik\n"
"1:a lagen:\n"
" dU = Q + W\n"
"Gasarbete:\n"
" W = -p*dV\n"
"Verkn.grad motor:\n"
" eta = W/Q_in\n"
"Teckenkonv:\n"
" Q in: positivt\n"
" W pa systemet: pos"
    )


def termo_tab_c():
    p(
"== Spec varme c\n"
"  (kJ/(kg*K))\n"
"aluminium  0.90\n"
"jarn       0.44\n"
"koppar     0.39\n"
"massing    0.38\n"
"silver     0.24\n"
"vatten     4.18\n"
"volfram    0.14"
    )


def termo_tab_l():
    p(
"== Smalt/angbildn\n"
"l_s (kJ/kg):\n"
" is       334\n"
" jarn     276\n"
" koppar   205\n"
"l_a (kJ/kg):\n"
" vatten  2260"
    )


def termo_tab_rho():
    p(
"== Densitet rho\n"
"  (g/cm^3)\n"
"aluminium  2.70\n"
"bly       11.35\n"
"guld      19.30\n"
"jarn       7.87\n"
"koppar     8.96\n"
"silver    10.50"
    )


def termo_tab_resi():
    p(
"== Resistivitet\n"
" (ohm*mm^2/m)\n"
"guld    0.0235\n"
"koppar  0.0172\n"
"silver  0.0159"
    )


def termo():
    while True:
        v = choose("= TERMOFYSIK =", [
            "1 Tryck/gaslag",
            "2 Varme/fasbyte",
            "3 1:a huvudsats",
            "4 Tab c",
            "5 Tab l_s/l_a",
            "6 Tab densitet",
            "7 Tab resistivitet",
        ])
        if v == "0":
            return
        elif v == "1":
            termo_tryck()
        elif v == "2":
            termo_varme()
        elif v == "3":
            termo_huvudsats()
        elif v == "4":
            termo_tab_c()
        elif v == "5":
            termo_tab_l()
        elif v == "6":
            termo_tab_rho()
        elif v == "7":
            termo_tab_resi()

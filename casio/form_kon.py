# form_* split for fx-9860GIII (<=300 lines/editor)
from form_ui import *

def kon_grund():
    p(
"== Konstanter 1\n"
"c   = 3.00e8 m/s\n"
"v_lj= 340 m/s\n"
"e   = 1.602e-19 C\n"
"m_e = 9.109e-31 kg\n"
"G   = 6.674e-11\n"
"h   = 6.626e-34 Js\n"
"N_A = 6.022e23 /mol\n"
"k_B = 1.381e-23 J/K"
    )


def kon_fysik():
    p(
"== Konstanter 2\n"
"sigma = 5.67e-8\n"
"a_W   = 2.898e-3\n"
"k_C   = 8.988e9\n"
"eps0  = 8.854e-12\n"
"mu0 = 4*pi*1e-7\n"
"k_C = 1/(4*pi*eps0)"
    )


def kon_omr():
    p(
"== Omrakningar\n"
"1 eV = 1.602e-19 J\n"
"1 u  = 1.661e-27 kg\n"
"1 u  = 931.494 MeV\n"
"1 kcal = 4186.8 J\n"
"1 kWh  = 3.6e6 J\n"
"1 hk   = 735.5 W\n"
"1 bar  = 1.00e5 Pa\n"
"1 mmHg = 133 Pa\n"
"E*lam = 1240 eV*nm"
    )


def kon_nuklid():
    p(
"== Nuklider\n"
"m_p = 1.007276 u\n"
"m_n = 1.008665 u\n"
"He-4 = 4.002602 u"
    )


def konst():
    while True:
        v = choose("= KONSTANTER =", [
            "1 Grund (c,e,h,G)",
            "2 Fysik (sigma,k)",
            "3 Omrakningar",
            "4 Nuklider",
        ])
        if v == "0":
            return
        elif v == "1":
            kon_grund()
        elif v == "2":
            kon_fysik()
        elif v == "3":
            kon_omr()
        elif v == "4":
            kon_nuklid()


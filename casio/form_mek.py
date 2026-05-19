# form_* split for fx-9860GIII (<=300 lines/editor)
from form_ui import *

def mek_kinematik():
    p(
"== MEKANIK kinematik\n"
"v_m = ds/dt\n"
"a_m = dv/dt\n"
"Konst hast: s = v*t\n"
"Konst acc:\n"
" s = v0*t + a*t^2/2\n"
" v = v0 + a*t\n"
" v_m = (v0+v)/2"
    )


def mek_kast():
    p(
"== MEKANIK kast\n"
"a_h = 0\n"
"v_h = v0*cos(a)\n"
"x = v0*cos(a)*t\n"
"a_v = -g\n"
"v_v = v0*sin(a) - g*t\n"
"y = v0*sin(a)*t\n"
"    - g*t^2/2"
    )


def mek_kast2():
    p(
"== MEKANIK kast 2\n"
"Stighojd:\n"
" h = v0^2*sin(a)^2\n"
"     /(2g)\n"
"Kastvidd:\n"
" s = v0^2*sin(2a)/g"
    )


def mek_central():
    p(
"== MEKANIK rotation\n"
"w = dT/dt  T=w*t\n"
"v = w*r\n"
"a_c = v^2/r = r*w^2\n"
"    = 4*pi^2*r/T^2\n"
"--- svangning ---\n"
"w = sqrt(k/m)\n"
"x = A*sin(w*t)\n"
"T = 2*pi*sqrt(m/k)"
    )


def mek_krafter():
    p(
"== MEKANIK krafter\n"
"F_res = m*a\n"
"F = G*m1*m2/r^2\n"
"F = k*dl  (Hooke)\n"
"F = mu*F_N\n"
"M = F*l\n"
"summa M = 0"
    )


def mek_lutande():
    p(
"== Lutande plan\n"
"Langs planet:\n"
" F_par = m*g*sin(a)\n"
"Mot planet:\n"
" F_N = m*g*cos(a)\n"
"Friktion (vila):\n"
" F_f <= mu_s*F_N\n"
"Glidande:\n"
" F_f = mu_k*F_N"
    )


def mek_energi():
    p(
"== MEKANIK energi\n"
"W = F_s*s\n"
" F_s = kraftkomp\n"
"     i rorelseriktn\n"
"E_p = m*g*h\n"
"E_k = m*v^2/2\n"
"E = E_p + E_k\n"
"P = dE/dt = F_s*v\n"
"verk: eta = E_n/E_t"
    )


def mek_rorelse():
    p(
"== Rorelsemangd\n"
"p = m*v\n"
"I = F*t\n"
"I = dp\n"
"summa p_i = konst\n"
"Stot:\n"
" elastisk: E_k bevar\n"
" oelastisk: bara p"
    )


def mekanik():
    while True:
        v = choose("= MEKANIK =", [
            "1 Kinematik",
            "2 Kastrorelse 1",
            "3 Kastrorelse 2",
            "4 Rotation/svangn",
            "5 Krafter",
            "6 Lutande plan",
            "7 Energi/effekt",
            "8 Rorelsemangd",
        ])
        if v == "0":
            return
        elif v == "1":
            mek_kinematik()
        elif v == "2":
            mek_kast()
        elif v == "3":
            mek_kast2()
        elif v == "4":
            mek_central()
        elif v == "5":
            mek_krafter()
        elif v == "6":
            mek_lutande()
        elif v == "7":
            mek_energi()
        elif v == "8":
            mek_rorelse()

# form_* split for fx-9860GIII (<=300 lines/editor)
from form_ui import *

def vag_grund():
    p(
"== VAGOR grund\n"
"f = 1/T\n"
"w = 2*pi/T\n"
"v = lambda*f\n"
"Staende vag str:\n"
" L = k*lambda/2"
    )


def vag_doppler():
    p(
"== Doppler\n"
"Mekanisk:\n"
" f_o = f_k *\n"
"   (v+v_o)/(v-v_k)\n"
"v_o och v_k positiva\n"
"riktade mot varandra\n"
"EM (small v/c):\n"
" lambda/lambda0 ~\n"
"   1 + v/c"
    )


def vag_interf():
    p(
"== Interferens\n"
"Konstr: ds = k*lam\n"
" k = 0,1,2,...\n"
"Destr:\n"
" ds = (k+1/2)*lam\n"
"Gitter:\n"
" n*lam = d*sin(a_n)\n"
" n_max = floor(d/lam)\n"
" tot max = 2n_max+1"
    )


def vag_brytning():
    p(
"== Brytning\n"
"Snell:\n"
" sin(a_i)/sin(a_r)\n"
"  = v_i/v_r\n"
" n1*sin(a1)\n"
"  = n2*sin(a2)\n"
"n = c/c_m\n"
"Totalref:\n"
" sin(a_k) = n2/n1\n"
" om n1 > n2"
    )


def vag_lins():
    p(
"== Linsformel\n"
"1/f = 1/a + 1/b\n"
"M = B/F = b/a\n"
"Tecken:\n"
" reell bild: b > 0\n"
" virtuell:   b < 0"
    )


def vag_index():
    p(
"== Brytningsindex\n"
"luft     1.00\n"
"vatten   1.33\n"
"etanol   1.36\n"
"glas     1.50\n"
"diamant  2.47"
    )


def vagor():
    while True:
        v = choose("= VAGOR / OPTIK =", [
            "1 Grund (f,v,lam)",
            "2 Doppler",
            "3 Interferens/gitter",
            "4 Brytning/totalref",
            "5 Linsformel",
            "6 Brytningsindex",
        ])
        if v == "0":
            return
        elif v == "1":
            vag_grund()
        elif v == "2":
            vag_doppler()
        elif v == "3":
            vag_interf()
        elif v == "4":
            vag_brytning()
        elif v == "5":
            vag_lins()
        elif v == "6":
            vag_index()

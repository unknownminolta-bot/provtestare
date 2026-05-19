# form_* split for fx-9860GIII (<=300 lines/editor)
from form_ui import *

def mod_relativ():
    p(
"== Relativitet\n"
"gamma = 1/sqrt(1 -\n"
"          v^2/c^2)\n"
"Tid: t = gamma*t0\n"
"Langd: l = l0/gamma\n"
"p = gamma*m0*v\n"
"E = gamma*m0*c^2\n"
"E0 = m0*c^2\n"
"E_k = E - E0"
    )


def mod_em():
    p(
"== EM/varmestraln\n"
"M = P/A\n"
"Wiens lag:\n"
" lambda_max*T = a\n"
" a=2.898e-3 K*m\n"
"Stefan-Boltzmann:\n"
" M = sigma*T^4\n"
" sigma=5.67e-8\n"
"  W/(m^2*K^4)"
    )


def mod_radio():
    p(
"== Radioaktivitet\n"
"Alfa: utsander He-4\n"
" A: -4   Z: -2\n"
"Beta-: n -> p+e+anti\n"
" A: 0    Z: +1\n"
"Beta+: p -> n+e++neu\n"
" A: 0    Z: -1\n"
"Gamma: foton, A,Z\n"
" oforandrade"
    )


def mod_sonderfall():
    p(
"== Sonderfall\n"
"lambda = ln2/T_halv\n"
"N = N0*(1/2)^(t/T_h)\n"
"  = N0*exp(-lam*t)\n"
"A = lambda*N\n"
"A = A0*(1/2)^(t/T_h)\n"
"Q = (m_fore -\n"
"     m_efter)*c^2\n"
"Beta+: ofta -2*m_e"
    )


def mod_absorption():
    p(
"== Absorption\n"
"mu = ln2/d_halv\n"
"I = I0*(1/2)^(x/d_h)\n"
"  = I0*exp(-mu*x)\n"
"Energi fran massdef:\n"
" E = dm*c^2\n"
" 1 u = 931.5 MeV"
    )


def mod_atom():
    p(
"== Atom/kvant\n"
"Foton: E = h*f\n"
"     = h*c/lambda\n"
"Snabb: lam(nm)=1240\n"
"          /E(eV)\n"
"Foton p = E/c\n"
"      = h/lambda\n"
"de Broglie:\n"
" lambda = h/p\n"
"Vate: E_n =\n"
" -13.6 eV / n^2"
    )


def mod_foto_rontg():
    p(
"== Fotoeffekt/Rontg\n"
"h*f = W_u + E_k\n"
"W_u = uttradesarbete\n"
"f0 = W_u/h\n"
"Elektron acc U volt:\n"
" E_k = e*U\n"
" p = sqrt(2*m*E_k)\n"
"Rontgenror:\n"
" lam_min = h*c/(e*U)\n"
" f_max = e*U/h"
    )


def mod_astro():
    p(
"== Astrofysik\n"
"Flykthast:\n"
" v = sqrt(2*G*m/R)\n"
"Schwarzschild:\n"
" r_S = 2*G*m/c^2\n"
"Rodforskj:\n"
" z = (lam-lam0)/lam0\n"
"   ~ v/c\n"
"Hubble:\n"
" v = H0*d\n"
" H0 ~ 70 km/s/Mpc"
    )


def mod_uttr():
    p(
"== Uttradesarbete\n"
" W_u (eV)\n"
"aluminium  2.81\n"
"bly        4.25\n"
"cesium     1.94\n"
"kadmium    4.00\n"
"kalcium    3.20\n"
"kalium     2.24\n"
"natrium    2.46\n"
"silver     4.61"
    )


def modern():
    while True:
        v = choose("= MODERN FYSIK =", [
            "1 Relativitet",
            "2 EM/varmestraln",
            "3 Radioaktivitet",
            "4 Sonderfall",
            "5 Absorption/dm",
            "6 Atom/kvant",
            "7 Foto/Rontg",
            "8 Astrofysik",
            "9 Uttr.arbete",
        ])
        if v == "0":
            return
        elif v == "1":
            mod_relativ()
        elif v == "2":
            mod_em()
        elif v == "3":
            mod_radio()
        elif v == "4":
            mod_sonderfall()
        elif v == "5":
            mod_absorption()
        elif v == "6":
            mod_atom()
        elif v == "7":
            mod_foto_rontg()
        elif v == "8":
            mod_astro()
        elif v == "9":
            mod_uttr()


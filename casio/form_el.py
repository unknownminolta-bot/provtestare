# form_* split for fx-9860GIII (<=300 lines/editor)
from form_ui import *

def el_grund():
    p(
"== EL grund\n"
"F = k*Q1*Q2/r^2\n"
"I = Q/t\n"
"U = W/Q\n"
"R = U/I\n"
"U = R*I  (Ohm)"
    )


def el_kretsar():
    p(
"== EL kretsar\n"
"Kirchhoff strom:\n"
" sum I_in = sum I_ut\n"
"Kirchhoff U:\n"
" U = U1 + ... + Un\n"
"Serie:\n"
" R = R1+...+Rn\n"
"Parallell:\n"
" 1/R = 1/R1+...\n"
"Tva parallella:\n"
" R = R1*R2/(R1+R2)\n"
"Polspann (urladdn):\n"
" U = emf - R_i*I"
    )


def el_effekt_falt():
    p(
"== Effekt och falt\n"
"P = U*I\n"
"P = U^2/R = R*I^2\n"
"E_falt = F/q\n"
"Homogent: E = U/d\n"
"k = 1/(4*pi*eps0)"
    )


def el_kondens():
    p(
"== Kondensator\n"
"C = Q/U\n"
"Plattkondensator:\n"
" C = eps0*eps_r*A/d\n"
"Parallell: C = C1+C2\n"
"Serie: 1/C = 1/C1+\n"
"            1/C2\n"
"E = QU/2 = CU^2/2\n"
"Tau (RC) = R*C"
    )


def el_magnetfalt():
    p(
"== Magnetfalt\n"
"Lang ledare:\n"
" B = mu*I/(2*pi*a)\n"
"Platt spole:\n"
" B = mu*N*I/(2r)\n"
"Solenoid:\n"
" B = mu*N*I/l\n"
"Krafter:\n"
" F = q*v*B*sin(a)\n"
" F = l*I*B*sin(a)"
    )


def el_induktion():
    p(
"== Induktion\n"
"Flode:\n"
" phi = B*A*cos(t)\n"
"Generator:\n"
" e = l*v*B\n"
"Induktionslagen:\n"
" u = -dphi/dt\n"
"Spole: u = -N*dphi/dt\n"
"Lenz:\n"
" minus visar motverk.\n"
"Induktans:\n"
" L = dphi/dI\n"
" u = -L*dI/dt"
    )


def el_vaxel():
    p(
"== Vaxelstrom\n"
"u = u_max*sin(w*t)\n"
"i = i_max*sin(w*t)\n"
"Effektivvarde:\n"
" U = u_max/sqrt(2)\n"
" I = i_max/sqrt(2)\n"
"Transformator:\n"
" N1/N2 = U1/U2\n"
"     = I2/I1"
    )


def elmagn():
    while True:
        v = choose("= EL/MAGNETISM =", [
            "1 Grund (Coulomb)",
            "2 Kretsar",
            "3 Effekt och falt",
            "4 Kondensator/RC",
            "5 Magnetfalt/kraft",
            "6 Induktion/Lenz",
            "7 Vaxelstrom",
        ])
        if v == "0":
            return
        elif v == "1":
            el_grund()
        elif v == "2":
            el_kretsar()
        elif v == "3":
            el_effekt_falt()
        elif v == "4":
            el_kondens()
        elif v == "5":
            el_magnetfalt()
        elif v == "6":
            el_induktion()
        elif v == "7":
            el_vaxel()

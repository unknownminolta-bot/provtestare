# form_* split for fx-9860GIII (<=300 lines/editor)
from form_ui import *

def kemi_mol():
    p(
"== Mol/gas/konc\n"
"n = m/M\n"
"N = n*N_A\n"
"pV = nRT\n"
"R = 8.314 J/(mol*K)\n"
"p*V/T = konst\n"
" (n konst)\n"
"c = n/V\n"
"V i L for mol/L\n"
"T i K, p i Pa\n"
" om R=8.314"
    )


def kemi_stok():
    p(
"== Stokiometri\n"
"Balansera till\n"
" CO2 och H2O\n"
"Spar:\n"
" m -> n bransle\n"
" -> mol CO2/H2O\n"
" -> massa\n"
"Begransande reakt:\n"
" min n/koeff\n"
"Utbyte =\n"
" m_verklig/m_teor\n"
" * 100%"
    )


def kemi_oxid():
    p(
"== Oxidationstal\n"
"Fria grundamnen: 0\n"
"Monatom jon:\n"
" som laddning\n"
"O oftast -2\n"
" (peroxid undantag)\n"
"H oftast +1\n"
"Summa neutral mol=0\n"
"Summa i jon = laddn"
    )


def kemi_redox():
    p(
"== Redox sur\n"
"1 Dela ox och red\n"
"2 Bala amne utom O,H\n"
"3 O med H2O\n"
"4 H med H+\n"
"5 Laddning med e-\n"
"6 Mult halvreak.\n"
"  och addera\n"
"--- basisk ---\n"
"Gor som sur, lagg\n"
"OH- pa bada sidor,\n"
"stryk H2O"
    )


def kemi_elektro():
    p(
"== Elektrokemi\n"
"Tabell = reduktion\n"
"Spontan om E(cell)>0\n"
"E0(cell) =\n"
" E0(katod)\n"
" - E0(anod)\n"
"Bada som reduktion\n"
"katod: hogre E0\n"
"anod:  lagre E0\n"
"Nernst:\n"
" E = E0 -\n"
"   (RT/(n*F))*lnQ\n"
"Elektrolys:\n"
" m = M*I*t/(z*F)"
    )


def kemi_syrabas():
    p(
"== Syra-bas\n"
"pH = -lg[H+]\n"
"pOH = -lg[OH-]\n"
"pH + pOH = 14\n"
" vid 25 grader C\n"
"Stark syra:\n"
" [H+] = c\n"
"Svag syra:\n"
" Ka = [H+][A-]/[HA]\n"
"Buffert:\n"
" pH = pKa +\n"
"  lg([bas]/[syra])\n"
"H2SO4 inte alltid c"
    )


def kemi_titr():
    p(
"== Titrering\n"
"Spadning (samma am):\n"
" c1*V1 = c2*V2\n"
"Stark s-b 1:1:\n"
" c1*V1 = c2*V2\n"
"Vid ekvivalens:\n"
" n(H+) = n(OH-)\n"
"Inte 1:1:\n"
" anvand reaktions-\n"
" koefficienter"
    )


def kemi_blandn():
    p(
"== Blandning joner\n"
"Per jon:\n"
" n = c1*V1 + c2*V2\n"
"   + ...\n"
"[jon] = n/V_tot\n"
"V_tot = sum volymer\n"
"Fallning:\n"
" Q_sp > K_sp ger\n"
" fallning"
    )


def kemi_metallsyr():
    p(
"== Gas + metall+syra\n"
"pV = nRT (T i K)\n"
"Mg + 2 H+ ->\n"
" Mg2+ + H2\n"
"n(H2) = n(Mg)\n"
"R ~ 8.31 om tenta\n"
"saknar siffror"
    )


def kemi_kalorimetri():
    p(
"== Kalorimetri\n"
"Q = m*c*dT\n"
"Per mol reaktant:\n"
" Q/n  (kJ/mol)\n"
"Tecken:\n"
" Q in: positivt\n"
" Q ut: negativt"
    )


def kemi_lab():
    p(
"== Lab/sulfat\n"
"Kristallvatten:\n"
" CuSO4 * x H2O\n"
" m(H2O)/M(H2O)\n"
"  = x*n(salt)\n"
"--- Sulfattest ---\n"
"Ba2+ + SO4 2-\n"
" -> BaSO4(s)\n"
"Reagens: Ba2+-salt\n"
" t.ex. BaCl2"
    )


def kemi_jamvikt():
    p(
"== Jamvikt\n"
"Kc =\n"
" [C]^c*[D]^d /\n"
" ([A]^a*[B]^b)\n"
"Kp = Kc*(RT)^(dn)\n"
" dn = sum gas-koeff\n"
"Q jamfor med K:\n"
" Q<K framat\n"
" Q>K bakat\n"
"ICE-tabell:\n"
" start, andring,\n"
" jamvikt\n"
"Le Chatelier:\n"
" motverkar storning"
    )


def kemi_termo():
    p(
"== Termo (kemi)\n"
"dG = dH - T*dS\n"
"dG = -n*F*E\n"
"dG0 = -R*T*lnK\n"
"Hess: summera dH\n"
"F = 96485 C/mol\n"
"dG<0: spontan\n"
" (sager inget om\n"
"  hastighet)"
    )


def kemi_kinetik():
    p(
"== Kinetik\n"
"v = k*[A]^m\n"
"m bestams\n"
" experimentellt,\n"
" inte fran balans-\n"
" koefficienter\n"
"1:a ordning:\n"
" ln([A]0/[A]) = k*t\n"
" t_halv = ln2/k"
    )


def kemi():
    while True:
        v = choose("= KEMI =", [
            "1 Mol/gas/konc",
            "2 Stokiometri",
            "3 Oxidationstal",
            "4 Redox sur/bas",
            "5 Elektrokemi",
            "6 Syra/buffert",
            "7 Titr/spadning",
            "8 Blandning/Ksp",
            "9 Gas metall+syra",
            "10 Kalorimetri",
            "11 Lab/sulfat",
            "12 Jamvikt/Q/ICE",
            "13 Termo/Hess",
            "14 Kinetik",
        ])
        if v == "0":
            return
        elif v == "1":
            kemi_mol()
        elif v == "2":
            kemi_stok()
        elif v == "3":
            kemi_oxid()
        elif v == "4":
            kemi_redox()
        elif v == "5":
            kemi_elektro()
        elif v == "6":
            kemi_syrabas()
        elif v == "7":
            kemi_titr()
        elif v == "8":
            kemi_blandn()
        elif v == "9":
            kemi_metallsyr()
        elif v == "10":
            kemi_kalorimetri()
        elif v == "11":
            kemi_lab()
        elif v == "12":
            kemi_jamvikt()
        elif v == "13":
            kemi_termo()
        elif v == "14":
            kemi_kinetik()

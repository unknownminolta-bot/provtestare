# form_* split for fx-9860GIII (<=300 lines/editor)
from form_ui import *
from form_mek import *
from form_vag import *
from form_el import *
from form_ter import *
from form_mod import *
from form_kon import *
from formkemi import *

# ---------- HUVUDMENY ----------

def meny():
    while True:
        v = choose("== FORMLER FYXF04 ==", [
            "1 Mekanik",
            "2 Vagor/optik",
            "3 El/magnetism",
            "4 Termofysik",
            "5 Modern fysik",
            "6 Konstanter",
            "7 Kemi",
        ], back="0 Avsluta")
        if v == "0":
            return
        elif v == "1":
            mekanik()
        elif v == "2":
            vagor()
        elif v == "3":
            elmagn()
        elif v == "4":
            termo()
        elif v == "5":
            modern()
        elif v == "6":
            konst()
        elif v == "7":
            kemi()


# ---------- TEST/EMULATOR HOOK ----------

def _menu_screen(title, items, back="0 Tillbaka"):
    def _fn():
        lines = [title] + items + [back]
        for start in range(0, len(lines), 7):
            for line in lines[start:start + 7]:
                print(line)
            if start + 7 < len(lines):
                wait()
    _fn.__name__ = title.strip("= ").lower().replace(" ", "_") + "_menu"
    return _fn


def all_pages():
    yield _menu_screen(
        "== FORMLER FYXF04 ==",
        ["1 Mekanik", "2 Vagor/optik", "3 El/magnetism",
         "4 Termofysik", "5 Modern fysik", "6 Konstanter", "7 Kemi"],
        back="0 Avsluta",
    )

    yield _menu_screen(
        "= MEKANIK =",
        ["1 Kinematik", "2 Kastrorelse 1", "3 Kastrorelse 2",
         "4 Rotation/svangn", "5 Krafter", "6 Lutande plan",
         "7 Energi/effekt", "8 Rorelsemangd"],
    )
    yield mek_kinematik
    yield mek_kast
    yield mek_kast2
    yield mek_central
    yield mek_krafter
    yield mek_lutande
    yield mek_energi
    yield mek_rorelse

    yield _menu_screen(
        "= VAGOR / OPTIK =",
        ["1 Grund (f, v, lam)", "2 Doppler", "3 Interferens/gitter",
         "4 Brytning/totalref", "5 Linsformel", "6 Brytningsindex"],
    )
    yield vag_grund
    yield vag_doppler
    yield vag_interf
    yield vag_brytning
    yield vag_lins
    yield vag_index

    yield _menu_screen(
        "= EL/MAGNETISM =",
        ["1 Grund (Coulomb)", "2 Kretsar", "3 Effekt och falt",
         "4 Kondensator/RC", "5 Magnetfalt/krafter",
         "6 Induktion/Lenz", "7 Vaxelstrom"],
    )
    yield el_grund
    yield el_kretsar
    yield el_effekt_falt
    yield el_kondens
    yield el_magnetfalt
    yield el_induktion
    yield el_vaxel

    yield _menu_screen(
        "= TERMOFYSIK =",
        ["1 Tryck/gaslag", "2 Varme/fasbyte", "3 1:a huvudsats",
         "4 Tab c", "5 Tab l_s/l_a", "6 Tab densitet",
         "7 Tab resistivitet"],
    )
    yield termo_tryck
    yield termo_varme
    yield termo_huvudsats
    yield termo_tab_c
    yield termo_tab_l
    yield termo_tab_rho
    yield termo_tab_resi

    yield _menu_screen(
        "= MODERN FYSIK =",
        ["1 Relativitet", "2 EM/varmestraln", "3 Radioaktivitet",
         "4 Sonderfallslagen", "5 Absorption/dm", "6 Atom/kvant",
         "7 Fotoeffekt/Rontg", "8 Astrofysik", "9 Uttradesarbete"],
    )
    yield mod_relativ
    yield mod_em
    yield mod_radio
    yield mod_sonderfall
    yield mod_absorption
    yield mod_atom
    yield mod_foto_rontg
    yield mod_astro
    yield mod_uttr

    yield _menu_screen(
        "= KONSTANTER =",
        ["1 Grund (c,e,h,G)", "2 Fysik (sigma,k)",
         "3 Omrakningar", "4 Nuklider"],
    )
    yield kon_grund
    yield kon_fysik
    yield kon_omr
    yield kon_nuklid

    yield _menu_screen(
        "= KEMI =",
        ["1 Mol/gas/konc", "2 Stokiometri", "3 Oxidationstal",
         "4 Redox sur/basisk", "5 Elektrokemi", "6 Syra/buffert",
         "7 Titrering/spadning", "8 Blandning/Ksp",
         "9 Gas metall+syra", "10 Kalorimetri",
         "11 Lab/sulfat", "12 Jamvikt/Q/ICE",
         "13 Termo/Hess", "14 Kinetik"],
    )
    yield kemi_mol
    yield kemi_stok
    yield kemi_oxid
    yield kemi_redox
    yield kemi_elektro
    yield kemi_syrabas
    yield kemi_titr
    yield kemi_blandn
    yield kemi_metallsyr
    yield kemi_kalorimetri
    yield kemi_lab
    yield kemi_jamvikt
    yield kemi_termo
    yield kemi_kinetik


if __name__ == "__main__":
    try:
        meny()
    except KeyboardInterrupt:
        pass

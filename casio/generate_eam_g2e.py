#!/usr/bin/env python3
"""Generate .eam files with Eact Maker markup for proper math rendering.

Uses \\frac{}{}, ^{}, _{}, and \\func; codes for Greek/special chars.
Then submits to planet-casio EactMaker to produce .g2e files.

Usage:
  python generate_eam_g2e.py          # generate .eam files only
  python generate_eam_g2e.py --convert  # also convert to .g2e via EactMaker
"""

import re
import sys
import os
import urllib.request
import urllib.parse
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
OUT_DIR = SCRIPT_DIR / "g2e_out"

SECTIONS = {
    "MEKANIK": {
        "title": "MEKANIK",
        "content": r"""== MEKANIK & R\ouml;RELSE ==

--- INTRODUKTION ---
Densitet
 \rho; = \frac{m}{V}

--- KINEMATIK ---
Medelhastighet
 v = \frac{\Delta;s}{\Delta;t}
Medelacceleration
 a = \frac{\Delta;v}{\Delta;t}

Konstant hastighet:
 s = v\times;t

Konst. acceleration:
 s = v\subs0;t + \frac{at^{2}}{2}
 v = v\subs0; + at
 v\submi; = \frac{v\subs0;+v}{2}

--- KASTRORELSE ---
Horisontellt:
 a\submi;=0, v\submi;=v\subs0;cos(\alpha;)
 x = v\subs0;cos(\alpha;)t
Vertikalt:
 a\submi;=\minus;g
 v\submi;=v\subs0;sin(\alpha;)\minus;gt
 y=v\subs0;sin(\alpha;)t \minus; \frac{gt^{2}}{2}
Stigh\ouml;jd:
 h = \frac{v\subs0;^{2}sin^{2}(\alpha;)}{2g}
Kastvidd:
 s = \frac{v\subs0;^{2}sin(2\alpha;)}{g}

--- CENTRALR\ouml;RELSE ---
Vinkelhast. \omega; = \frac{\Delta;\theta;}{\Delta;t}
Konst: \theta; = \omega;t
Banhast. v = \omega;r
Centrip.acc:
 a\subc; = \frac{v^{2}}{r} = r\omega;^{2}
    = \frac{4\pi;^{2}r}{T^{2}}

--- HARM. SV\Auml;NGN. ---
Vinkelfrekvens:
 \omega; = \sqrt{\frac{k}{m}}
Elongation:
 x = Asin(\omega;t)
Period:
 T = 2\pi;\sqrt{\frac{m}{k}}
Pot. energi:
 E\subp; = \frac{kx^{2}}{2}
Pendel:
 T = 2\pi;\sqrt{\frac{l}{g}}

--- KRAFTER ---
Newtons andra lag:
 F\submi; = ma
Gravitation:
 F\subG; = \frac{Gm\subs1;m\subs2;}{r^{2}}
Hookes lag:
 F\submi; = k\Delta;l
Friktion:
 F\subf; = \mu;F\subN;

--- GRAVITATION ---
Keplers 3:e lag:
 \frac{T^{2}}{r^{3}} = konst

--- KRAFTMOMENT ---
 M = Fl
Momentlagen:
 \Sigma;M = 0

--- ENERGI ---
Arbete: W = F\subs;s
Energi: \Delta;E = W
L\auml;gesenergi: E\subp;=mgh
R\ouml;relseenergi:
 E\subk; = \frac{mv^{2}}{2}
Mek. energi:
 E = E\subp; + E\subk;
Effekt: P = \frac{\Delta;E}{\Delta;t}
 P = F\subs;v
Verkningsgrad:
 \eta; = \frac{E\submi;}{E\submi;}

--- R\ouml;RELSEM\Auml;NGD ---
 p = mv
Impuls: I = Ft
Impulslagen: I = \Delta;p
Bevarandelagen:
 \Sigma;p\subi; = konst
"""
    },
    "VAGOR": {
        "title": "VAGOR",
        "content": r"""== V\aring;GOR & OPTIK ==

--- V\aring;GR\ouml;RELSE ---
Frekvens: f = \frac{1}{T}
Vinkelfrekvens:
 \omega; = \frac{2\pi;}{T}
Utbredningshastig.:
 v = \lambda;f
St\aring;ende v\aring;g i str\auml;ng
 L = \frac{k\lambda;}{2}

--- DOPPLEREFFEKT ---
Mekanisk:
 f\subo; = f\subk;\frac{v+v\subo;}{v\minus;v\subk;}

EM-Doppler:
 \frac{\lambda;}{\lambda;\subs0;} = \sqrt{\frac{1+\frac{v}{c}}{1\minus;\frac{v}{c}}}
 \approx; 1 + \frac{v}{c}

--- INTERFERENS ---
Konstruktiv:
 \Delta;s = k\lambda;
 (k=0,1,2,...)
Destruktiv:
 \Delta;s = (k+\frac{1}{2})\lambda;

--- GITTERFORMELN ---
 n\lambda; = dsin(\alpha;\subn;)

d = gitterkonstant
n = ordning (0,1,2..)
\alpha;\subn; = vinkel for max n

Max antal ordningar:
 n\submi; = \frac{d}{\lambda;}
 (avrunda nedat)
Totalt antal max:
 2n\submi; + 1

--- BRYTNING ---
Snells lag:
 \frac{sin(\alpha;\subi;)}{sin(\alpha;\subb;)} = \frac{v\subi;}{v\subb;}

Med brytningsindex:
 n\subs1;sin(\alpha;\subs1;) = n\subs2;sin(\alpha;\subs2;)

Brytningsindex:
 n = \frac{c}{c\subm;}

Totalreflektion vid:
 sin(\alpha;\subg;) = \frac{n\subs2;}{n\subs1;}
 (n\subs1; > n\subs2;)

--- BRYTNINGSINDEX ---
luft      1.00
vatten    1.33
etanol    1.36
glas      1.50
diamant   2.47
"""
    },
    "ELMAGN": {
        "title": "ELMAGN",
        "content": r"""== EL & MAGNETISM ==

--- ELEKTRICITET ---
Coulombs lag:
 F = \frac{kQ\subs1;Q\subs2;}{r^{2}}

Str\ouml;m: I = \frac{Q}{t}
Sp\auml;nning: U = \frac{W}{Q}
Resistans: R = \frac{U}{I}
Ohms lag: U = RI

--- KRETSAR ---
Kirchhoff str\ouml;m:
 \Sigma;I\submi; = \Sigma;I\submi;

Kirchhoff sp\auml;nning:
 U = U\subs1; + ... + U\subn;

Seriekoppling:
 R = R\subs1; + ... + R\subn;

Parallellkoppling:
 \frac{1}{R} = \frac{1}{R\subs1;}+...+\frac{1}{R\subn;}

Tva parallella:
 R = \frac{R\subs1;R\subs2;}{R\subs1;+R\subs2;}

Polsp\auml;nning:
 U = \epsilon; \minus; R\subi;I

Effekt:
 P = UI
 P = \frac{U^{2}}{R} = RI^{2}

--- EL. FALT ---
Faltstyrka:
 E = \frac{F}{q}
Homogent falt:
 E = \frac{U}{d}
Potentialskillnad:
 U\subA;\subB; = |V\subA; \minus; V\subB;|

--- KONDENSATOR ---
Kapacitans: C = \frac{Q}{U}
Plattkondensator:
 C = \frac{\epsilon;\subs0;\epsilon;\subr;A}{d}
Lagrad energi:
 E = \frac{QU}{2} = \frac{CU^{2}}{2}

--- MAGNETISM ---
Fl\ouml;dest\auml;th. ledare:
 B = \frac{\mu;I}{2\pi;a}
Platt spole:
 B = \frac{N\mu;I}{r}
Solenoid:
 B = \frac{N\mu;I}{l}

Kraft p\aring; laddning:
 F = qvB
Kraft p\aring; ledare:
 F = lIB

--- INDUKTION ---
Magn. fl\ouml;de:
 \phi; = BA
Generatorformeln:
 e = lvB
Induktionslagen:
 u = \minus;\frac{\Delta;\phi;}{\Delta;t}
Spole:
 u = \minus;N\frac{\Delta;\phi;}{\Delta;t}
Induktans:
 L = \frac{\Delta;\phi;}{\Delta;I}
 u = \minus;L\frac{\Delta;i}{\Delta;t}

--- V\Auml;XELSTR\Ouml;M ---
V\auml;xelsp\auml;nning:
 u = u\submi;sin(\omega;t)
V\auml;xelstr\ouml;m:
 i = i\submi;sin(\omega;t)
Effektivv\auml;rde:
 U = \frac{u\submi;}{\sqrt{2}}
 I = \frac{i\submi;}{\sqrt{2}}

Transformator:
 \frac{N\subs1;}{N\subs2;} = \frac{U\subs1;}{U\subs2;} = \frac{I\subs2;}{I\subs1;}
"""
    },
    "TERMO": {
        "title": "TERMO",
        "content": r"""== TERMOFYSIK ==

--- TRYCK ---
Tryck: p = \frac{F}{A}
V\auml;tsketryck:
 p = p\subs0; + \rho;gh
Arkimedes princip:
 F\submi; = \rho;\subv;Vg

Ideala gaslagen:
 \frac{pV}{T} = konst

--- V\Auml;RME ---
V\auml;rme och temperatur:
 E = cm\Delta;T

Sm\auml;ltv\auml;rme:
 E = l\subs;m
\Aring;ngbildningsv\auml;rme:
 E = l\suba;m

--- SPEC V\Auml;RME c ---
 (kJ/(kgK))
aluminium  0.90
jaern      0.44
koppar     0.39
maessing   0.38
silver     0.24
vatten     4.18
volfram    0.14

--- SM\Auml;LTENTALPITET ---
 l\subs; (kJ/kg)
is       334
jaern    276
koppar   205

--- \Aring;NGBILDN.ENT. ---
 l\suba; (kJ/kg)
vatten   2260

--- DENSITET ---
 \rho; (g/cm^{3})
aluminium  2.70
bly       11.35
guld      19.30
jaern      7.87
koppar     8.96
nickel     8.90
platina   21.45
silver    10.50
stal       7.80
titan      4.54
vatten     1.00

--- RESISTIVITET ---
 \rho; (\Omega;mm^{2}/m)
guld    0.0235
koppar  0.0172
silver  0.0159
"""
    },
    "MODERN": {
        "title": "MODERN",
        "content": r"""== MODERN FYSIK ==

--- RELATIVITET ---
Lorentzfaktorn:
 \gamma; = \frac{1}{\sqrt{1\minus;\frac{v^{2}}{c^{2}}}}

Tidsdilatation:
 t = \gamma;t\subs0;
 (t\subs0; = egentid)

L\auml;ngdkontraktion:
 l = \frac{l\subs0;}{\gamma;}
 (l\subs0; = egenlangd)

R\ouml;relsem\auml;ngd:
 p = \gamma;m\subs0;v
Totalenergi:
 E = \gamma;m\subs0;c^{2}
Viloenergi:
 E\subs0; = m\subs0;c^{2}
R\ouml;relseenergi:
 E\subk; = E \minus; E\subs0;

--- EM V\aring;GOR ---
Emittans: M = \frac{P}{A}

Wiens forsk.lag:
 \lambda;\submi;T = a
 a=2.898\times;10^{\minus;3} Km

Stefan-Boltzmanns:
 M = \sigma;T^{4}
 \sigma;=5.67\times;10^{\minus;8}
  W/(m^{2}K^{4})

--- RADIOAKTIVITET ---

>> ALFA-S\ouml;NDERFALL <<
En \alpha;partikel
(He-4) s\auml;nds ut.
Moderk\auml;rnans:
 masstal  \minus;4
 atomnr   \minus;2
X \rArr; Y + He-4

>> BETA-MINUS <<
Neutron \rArr; proton
 + elektron
 + antineutrino
Moderk\auml;rnans:
 masstal  of\ouml;r\auml;ndrat
 atomnr   +1

>> BETA-PLUS <<
Proton \rArr; neutron
 + positron
 + neutrino
Moderk\auml;rnans:
 masstal  of\ouml;r\auml;ndrat
 atomnr   \minus;1

>> GAMMA <<
K\auml;rna g\aring;r fr\aring;n
exciterat tillst\aring;nd
till l\auml;gre energi.
Masstal of\ouml;r\auml;ndrat.
Atomnr of\ouml;r\auml;ndrat.
Foton (\gamma;) s\auml;nds
ut med E = hf.

--- S\ouml;NDERFALLSLAG ---
S\ouml;nderfallskonstant:
 \lambda; = \frac{ln2}{T\submi;}

S\ouml;nderfallslagen:
 N = N\subs0;(\frac{1}{2})^{\frac{t}{T\submi;}}
 N = N\subs0;e^{\minus;\lambda;t}

Aktivitet:
 A = \lambda;N
Aktivitetslagen:
 A = A\subs0;(\frac{1}{2})^{\frac{t}{T\submi;}}
 A = A\subs0;e^{\minus;\lambda;t}

--- ABSORPTION ---
Absorptionskoeff:
 \mu; = \frac{ln2}{d\submi;}
Absorption:
 I = I\subs0;(\frac{1}{2})^{\frac{x}{d\submi;}}
 I = I\subs0;e^{\minus;\mu;x}

Energi fran massdef:
 E = \Delta;mc^{2}
 1 u = 931.5 MeV

--- ATOM & KVANT ---
Fotonenergi:
 E = hf
 E = \frac{hc}{\lambda;}

Fotoelektrisk eff:
 hf = W\subu; + E\subk;
 W\subu; = uttr\auml;desarbete
 E\subk; = max kin. energi
 tr\ouml;skelfrekv:
  f\subs0; = \frac{W\subu;}{h}

Energiniv\aring;er v\auml;te:
 E\subn; = \frac{\minus;13.6 eV}{n^{2}}
 (n = 1,2,3,...)

Foton vid \ouml;verg\aring;ng:
 E = |E\subn;\subs1; \minus; E\subn;\subs2;|
 \lambda; = \frac{hc}{E}
Snabbformel:
 \lambda;(nm) = \frac{1240}{E(eV)}

Fotonens r\ouml;relsem.:
 p = \frac{E}{c} = \frac{h}{\lambda;}

de Broglie-v\aring;gl.:
 \lambda; = \frac{h}{p}
Elektron acc. U volt:
 E\subk; = eU
 p = \sqrt{2mE\subk;}
 \lambda; = \frac{h}{p}

R\ouml;ntgenr\ouml;r:
 \lambda;\submi; = \frac{hc}{eU}
 f\submi; = \frac{eU}{h}

--- ASTROFYSIK ---
Flykthastighet:
 v = \sqrt{\frac{2Gm}{R}}

Schwarzschildradie:
 r\submi; = \frac{2Gm}{c^{2}}

R\ouml;df\ouml;rskjutning:
 z = \frac{\lambda;\minus;\lambda;\subs0;}{\lambda;\subs0;}
 z \approx; \frac{v}{c}

Hubbles lag:
 v = H\subs0;d
 H\subs0;=70 km/s/Mpc

--- UTTR\Auml;DESARBETE ---
 W\subu; (eV)
aluminium  2.81
bly        4.25
cesium     1.94
kadmium    4.00
kalcium    3.20
kalium     2.24
natrium    2.46
silver     4.61
titan      4.33
volfram    4.50
"""
    },
    "KONST": {
        "title": "KONST",
        "content": r"""== KONSTANTER ==

Ljusets hast. c
 299 792 458 m/s
 (3.00\times;10^{8} m/s)

Ljudets hast.
 340 m/s

Elektronladn. e
 1.602\times;10^{\minus;19} C

Elektronmassa m\sube;
 9.109\times;10^{\minus;31} kg

Jordens radie
 6371 km

Jordens massa
 5.974\times;10^{24} kg

Permeabilitet \mu;
 4\pi;\times;10^{\minus;7} Vs/Am

Gravitationskonst G
 6.674\times;10^{\minus;11} Nm^{2}/kg^{2}

Plancks konst. h
 6.626\times;10^{\minus;34} Js

Avogadros tal N\subA;
 6.022\times;10^{23} /mol

Boltzmanns k
 1.381\times;10^{\minus;23} J/K

Stefan-Boltzmann \sigma;
 5.67\times;10^{\minus;8} W/(m^{2}K^{4})

Wiens konst. a
 2.898\times;10^{\minus;3} Km

Coulombs konst. k
 8.988\times;10^{9} Nm^{2}/C^{2}

Vakuumpermitt. \epsilon;\subs0;
 8.854\times;10^{\minus;12} F/m

== OMR\Auml;KNINGSFAKT. ==

1 eV = 1.602\times;10^{\minus;19} J
1 u  = 1.661\times;10^{\minus;27} kg
1 u  = 931.494 MeV

1 kcal = 4186.8 J
1 kWh  = 3.6\times;10^{6} J
1 hk   = 735.5 W

1 bar  = 1.00\times;10^{5} Pa
1 mmHg = 133 Pa

Snabbformel foton:
 E(eV)\times;\lambda;(nm) = 1240

--- NUKLID INFO ---
Protonmassa:
 1.007276 u
Neutronmassa:
 1.008665 u
He-4 massa:
 4.002602 u
"""
    },
}


def build_eam(title: str, content: str) -> str:
    """Build .eam file content in the format EactMaker expects."""
    return f"g2e\x1e{title}\x1e\x1e{content.strip()}"


def convert_via_eactmaker(title: str, eam_content: str, output_path: Path) -> bool:
    """Submit to EactMaker's converter.php and save the resulting .g2e file."""
    url = "https://tools.planet-casio.com/EactMaker/system/converter.php"
    data = urllib.parse.urlencode({
        "titre": title,
        "format": "g2e",
        "texte": eam_content.split("\x1e", 3)[3] if "\x1e" in eam_content else eam_content,
        "additional": "",
        "font": "",
        "password": "",
    }).encode("utf-8")

    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    req.add_header("Referer", "https://tools.planet-casio.com/EactMaker/")

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = resp.read()
            if len(result) < 100:
                print(f"  WARNING: Response too small ({len(result)} bytes), likely an error page")
                return False
            output_path.write_bytes(result)
            print(f"  {output_path.name} ({len(result)} bytes)")
            return True
    except Exception as e:
        print(f"  ERROR converting {title}: {e}")
        return False


def main():
    OUT_DIR.mkdir(exist_ok=True)
    eam_dir = SCRIPT_DIR / "eam_g2e"
    eam_dir.mkdir(exist_ok=True)

    do_convert = "--convert" in sys.argv

    print("Generating EAM files with math markup:")
    for name, section in SECTIONS.items():
        eam_content = build_eam(section["title"], section["content"])
        eam_path = eam_dir / f"{name}.g2e.eam"
        eam_path.write_text(eam_content, encoding="utf-8")
        print(f"  {eam_path.name} ({len(section['content'])} chars)")

    print(f"\nEAM files saved to: {eam_dir}")

    if do_convert:
        print("\nConverting to G2E via EactMaker:")
        success = 0
        for name, section in SECTIONS.items():
            eam_content = build_eam(section["title"], section["content"])
            g2e_path = OUT_DIR / f"{name}.g2e"
            if convert_via_eactmaker(section["title"], eam_content, g2e_path):
                success += 1
        print(f"\nConverted {success}/{len(SECTIONS)} files to: {OUT_DIR}")
    else:
        print("\nTo convert to .g2e, either:")
        print("  1. Run: python generate_eam_g2e.py --convert")
        print("  2. Or manually load each .eam in https://tools.planet-casio.com/EactMaker/")
        print("     Set format to G2E, then click the download button")


if __name__ == "__main__":
    main()

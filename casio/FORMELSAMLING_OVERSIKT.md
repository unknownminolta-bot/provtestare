# Formelsamling översikt

Den här översikten beskriver hur formelsamlingen är tänkt att användas på räknaren. `generate_eam_g2e.py` är den exporterande källan för e-ACT-filerna, medan `*.txt`-filerna fungerar som läsbara referenser. KEMI är prioriterat eftersom den sektionen kräver flest metodval och har flest vanliga tentafällor.

## Övergripande arbetsmetod

1. Identifiera storheten som efterfrågas och skriv enheten innan du räknar.
2. Välj modell: konstant acceleration, energi, jämvikt, ideal gas, redox, vågoptik, kretsmodell osv.
3. Kontrollera villkoren: 25 °C, konstant substansmängd, 1:1-stökiometri, SI-enheter, reduktionspotentialer, små vinklar, ideal gas, inga förluster.
4. Räkna symboliskt så långt det går och sätt in tal sist.
5. Rimlighetskontrollera tecken, storleksordning och enhet.

## KEMI

### Mol, massa, koncentration och gas

Kärnkedjan är `m -> n -> reaktionsförhållande -> n -> m` eller `V/c` beroende på vad uppgiften ger. Vid mol/L ska volymen vara i liter. Vid `pV=nRT` med `R=8.314` ska tryck vara i Pa, volym i m³ och temperatur i kelvin. Om uppgiften anger ett annat `R` följer enheterna den konstanten.

Vanliga fällor:

- Glöm inte att molmassa gäller per mol formelenhet, inte per atom om ämnet är en förening.
- Begränsande reaktant fås genom att jämföra `n/koefficient`.
- Förbränning av kolväten ger normalt `CO2` och `H2O`; syre från luft är ofta i överskott.
- Utbyte och renhet är multiplikativa korrigeringar, inte nya reaktionskoefficienter.

### Redox och oxidationstal

Oxidationstal används först för att se vad som oxideras och reduceras. I sur lösning balanseras O med `H2O`, H med `H+` och laddning med `e-`. I basisk lösning gör man samma sak som i sur lösning och neutraliserar därefter `H+` med `OH-` på båda sidor.

Edge cases:

- Kontrollera elektronerna sist: antal avgivna och upptagna elektroner måste vara lika.
- Syre är oftast `-2`, men peroxider är undantag.
- Väte är oftast `+1`, men metallhydrider är undantag.
- Skriv inte ihop halvreaktioner innan både massa och laddning är balanserade.

### Elektrokemi

Alla tabellvärden i spänningsserien behandlas som reduktionspotentialer. Då är
`E0(cell)=E0(katod)-E0(anod)`. Högre reduktionspotential ger katod i en galvanisk cell, lägre blir anod. Spontan cell kräver `E(cell)>0` med konsekvent teckenhantering.

Metod:

- Välj katod/anod från reduktionstabellen.
- Beräkna `E0(cell)`.
- Om koncentrationer inte är standard, använd Nernst och reaktionskvoten `Q`.
- Vid elektrolys kopplas substansmängden till laddning via `F` och antal elektroner `z`.

Vanliga fällor:

- I galvanisk cell är anoden oxidation; i elektrolys är teckenkonventionen i praktiken kopplad till den påtvingade strömkällan.
- Blanda inte oxidationstabeller och reduktionstabeller.
- `n` i Nernst är antal elektroner i balanserad cellreaktion.

### Syra-bas, buffert och titrering

Stark enprotonig syra ger `[H+]=c`, men det gäller inte automatiskt för svaga syror eller flerprotoniga syror. Vid 25 °C gäller `pH+pOH=14`. Svaga syror kräver `Ka`, och buffertar hanteras effektivt med Henderson-Hasselbalch.

Metod:

- Stark syra/bas: använd stökiometri först, pH sist.
- Svag syra/bas: skriv jämviktsuttryck och använd approximation endast om den är rimlig.
- Buffert: identifiera syraformen och basformen.
- Titrering: vid ekvivalens ska substansmängder jämföras med reaktionskoefficienter, inte alltid 1:1.

Edge cases:

- `H2SO4` kan inte alltid behandlas som bara `[H+]=c`.
- Spädning ändrar koncentration, inte substansmängd.
- Vid blandning av stark syra och stark bas ska överskottet efter neutralisation avgöra pH.

### Jämvikt, fällning och termokemi

`K` beskriver jämvikt, `Q` beskriver nuläge. Om `Q<K` går reaktionen framåt; om `Q>K` går den bakåt. En ICE-tabell håller isär start, ändring och jämvikt. För gasjämvikter måste `Delta n` räknas på gasformiga ämnen.

Metod:

- Skriv balanserad reaktion först.
- Skriv `K` med produkter över reaktanter.
- För fällning jämförs `Qsp` med `Ksp`.
- För termokemi: summera reaktioner med Hess lag och följ tecknet på `dH`, `dS` och `dG`.

Vanliga fällor:

- Rent fast ämne och ren vätska ingår inte i jämviktsuttrycket.
- `Kp=Kc(RT)^Delta n` kräver konsekventa enheter.
- `dG<0` betyder spontan riktning under de givna villkoren, inte nödvändigtvis snabb reaktion.

### Kinetik

Hastighetslagen `v=k[A]^m` bestäms experimentellt. Exponenterna behöver inte vara samma som reaktionskoefficienterna. För första ordningen kan `ln([A]0/[A])=kt` och `t_halv=ln2/k` användas.

## MEKANIK

Mekaniken bör väljas efter situation:

- Konstant acceleration: använd kinematikformlerna när `a` är konstant.
- Kast: dela upp horisontellt och vertikalt; `a_h=0`, `a_v=-g` om uppåt är positivt.
- Krafter: rita friläggningsdiagram, välj axlar och summera krafter i varje riktning.
- Energi: använd när bara start/slutläge spelar roll och icke-konservativa förluster är kända eller saknas.
- Rörelsemängd: använd vid stötar, explosioner och korta kontaktförlopp.

Edge cases:

- Friktionskraften är högst `mu_s F_N` vid vila men `mu_k F_N` vid glidning.
- Vid lutande plan är komponenterna `mg sin(alpha)` längs planet och `mg cos(alpha)` normalt mot planet.
- Elastisk stöt bevarar både rörelsemängd och kinetisk energi; oelastisk stöt bevarar bara rörelsemängd.
- Arbete `W=F_s s` använder kraftkomponenten i rörelseriktningen.

## VÅGOR OCH OPTIK

Vågsektionen täcker period, frekvens, våghastighet, stående våg, Doppler, interferens, gitter och brytning.

Metod:

- Vågrörelse: börja med sambandet `v=lambda f`.
- Stående våg: kontrollera randvillkor innan du väljer harmoniskt tal.
- Gitter: beräkna ordning med `n lambda = d sin(alpha)` och kontrollera att `sin(alpha)<=1`.
- Brytning: använd Snells lag och kontrollera om totalreflektion är möjlig.
- Linser: använd linsformeln och bestäm om bilden är reell eller virtuell.

Edge cases:

- Doppler kräver teckenkonvention: rita alltid källa, observatör och rörelseriktning.
- `n_max=floor(d/lambda)` och totalt antal maxima är ofta `2n_max+1`.
- Totalreflektion kräver att ljuset går från högre till lägre brytningsindex.
- Småvinkelapproximationer ska inte användas om vinkeln är stor.

## EL OCH MAGNETISM

Elsektionen går från grundläggande kretsar till kondensatorer, magnetfält, induktion, växelström och transformatorer.

Metod:

- Kretsar: ersätt resistorer, beräkna totalström och gå tillbaka till delspänningar/effekter.
- Kondensatorer: parallellkoppling adderar kapacitanser; seriekoppling adderar inverser.
- Magnetiska krafter: använd `sin(alpha)` och högerhandsregel för riktning.
- Induktion: Lenz lag bestämmer motverkande riktning.
- Växelström: skilj toppvärden från effektivvärden.

Edge cases:

- Polspänning `U=epsilon-R_i I` gäller vid urladdning.
- Magnetiskt flöde beror på vinkeln: `phi=BA cos(theta)`.
- RC-tidskonstanten `tau=RC` anger skalan för uppladdning/urladdning, inte exakt sluttid.
- Transformatorformeln antar ideal transformator.

## TERMOFYSIK

Termofysiken blandar vätsketryck, gas, värme, fasövergångar och materialtabeller.

Metod:

- Gas: använd kelvin och kontrollera om substansmängden är konstant.
- Värme: dela upp problemet i temperaturändringar och fasbyten.
- Första huvudsatsen: var tydlig med om arbete räknas på eller av systemet.
- Densitetstabeller kan kräva enhetsbyte mellan `g/cm3` och `kg/m3`.

Edge cases:

- `rho` används både för densitet och resistivitet; sammanhanget avgör.
- Vid fasbyte ändras temperaturen inte i idealiserade problem.
- Gasarbete får tecken beroende på konvention.

## MODERN FYSIK

Modern fysik kräver ofta mer modellval än algebra. Sektionen täcker relativitet, strålning, radioaktivitet, atomfysik, fotoelektrisk effekt, de Broglie, röntgen och astrofysik.

Metod:

- Relativitet: använd `gamma` när hastigheten är jämförbar med `c`.
- Sönderfall: koppla `lambda`, halveringstid, antal kärnor och aktivitet.
- Fotoner: välj mellan `E=hf`, `E=hc/lambda` och snabbformeln `E(eV)lambda(nm)=1240`.
- Kärnreaktioner: använd massdefekt och kontrollera om atom- eller kärnmassor används.

Edge cases:

- Beta-plus med atommassor kräver ofta elektronmass-korrigering.
- Elektroninfångning har annan massbokföring än beta-plus.
- `E0=m0c2` är viloenergi; blanda inte relativistisk och klassisk kinetisk energi utan villkorskontroll.
- Röntgengränsvåglängd beror på accelerationsspänningen.

## Konstantsektionen

Konstanterna är avsedda som snabb referens. Kontrollera avrundning mot uppgiften om provet anger egna värden. Sambandet `k=1/(4*pi*epsilon0)` kopplar Coulombs konstant till vakuumpermittiviteten.

## Export och rendering

I `generate_eam_g2e.py` används Eact-koder för svenska tecken och specialtecken, till exempel `\auml;`, `\ouml;`, `\aring;`, `\Delta;` och `\minus;`. I g1e-export normaliseras subskript för att undvika råa `\sub...;`-token på fx-9860GIII. Sifferindex blir Unicode-subskript, medan bokstavsindex blir ASCII som `_max`, `_tot`, `_A`.

Viktiga renderingsregler:

- Lägg in `\times;` före `sin`, `cos` och `tan` när en variabel eller ett index står direkt före funktionen.
- Undvik nya `\sub...;`-namn med bokstäver som inte hanteras av normaliseringen utan test.
- Kör alltid `python3 test_formula_audit.py` innan EactMaker-export.
- Kör `python3 generate_eam_g2e.py --convert --formats both` först när testerna är gröna.


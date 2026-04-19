# FYXF04 Formelblad
# Kör i Python-läge på fx-9860GIII
# Navigera med siffror

def p(t):
  for l in t.split("\n"):
    print(l)
  input()

def meny():
 while True:
  print("== FORMLER ==")
  print("1 Mekanik")
  print("2 Vagor/Optik")
  print("3 El/Magnetism")
  print("4 Termofysik")
  print("5 Modern fysik")
  print("6 Konstanter")
  print("0 Avsluta")
  v=input(">")
  if v=="1": mekanik()
  elif v=="2": vagor()
  elif v=="3": elmag()
  elif v=="4": termo()
  elif v=="5": modern()
  elif v=="6": konst()
  elif v=="0": break

def mekanik():
 while True:
  print("= MEKANIK =")
  print("1 Kinematik")
  print("2 Kastrorelse")
  print("3 Central/svangn")
  print("4 Krafter")
  print("5 Energi")
  print("6 Rorelsemangd")
  print("0 Tillbaka")
  v=input(">")
  if v=="0": break
  elif v=="1": p(
"Medelhast v=ds/dt\n"
"Medelacc  a=dv/dt\n"
"Konst.hast: s=v*t\n"
"Konst.acc:\n"
" s=v0*t+a*t^2/2\n"
" v=v0+a*t\n"
" v_m=(v0+v)/2")
  elif v=="2": p(
"a_h=0 v_h=v0*cos(a)\n"
"x=v0*cos(a)*t\n"
"a_v=-g\n"
"v_v=v0*sin(a)-g*t\n"
"y=v0*sin(a)*t\n"
"  -g*t^2/2\n"
"Stighoejd:\n"
" h=v0^2*sin^2(a)/2g\n"
"Kastvidd:\n"
" s=v0^2*sin(2a)/g")
  elif v=="3": p(
"w=d0/dt  0=w*t\n"
"v=w*r\n"
"ac=v^2/r=r*w^2\n"
"  =4pi^2*r/T^2\n"
"---Svangning---\n"
"w=sqrt(k/m)\n"
"x=A*sin(w*t)\n"
"T=2pi*sqrt(m/k)\n"
"Ep=k*x^2/2\n"
"Pendel:\n"
" T=2pi*sqrt(l/g)")
  elif v=="4": p(
"F_res=m*a\n"
"F=G*m1*m2/r^2\n"
"F=k*dl (Hooke)\n"
"F=mu*FN\n"
"M=F*l\n"
"Summa M=0\n"
"Kepler: T^2/r^3=C")
  elif v=="5": p(
"W=Fs*s\n"
"dE=W\n"
"Ep=m*g*h\n"
"Ek=m*v^2/2\n"
"E=Ep+Ek\n"
"P=dE/dt=Fs*v\n"
"eta=E_n/E_t\n"
"   =P_n/P_t")
  elif v=="6": p(
"p=m*v\n"
"I=F*t\n"
"I=dp\n"
"Summa(pi)=konst")

def vagor():
 while True:
  print("= VAGOR =")
  print("1 Vagrorelse")
  print("2 Doppler")
  print("3 Interferens")
  print("4 Gitter")
  print("5 Brytning")
  print("6 Brytn.index")
  print("0 Tillbaka")
  v=input(">")
  if v=="0": break
  elif v=="1": p(
"f=1/T\n"
"w=2pi/T\n"
"v=lambda*f\n"
"Stående vag:\n"
" L=k*lambda/2")
  elif v=="2": p(
"Mekanisk:\n"
" fo=fk*(v+vo)/(v-vk)\n"
"EM-Doppler:\n"
" l/l0=sqrt((1+v/c)\n"
"          /(1-v/c))\n"
" approx 1+v/c")
  elif v=="3": p(
"Konstruktiv:\n"
" ds=k*lambda\n"
"Destruktiv:\n"
" ds=(k+1/2)*lambda")
  elif v=="4": p(
"n*lambda=d*sin(an)\n"
"d=gitterkonstant\n"
"n=ordning(0,1,2..)\n"
"Max ordning:\n"
" n_max=d/lambda\n"
" (avrunda nedat)\n"
"Tot max: 2*n_max+1")
  elif v=="5": p(
"sin(ai)/sin(ar)\n"
" =vi/vr\n"
"n1*sin(a1)\n"
" =n2*sin(a2)\n"
"n=c/cm\n"
"Totalreflektion:\n"
" sin(ak)=n2/n1")
  elif v=="6": p(
"luft     1.00\n"
"vatten   1.33\n"
"etanol   1.36\n"
"glas     1.50\n"
"diamant  2.47")

def elmag():
 while True:
  print("= EL/MAGN =")
  print("1 Grundl.")
  print("2 Kretsar")
  print("3 Falt")
  print("4 Kondensator")
  print("5 Magnetism")
  print("6 Induktion")
  print("7 Vaxelstrom")
  print("0 Tillbaka")
  v=input(">")
  if v=="0": break
  elif v=="1": p(
"F=k*Q1*Q2/r^2\n"
"I=Q/t\n"
"U=W/Q\n"
"R=U/I\n"
"U=R*I")
  elif v=="2": p(
"Kirchhoff strom:\n"
" Sum(Iin)=Sum(Iut)\n"
"Kirchhoff spann:\n"
" U=U1+...+Un\n"
"Serie: R=R1+..+Rn\n"
"Par: 1/R=1/R1+1/R2\n"
"Polsp: U=E-Ri*I\n"
"P=U*I=U^2/R=R*I^2")
  elif v=="3": p(
"E=F/q\n"
"Homogent: E=U/d\n"
"UAB=|VA-VB|")
  elif v=="4": p(
"C=Q/U\n"
"Plattkond:\n"
" C=eps*A/d\n"
"Energi:\n"
" E=QU/2=CU^2/2")
  elif v=="5": p(
"Ledare: B=uI/(2pia)\n"
"Spole:  B=NuI/r\n"
"Solen:  B=NuI/l\n"
"Kraft ladn: F=qvB\n"
"Kraft led:  F=lIB")
  elif v=="6": p(
"phi=B*A\n"
"Generator: e=lvB\n"
"Induktion:\n"
" u=-dphi/dt\n"
"Spole: u=-N*dphi/dt\n"
"L=dphi/dI\n"
"u=-L*di/dt")
  elif v=="7": p(
"u=u_max*sin(wt)\n"
"i=i_max*sin(wt)\n"
"U=u_max/sqrt(2)\n"
"I=i_max/sqrt(2)\n"
"Transformator:\n"
" N1/N2=U1/U2=I2/I1")

def termo():
 p(
"Tryck: p=F/A\n"
"Vatske: p=p0+rho*gh\n"
"Arkimedes:\n"
" F=rho_v*V*g\n"
"Ideala: pV/T=konst\n"
"---Varme---\n"
"E=c*m*dT\n"
"Smalt: E=ls*m\n"
"Angbild: E=la*m\n"
"---c (kJ/(kg*K))---\n"
"Al 0.90  Fe 0.44\n"
"Cu 0.39  Ag 0.24\n"
"H2O 4.18 W  0.14\n"
"---ls (kJ/kg)---\n"
"is 334 Fe 276\n"
"Cu 205\n"
"---la (kJ/kg)---\n"
"H2O 2260")

def modern():
 while True:
  print("= MODERN =")
  print("1 Relativitet")
  print("2 EM-vagor")
  print("3 Sonderfall")
  print("4 Radioaktiv.")
  print("5 Atom/Kvant")
  print("6 Astrofysik")
  print("7 Uttradesarb.")
  print("0 Tillbaka")
  v=input(">")
  if v=="0": break
  elif v=="1": p(
"gamma=1/sqrt(\n"
"  1-v^2/c^2)\n"
"Tidsdil: t=gamma*t0\n"
"Langdkont: l=l0/g\n"
"p=gamma*m0*v\n"
"E=gamma*m0*c^2\n"
"E0=m0*c^2\n"
"Ek=E-E0")
  elif v=="2": p(
"Emittans: M=P/A\n"
"Wien:\n"
" lmax*T=2.898E-3\n"
"Stefan-Boltzmann:\n"
" M=sigma*T^4\n"
" s=5.67E-8 W/m^2K^4")
  elif v=="3": p(
">> ALFA <<\n"
"Alphapart.(He-4)\n"
"sands ut.\n"
"Masstal:  -4\n"
"Atomnr:   -2\n"
">> BETA-MINUS <<\n"
"n->p+e+antineutr.\n"
"Masstal: oforandr.\n"
"Atomnr:  +1\n"
">> BETA-PLUS <<\n"
"p->n+positr.+neut\n"
"Masstal: oforandr.\n"
"Atomnr:  -1\n"
">> GAMMA <<\n"
"Foton sands ut.\n"
"Masstal: oforandr.\n"
"Atomnr:  oforandr.")
  elif v=="4": p(
"lambda=ln2/T_halv\n"
"N=N0*(1/2)^(t/T_halv)\n"
"N=N0*e^(-lam*t)\n"
"A=lambda*N\n"
"A=A0*(1/2)^(t/T_halv)\n"
"---Absorption---\n"
"mu=ln2/d_halv\n"
"I=I0*(1/2)^(x/d_halv)\n"
"I=I0*e^(-mu*x)\n"
"---Massdefekt---\n"
"E=dm*c^2\n"
"1u=931.5 MeV")
  elif v=="5": p(
"E=h*f=hc/lambda\n"
"Fotoelektr:\n"
" hf=Wu+Ek\n"
" f0=Wu/h\n"
"Vate: En=-13.6/n^2\n"
"Overgang: E=|E(n1)-E(n2)|\n"
"Snabbf:\n"
" E(eV)*l(nm)=1240\n"
"Foton: p=E/c=h/l\n"
"de Broglie: l=h/p\n"
"Elektr acc U volt:\n"
" Ek=eU p=sqrt(2mEk)\n"
"Rontgen:\n"
" lmin=hc/(eU)\n"
" fmax=eU/h")
  elif v=="6": p(
"Flykthast:\n"
" v=sqrt(2Gm/R)\n"
"Schwarzschild:\n"
" rS=2Gm/c^2\n"
"Rodforskj:\n"
" z=(l-l0)/l0~v/c\n"
"Hubble:\n"
" v=H0*d\n"
" H0=70 km/s/Mpc")
  elif v=="7": p(
"Wu (eV)\n"
"Al   2.81  Pb 4.25\n"
"Cs   1.94  Cd 4.00\n"
"Ca   3.20  K  2.24\n"
"Na   2.46  Ag 4.61\n"
"Ti   4.33  W  4.50")

def konst():
 p(
"c  =3.00E8 m/s\n"
"e  =1.602E-19 C\n"
"me =9.109E-31 kg\n"
"G  =6.674E-11\n"
"h  =6.626E-34 Js\n"
"NA =6.022E23 /mol\n"
"k  =1.381E-23 J/K\n"
"sig=5.67E-8\n"
"a  =2.898E-3 Km\n"
"mu =4piE-7 Vs/Am\n"
"---Omrakn.---\n"
"1eV=1.602E-19 J\n"
"1u =1.661E-27 kg\n"
"1u =931.494 MeV\n"
"E*l=1240 eV*nm\n"
"---Nuklid---\n"
"mp=1.007276 u\n"
"mn=1.008665 u\n"
"He4=4.002602 u")

meny()

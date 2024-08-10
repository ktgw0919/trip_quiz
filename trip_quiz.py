A=0
B=0
E=7
K=0
O=0
S=0
T=0
U=0

for A in range(0,10):
  for B in range(0,10):
    for K in range(0,10):
      for O in range(0,10):
        for S in range(0,10):
          for T in range(0,10):
            for U in range(0,10):
              OTSU = 1000*O + 100*T + 10*S + U
              KOBE = 1000*K + 100*O + 10*B + E
              OSAKA = 10000*O + 1000*S + 100*A + 10*K + A
              if OTSU + KOBE == OSAKA:
                if A != B and A != E and A != K and A != O and A != S and A != T and A != U and B != E and B != K and B != O and B != S and B != T and B != U and E != K and E != O and E != S and E != T and E != U and K != O and K != S and K != T and K != U and O != S and O != T and O != U and S != T and S != U and T != U:
                  print("A = ", A)
                  print("B = ", B)
                  print("E = ", E)
                  print("K = ", K)
                  print("O = ", O)
                  print("S = ", S)
                  print("T = ", T)
                  print("U = ", U)
                  print("OTSU = ", OTSU)
                  print("KOBE = ", KOBE)
                  print("OSAKA = ", OSAKA)
                  break

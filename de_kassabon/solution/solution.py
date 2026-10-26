# Lees de twee bedragen in
bedrag_21 = float(input())
bedrag_6 = float(input())

# Bereken de bedragen inclusief btw
incl_21 = bedrag_21 * 1.21
incl_6 = bedrag_6 * 1.06

# Bereken het totaal en rond af op 2 decimalen
totaal = round(incl_21 + incl_6, 2)

# Print de exacte antwoordzin
print("Het totale bedrag inclusief btw is", totaal, "euro.")

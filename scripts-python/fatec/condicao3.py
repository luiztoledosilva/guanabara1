KWh=float(input("Qual a quantidade kwhs gastas na conta de luz? "))
tipo=str(input("""Qual o tipo de residência R p/ residencial,
                 C/ p comercial, I p industria:  """  ))
if tipo=='R' or tipo=='r' and KWh<=500:
    print("O preço a ser pago eh: {:.2f} ".format(KWh*0.40))
elif tipo=='R' or tipo=='r' and KWh>500:
    print("O preço a ser pago eh: {:.2f} ".format(KWh*0.65))

elif tipo=='C' or tipo=='c' and KWh<=1000:
    print("O preço a ser pago eh: {:.2f} ".format(KWh*0.55))
elif tipo=='C' or tipo=='c' and KWh>1000:
    print("O preço a ser pago eh: {:.2f} ".format(KWh*0.60))
elif tipo=='I' or tipo=='i' and KWh<=5000:
    print("O preço a ser pago eh: {:.2f} ".format(KWh*0.55))
elif tipo=='I' or tipo=='i' and KWh>5000:
    print("O preço a ser pago eh: {:.2f} ".format(KWh*0.60))
else:
    print("Dados errados")
    




                
               
               

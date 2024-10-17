A=int(input("masukkan populasi awal serangga A: "))
B=int(input("masukkan populasi awal serangga B: "))
hari=int(input("masukkan jumlah hari: "))
for i in range(1,hari+1):
    if i%5==0:
        print(f"hari {i}: predator memakan 10% populasi.")
        if i%2!=0:
            A*=0.9*1.3
            B*=0.9*1.5
        elif i%2==0:
            A*=0.9*0.8
            B*=0.9*0.6

    elif i%2==0:
        A*=0.8
        B*=0.6
    else :
        A*=1.3
        B*=1.5
    print(f"hari {i}: serangga A = {int(A)}, serangga B ={int(B)}")
    
        
    
       
  
  




         

    


    
            
       

  




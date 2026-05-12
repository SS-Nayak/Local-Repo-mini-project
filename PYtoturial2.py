#____FOR LOOP TO MAKE MULTIPLICATION TABLE-(Python & JavaScript)_____#

#---------PYTHON CODE--------#
#CODE 1
x=5
for i in range (1,11): # Here 'i' is a varible, 1 is starting point and 11 is ending point.
  print(x + "x" + i + "=" + int(x*i))

#CODE 2
x=input("enter any number: ")

for i in range (1, 11):
    print(x, "x", i, "=", int(x)*i)

#-------- JAVA SCRIPT CODE------#
# CODE 1
'''<body>
    <script>

      let n=5;
      for(let i =1; i<10; ++i) {   
          console.log(n,"*",i,"=",n*i); <!--here we can also use '+' sign, rather than comma ','-->
      }
    </script>
  </body>'''
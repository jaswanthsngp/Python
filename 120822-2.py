st_name=["Shaun", "Linh", "Ahmed"]
st_id=[160801, 160802, 160803]
st_age=[18,20,19]
st_sub=["Communication Study", "Accounting", "Psychology Study"]

print(st_name)
print(st_id)
print(st_age)
print(st_sub)
print(" ")

st_data=[ ["Shaun", 160801, 18, "Communication Study"],
          ["Linh", 160802, 20, "Accounting"],
          ["Ahmed", 160803, 19, "Psychology Study"] ]

for i in range(0,3):
    for j in range(0,4): print(st_data[i][j])
    print(" ")
    

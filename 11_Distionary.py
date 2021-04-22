  #dict is nothing but key value pairs 
#   d1 = {}
d2 = {"david":"piza", "joyi":"romance", "shu":{"eating":"piza", "clouth":"top"}}
print(d2["shu"]["eating"])
d2["anu"] = "Junk Food"
d2[432] = "chicken"
print(d2)

d3 = d2.copy()
del d3["david"]
print(d3)

print(d3.get("shu"))
print(d2.keys())


# Dict function python 
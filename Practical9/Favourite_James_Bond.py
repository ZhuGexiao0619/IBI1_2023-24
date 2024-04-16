def favourite_bond(year_of_birth):
    bond_actors = {1973: "Roger Moore",1987: "Timothy Dalton",1995: "Pierce Brosnan", 2006: "Daniel Craig"}
    eighteen_year_old = year_of_birth + 18
    favourite_actor = bond_actors.get(eighteen_year_old, "Unknown")  # 如果出生年份不在时间线中，返回"Unknown"
    return favourite_actor
print(favourite_bond(1997))
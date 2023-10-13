v_type = input()
v_var = input()
if v_type == "int":
    number = int(v_var)
    number *= 2
    print(number)
elif v_type == "real":
    number = float(v_var)
    number *= 1.5
    print(f"{number:.2f}")
elif v_type == "string":
    v_var = '$' + v_var + '$'
    print(v_var)

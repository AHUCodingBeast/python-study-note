age = int(input("请输入年龄："))
if age < 10:
    print("eligible")
elif age < 18:
    print("eligible but need parental guidance")
else:
    print("not eligible")


# python 中的SwitchCase
def status_convertor(status):
    match status:
        case "404":
            return "not found"
        case "500"|"502":
            return "internal error"
        # 这里相当于是Java中的default
        case _:
            return "unknown"

print(status_convertor("404"))
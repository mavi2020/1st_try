def decorate(fn):
    def show(s):
        out = "--"
        out += fn(s)
        out += "--"
        return out

    return show


def display(txt):
    return txt + " welcome"


print(display("new world!"))

display = decorate(display)
print(display("shima"))
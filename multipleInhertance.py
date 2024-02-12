class father:
    a=123
    def fdisplay(self):
        print("father display")

class mother:
    def fdisplay(self):
        print("mother display")
# important if father is first then call father display only. It depends on order
class child(mother,father):
    def cdisplay(self):
        print("c display")

obj = child()
obj.fdisplay()
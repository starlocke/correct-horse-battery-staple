import sys
import re

class Program:
    def usage(self):
        print("Two version strings are required, like so:")
        print("    > python ver_cmp.py \"1.1\" \"1.2\"")
        print("    > python ver_cmp.py \"v1.3\" \"v1.3\"")
        print("    > python ver_cmp.py \"3.14\" \"3.1\"")
        print("    > python ver_cmp.py \"v2.0\" \"v20.0\"")
        print("    > python ver_cmp.py \"v1.0\" \"v1.0.0\"")
        print("    > python ver_cmp.py \"v2.0-rc\" \"v2.0-alpha\"")
        print("    > python ver_cmp.py \"v2-alpha\" \"v2.0-alpha\"")
        exit(1)

    def get_ver(self, arg: str):
        parts = [part for part in re.split('[.]', arg)]
        return parts

    def compare_versions(self, a: list, b: list):
        for i in range(min(len(a), len(b))):
            _a = a[i]
            _b = b[i]
            if _a.isdecimal() and _b.isdecimal():
                _a = int(_a)
                _b = int(_b)
            if _a == _b:
                continue
            elif a < b:
                return -1
            else:
                return 1
        if len(a) < len(b):
            return -1
        elif len(a) > len(b):
            return 1
        else:
            return 0

    def main(self):
        if len(sys.argv) != 3:
            self.usage()
        ver_1 = self.get_ver(sys.argv[1])
        ver_2 = self.get_ver(sys.argv[2])
        result = self.compare_versions(ver_1, ver_2)
        if result == -1:
            print(f"\"{sys.argv[1]}\" is less than \"{sys.argv[2]}\"")
        elif result == 0:
            print(f"\"{sys.argv[1]}\" is equal to \"{sys.argv[2]}\"")
        else:
            print(f"\"{sys.argv[1]}\" is greater than \"{sys.argv[2]}\"")

if __name__ == '__main__':
    p = Program()
    p.main()

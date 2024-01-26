import sys
import os

class Program:
    def debug(self, *args):
        if os.getenv('DEBUG', '0') == '1':
            print(*args)

    def usage(self):
        print("Two lines on the x-axis are needed as input arguments, like so:")
        print("    > python is_overlap.py \"(1,4)\" \"(2,3)\"")
        print("    > python is_overlap.py \"(1.0,2.0)\" \"(1.0,2.0)\"")
        print("    > python is_overlap.py \"-2,-1\" \"1,2\"")
        print("    > python is_overlap.py \"(-1.5,0)\" \"(0,1.5)\"")
        print("note 1: the \" quote marks are commonly helpful so that command line shells pass the values correctly, they are not actually a part of the input values.")
        print("note 2: the lines are always fully exclusive ranges. the () brackets are optional.")
        exit(1)

    def get_line(self, arg: str):
        args = [float(v) for v in arg.strip('()').split(',')]
        if len(args) != 2:
            raise ValueError(f"Invalid input value: {arg}. Must be given as '(xa,xb)', pair of values on the x-axis.")
        if args[0] == args[1]:
            raise ValueError(f"Invalid input value. Lines must be fully exclusive ranges. {arg} is null and void, not even a point.")
        args.sort()
        return tuple(args)
    
    def is_pt_in_bounds(self, pt, bounds):
        is_in_bounds = pt > bounds[0] and pt < bounds[1]
        if is_in_bounds:
            print(f"{pt} is within {bounds}")
        else:
            print(f"{pt} is not within {bounds}")
        return is_in_bounds

    def is_overlap(self, line_1, line_2):
        self.debug("is_overlap", line_1, line_2)
        return (
            line_1 == line_2
            or self.is_pt_in_bounds(line_1[0], line_2)
            or self.is_pt_in_bounds(line_1[1], line_2)
            or self.is_pt_in_bounds(line_2[0], line_1)
            or self.is_pt_in_bounds(line_2[1], line_1)
        )

    def main(self):
        if len(sys.argv) != 3:
            self.usage()
        line_1 = self.get_line(sys.argv[1])
        line_2 = self.get_line(sys.argv[2])

        if self.is_overlap(line_1, line_2):
            print(f"These lines are overlapping: {line_1} and {line_2}")
        else:
            print(f"These lines are not overlapping: {line_1}, {line_2}")

if __name__ == '__main__':
    p = Program()
    p.main()

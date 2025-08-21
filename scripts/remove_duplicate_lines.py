import io
import argparse

parser = argparse.ArgumentParser(
    prog="ProgramName",
    description="What the program does",
    epilog="Text at the bottom of help",
)

parser.add_argument("-i", "--input")
parser.add_argument("-o", "--output")
parser.add_argument("-s", "--dont-sort", action=argparse.BooleanOptionalAction)

args = parser.parse_args()

with io.open(args.input, "r", encoding="utf8") as f:
    lines = f.read().splitlines()

line_set = list(set(lines))
line_set = [l for l in line_set if l != ""]

if "sort" not in args.__dict__.keys() is not False:
    line_set = list(sorted(line_set))


if args.output is None:
    output = args.input
else:
    output = args.output


with io.open(output, "w+", encoding="utf8") as f:
    f.write("\n".join(line_set))
print("Wrote {} lines from {} in {}".format(len(line_set), len(lines), output))

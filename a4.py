import fileinput
import re
from itertools import groupby


def main(inp):
    print("task1", task1(get_passports(inp)))
    print("task2", task2(get_passports(inp)))


def get_passports(inp):
    for k, lines in groupby(inp, key=lambda x: x == ""):
        if k:
            continue
        ol = " ".join(lines)
        yield dict(kv.split(":") for kv in ol.split(" "))


def task1(passports):
    req_field = set(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))
    valid_count = 0
    for p in passports:
        if not (set(req_field) - set(p)):
            valid_count += 1
    return valid_count


def task2(passports):
    req_field = set(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))
    valid_count = 0
    for p in passports:
        if req_field - set(p):
            continue
        try:
            if not (1920 <= int(p["byr"]) <= 2002):
                continue
            if not (2010 <= int(p["iyr"]) <= 2020):
                continue
            if not (2020 <= int(p["eyr"]) <= 2030):
                continue
            if not (p["hgt"].endswith("cm") or p["hgt"].endswith("in")):
                continue
            if p["hgt"][-2:] == "cm" and not (150 <= int(p["hgt"][:-2]) <= 193):
                continue
            if p["hgt"][-2:] == "in" and not (59 <= int(p["hgt"][:-2]) <= 76):
                continue
            if not re.match(r"^#[0-9a-f]{6}$", p["hcl"]):
                continue
            if p["ecl"] not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
                continue
            if len(p["pid"]) != 9 or not p["pid"].isnumeric():
                continue
        except (TypeError, ValueError):
            continue
        valid_count += 1
    return valid_count


if __name__ == "__main__":
    main([r.strip() for r in fileinput.input()])

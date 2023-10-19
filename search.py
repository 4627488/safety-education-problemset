import json
from fuzzywuzzy import fuzz


def string_similar(s1, s2):
    return fuzz.partial_ratio(s1, s2)


if __name__ == "__main__":
    problem = []
    with open("problem.json", "r", encoding="utf-8") as fcc_file:
        problem = json.load(fcc_file)
        print(len(problem))

    while True:
        maxMatchedProblem = {}
        maxMatchedProblemDiff = 0
        str1 = input()
        for p in problem:
            new_diff = string_similar(str1, p["question"])
            if maxMatchedProblemDiff < new_diff:
                maxMatchedProblemDiff = new_diff
                maxMatchedProblem = p
        print(maxMatchedProblem["question"])
        print(f'{maxMatchedProblem["correct"]}\n{maxMatchedProblem["analyse"]}')
        print(f"diff: {maxMatchedProblemDiff}")

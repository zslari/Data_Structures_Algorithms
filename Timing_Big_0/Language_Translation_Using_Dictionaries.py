"""
Timing and Big O
Created By: Zafir Lari
Application: Language Translation Using Dictionaries

Description: This application takes in user input in Latin
and returns an english translation if available. Requires
'latin.txt' file to be imported to the same folder as this
program.
"""

from timeit import Timer


def translation():
    """ Given the 'latin.txt' file is present, import and process latin
    words into a dictionary with latin word keys and translated
    english values
    """
    translation_dict = {}
    with open("latin.txt") as file:
        for line in file:
            try:
                (key, val) = line.split(",")
            except ValueError:
                pass
            translation_dict[key] = val
            translation_dict[key] = val.rstrip()
    return translation_dict


def run(userquestion: str):
    """ Given input of latin words translates to english or
    informs user that no english translation is available for
    that word
    """
    my_dict = translation()
    no_match = " No English Translation for this word"
    lookup = userquestion.split()
    ret_str = str()
    for i in lookup:
        if i not in my_dict.keys():
            ret_str += (no_match + f" ({i})")
            continue
        if my_dict[i] == "":
            ret_str += (no_match + f" ({i})")
        else:
            ret_str += my_dict[i]
    return f"English Translation: {ret_str}"


def enter_latin():
    """ Allows user to enter a latin phrase and see translated
    output
    """
    desired_words = input("Enter a latin phrase: ")
    print(run(desired_words))


def test_cases():
    """ Assortment of Test Cases """
    run("differo")
    run("maculosos meror madide magister maiestas iustus iuvo jaculum"
        "labefacio labes labis labor lapsus")
    run("abbatis vultus absorbeo volturius inquit")
    run("This is not latin words")
    run("absque defleo burger pancake iuvo")


def test_run():
    """ Timing of Test Cases"""
    timedict = Timer("test_cases()", "from __main__ import test_cases,"
                                     " translation, run")
    dict_sect = timedict.timeit(1)
    times = timedict.repeat(5, 1)
    print(f"{dict_sect} seconds was the time it took to run 1 test of 5"
          f" translations")
    print(f"{times} was the timings for 5 test runs of 5 translations")
    print("Our program runs in O(1) time")


if __name__ == "__main__":
    test_run()
    enter_latin()


"""
TEST RUN OUTPUTS:

#1

0.008650442 seconds was the time it took to run 1 test of 5 translations
[0.010770481999999998, 0.011066222, 0.009310216000000003, 0.008808763999999997, 0.008595987999999992] was the timings for 5 test runs of 5 translations
Our program runs in O(1) time
Enter a latin phrase: oblivio occurro omnipotens opera opes
English Translation:  forgetfulness fall all work means

Process finished with exit code 0

#2

0.010497484000000001 seconds was the time it took to run 1 test of 5 translations
[0.010885035000000005, 0.010149779999999997, 0.009977730999999997, 0.008901908000000007, 0.008895759999999989] was the timings for 5 test runs of 5 translations
Our program runs in O(n) time
Enter a latin phrase: lamia largior officium olim
English Translation:  witch lavish duty once

Process finished with exit code 0

#3

0.01120876 seconds was the time it took to run 1 test of 5 translations
[0.010614212000000001, 0.010589203999999998, 0.009687468999999997, 0.009750660999999994, 0.008825699999999992] was the timings for 5 test runs of 5 translations
Our program runs in O(1) time
Enter a latin phrase: abcdefghijklmnop
English Translation:  No English Translation for this word (abcdefghijklmnop)

Process finished with exit code 0

#4

0.010123276000000002 seconds was the time it took to run 1 test of 5 translations
[0.010849479999999998, 0.010422352999999995, 0.009596627000000003, 0.008891296000000007, 0.009011707000000008] was the timings for 5 test runs of 5 translations
Our program runs in O(1) time
Enter a latin phrase: novem novus nos nullus absque
English Translation:  nine new us not No English Translation for this word (absque)

Process finished with exit code 0

#5

0.010859522000000002 seconds was the time it took to run 1 test of 5 translations
[0.010399163999999999, 0.011311496999999997, 0.010112298999999998, 0.009287716999999994, 0.008676435999999996] was the timings for 5 test runs of 5 translations
Our program runs in O(1) time
Enter a latin phrase: salutor sanctimonialis abbas dare dedi
English Translation:  visitor nun father give give

Process finished with exit code 0

"""

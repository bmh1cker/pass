#!/usr/bin/env python3
#
#  [Program]
#
#  PASS - Common User Passwords Profiler
#
#  [Author]
#
#  BM Hacker, https://github.com/bmh1cker
#
#  See 'LICENSE' for more information.

import os
import unittest
from unittest.mock import patch

from pass import *


class TestPass(unittest.TestCase):
    def setUp(self):

        read_config("pass.cfg")

    def test_config(self):

        self.assertIn("2018", CONFIG["global"]["years"], "2018 is in years")

    def test_generate_wordlist_from_profile(self):
        profile = {
            "name": "владимир",
            "surname": "путин",
            "nick": "putin",
            "birthdate": "07101952",
            "wife": "людмила",
            "wifen": "ljudmila",
            "wifeb": "06011958",
            "kid": "екатерина",
            "kidn": "katerina",
            "kidb": "31081986",
            "pet": "werny",
            "company": "russian federation",
            "words": ["Крим"],
            "spechars1": "y",
            "randnum": "y",
            "leetmode": "y",
            "spechars": [],
        }
        read_config("pass.cfg")
        generate_wordlist_from_profile(profile)

    def test_parser(self):
        """ downloads a file and checks if it exists """

        download_wordlist_http("16")

        filename = "dictionaries/hindi/hindu-names.gz"
        self.assertTrue(os.path.isfile(filename), "file " + filename + "exists")

    def test_print_cow(self):
        """ test the cow """
        print_cow()

    def test_alectodb_download(self):

        alectodb_download()

        self.assertTrue(
            os.path.isfile("alectodb-usernames.txt"),
            "file alectodb-usernames.txt exists",
        )
        self.assertTrue(
            os.path.isfile("alectodb-passwords.txt"),
            "file alectodb-passwords.txt exists",
        )

    def test_improve_dictionary(self):

        filename = "improveme.txt"
        open(filename, "a").write("password123\n2018password\npassword\n")

        __builtins__.input = lambda _: "Y"  # Mock
        improve_dictionary(filename)

    def test_download_wordlist(self):
        """ Download wordlists via menu """
        __builtins__.input = lambda _: "31"  # Mock
        download_wordlist()
        filename = "dictionaries/russian/russian.lst.gz"
        self.assertTrue(os.path.isfile(filename), "file " + filename + "exists")

    def test_interactive(self):
        """ Tests the interactive menu """

        expected_filename = "julian.txt"
        string_to_test = "Julian30771"

        # delete the file if it already exists
        if os.path.isfile(expected_filename):
            os.remove(expected_filename)

        user_input = [
            "Julian",  # First Name
            "Assange",  # Surname
            "Mendax",  # Nickname
            "03071971",  # Birthdate
            "",  # Partner
            "",  # Partner nick
            "",  # Partner birthdate
            "",  # Child name
            "",  # Child nick
            "",  # Child birthdate
            "",  # Pet's name
            "",  # Company name
            "N",  # keywords
            "Y",  # Special chars
            "N",  # Random
            "N",  # Leet mode
        ]

        test_ok = False

        with patch("builtins.input", side_effect=user_input):
            stacks = interactive()

        if os.path.isfile(expected_filename):
            if string_to_test in open(expected_filename).read():
                test_ok = True

        self.assertTrue(test_ok, "interactive generation works")

    def test_main(self):
        """ test run for the main function """
        main()


if __name__ == "__main__":
    unittest.main()

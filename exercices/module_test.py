import sys
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import mymodule


class TestURLPrint(TestCase):
    def test_url_gets_to_stdout(self):
        protocol = 'http'
        host = 'www'
        domain = 'example.com'
        sub = 'v1'
        expected_url = '{}://{}.{}\n'.format(protocol, host, domain)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            mymodule.urlprint(protocol, host, domain)
            self.assertEqual(fake_out.getvalue(), expected_url)

    def test_newurl(self):
        pr = "ftp"
        hs = "www"
        dm = "example.com"
        sub = 'v1'
        expected_url = f'{pr}://{hs}.{dm}/{sub}\n'

        with patch('sys.stdout', new=StringIO()) as new_f:
            mymodule.newUrl(pr, hs, dm, sub)
            self.assertEqual(new_f.getvalue(), expected_url)

    def test_new_link(self):
        hs = "www"
        dm = "domaine.com"
        sub = "v1"
        expected_url = f"{hs}.{dm}/{sub}\n"

        with patch("sys.stdout", new=StringIO()) as new_f:
            mymodule.new_link(hs, dm, sub)
            self.assertEqual(new_f.getvalue(), expected_url)

    def test_pass_word(self):
        name = {"first": "John", "second": "Jason", "third": "Jules", "fourth": "Jude"}
        expected_url = "first : John\nsecond : Jason\nthird : Jules\nfourth : Jude\n"

        with patch("sys.stdout", new=StringIO()) as new_f:
            mymodule.pass_wrd(**name)
            self.assertEqual(new_f.getvalue(), expected_url)

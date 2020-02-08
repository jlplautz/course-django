from django.test import TestCase

# instanciar um testcase do Django na variavel _test_case
# _test_case => protegido para ninguem utilizar
_test_case = TestCase()

# criar uma função assert_contains que vai receber o metodo assertContains
assert_contains = _test_case.assertContains

import decimal
import unittest

class Column:
    """Representa uma coluna de um DataTable

            Essa classe contem as informações de uma coluna e deve validar um dado
            de acordo com o tipo de dado confiurado no construtor.

            Attributes:
                name: Nome da coluna
                kind: tipo de dadp(varchar,bigint, numeric)
                description: Descrição da coluna
    """

    def __init__(self, name, kind, description=""):
        """Construtor
            Args:
                name: Nome da coluna
                kind: tipo de dadp(varchar,bigint, numeric)
                description: Descrição da coluna
            """
        self._name = name
        self._kind = kind
        self._description = description
        self._is_pk = False

    def __str__(self):
        _str = "Col: {} : {} {}".format(self._name, self._kind, self._description)
        return _str


    @staticmethod
    def validate(kind, data):
        if kind == 'bigint':
            if isinstance(data, int):
                return True
            return False
        elif kind =='varchar':
            if isinstance(data, str):
                return True
            return False
        elif kind =='numeric':
            try:
                val = decimal.Decimal(data)
            except:
                return False
            return True


class ColumnTest(unittest.TestCase):
    def test_validate_bigint(self):
        self.assertTrue(Column.validate('bigint', 100))
        self.assertTrue(not Column.validate('bigint', 10.1))
        self.assertTrue(not Column.validate('bigint', 'Texto'))

    def test_validate_numeric(self):
        self.assertTrue(Column.validate('numeric', 10.1))
        self.assertTrue(Column.validate('numeric', 100))
        self.assertTrue(not Column.validate('numeric', 'Texto'))

    def test_validate_varchar(self):
        self.assertTrue(Column.validate('varchar', 'Texto'))
        self.assertTrue(not Column.validate('varchar', 100))
        self.assertTrue(not Column.validate('varchar', 10.1))

if __name__ == "__main__":
    unittest.main()
from decimal import Decimal

class Relationship:
    """ Classe que representa um relacionamento entre DAtaTables

    Essa classe tem todas as informações que identificam um relacionamento entre tabelas.
    Em qual coluna ele existe, de onde vem e pra onde vai.
    """
    def __init__(self, name, _from, to, on):
        """Construtor
        Args:
            :param name: Nome
            :param _from: Tabela de onde sai
            :param to: Tabela pra onde vai
            :param on: instancia de coluna existente
        """
        self._name = name
        self._from = _from
        self._to = to
        self._on = on

class DataTable:
    """ Representa uma Tabela de Dados.

        Essa Classe representa uma tabela de dados do portal da Trnaspraência.
        Deve ser capaz de validar linhas inseridas de acordo com as colunas
        que possui. As linhas inseridas ficam registadas dentro dela.

        Attributes:
            name: Nome da tabela
            columns: [Lista de Colunas]
            data: [lista de dados]
    """

    def __init__(self, name):
        """Construtor

            Args:
                name: nome da Tabela
        """
        self._name = name
        self._columns = []
        self._references = []
        self._referenced = []
        self._data = []

    def _get_name(self):
        print("Getter Executado")
        return self._name

    def _set_name(self, _name):
        print("Setter Executado")
        self._name = _name

    def _del_name(self):
        print("Deletter Executado!")
        raise AttributeError("Não pode deleter esse atributo")

    name = property(_get_name, _set_name, _del_name)

    def add_column(self, name, kind, description=""):
        column = Column(name, kind, description=description)
        self._columns.append(column)
        return column

    def add_references(self, name, to, on):
        """ Cria uma referênai dessa tabela para outra tabela

        Args:
            :param name: nome da relação
            :param to: instancia da tabela apontada
            :param on: instancia coluna em que existe a relação
        """
        relationship = Relationship(name, self, to, on)
        self._references.append(relationship)

    def add_referenced(self, name, by, on):
        """Cria uma referencia para outra tabela que aponta para essa.

        Args:
            :param name: nome da relação
            :param by: instancia da tabela que aaponta para essa
            :param on: instancia colua em que existe a relação
        """

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

    def _validate(cls, kind, data):
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
                val = Decimal(data)
            except:
                return False
            return True
    validate = classmethod(_validate)



class PrimaryKey(Column):
    def __init__(self, table, name, kind, description=""):
        super().__init__(name, kind, description=description)
        self._is_pk = True

    def __str__(self):
        _str = "Col: {} : {} {}".format(self._name, self._kind, self._description)
        return "{} - {}".format('PK', _str)

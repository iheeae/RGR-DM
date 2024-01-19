class CayleyTable:
    def __init__(self, table):
        self.table = table
        self.size = len(table)

    def is_associative(self):
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    if self.table[self.table[i][j]][k] != self.table[i][self.table[j][k]]:
                        return False
        return True

    def is_commutative(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.table[i][j] != self.table[j][i]:
                    return False
        return True

    def is_distributive(self):
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    if self.table[i][self.table[j][k]] != self.table[self.table[i][j]][self.table[i][k]]:
                        return False
        return True

    def has_identity_element(self):
        for i in range(self.size):
            has_identity = all(self.table[i][j] == j and self.table[j][i] == j for j in range(self.size))
            if has_identity:
                return True
        return False

    def has_inverse_elements(self):
        for i in range(self.size):
            has_inverse = all(self.table[i][j] == j and self.table[j][i] == j for j in range(self.size))
            if not has_inverse:
                return False
        return True

    def has_scalar_addition(self):
        return all(self.table[i][0] == i and self.table[0][i] == i for i in range(self.size))

    def has_identity_matrix_multiplication(self):
        return all(self.table[i][i] == i for i in range(self.size))

    def has_transposition(self):
        return all(self.table[i][j] == self.table[j][i] for i in range(self.size) for j in range(self.size))

    def find_normal_subgroups(self):
        subgroups = []
        for i in range(1, self.size):
            subgroup = [0]
            for j in range(1, self.size):
                if all(self.table[j][k] in subgroup for k in range(self.size)):
                    subgroup.append(j)
            subgroups.append(subgroup)
        return subgroups


table_data = [[0, 1, 2], [1, 2, 0], [2, 0, 1]]
cayley_table = CayleyTable(table_data)

print("Работа выполнена Хваевский Ильей Игоревичем 338934\n",
        "Версия языка Python 3.12.1\n")

print("Данные таблицы:\n", table_data)

print("Task 1: по таблице Кели выяснить свойства операции\n",
        "       ассоциативность, коммутативность, дистрибутивность,\n",
        "       существование нейтрального элемента, существование обратного элемента,\n",
        "       сложение скаляра, умножение на единичную матрицу, транспонирование)")
print("Ассоциативность:", cayley_table.is_associative())
print("Коммутативность:", cayley_table.is_commutative())
print("Дистрибутивность:", cayley_table.is_distributive())
print("Существование нейтрального элемента:", cayley_table.has_identity_element())
print("Существование обратного элемента:", cayley_table.has_inverse_elements())
print("сложение скаляра:", cayley_table.has_scalar_addition())
print("Множение на единичную матрицу:", cayley_table.has_identity_matrix_multiplication())
print("Транспонирование:", cayley_table.has_transposition(), "\n")

print("\nTask 2: по таблице Кели найти нормальные подгруппы")
print("Нормальные подгруппы:", cayley_table.find_normal_subgroups())

class Table:
    def __init__(self, table_width=8):
        self.table_width = table_width
        self.queens = [-1] * table_width
        self.count = 0

    def add_queen(self, queen_amount: int = 0):
        if queen_amount == self.table_width:
            self.count += 1
            return print(f"\n{self.count}:\n",
                         "\n".join([col * "+\t" + "Q\t" + (self.table_width - col) * "+\t" for col in self.queens]))

        for queen_candidate in range(self.table_width):
            self.queens[queen_amount] = queen_candidate
            if self.is_valid(queen_amount):
                self.add_queen(queen_amount + 1)

    def is_valid(self, queen_amount: int):
        if len(set(self.queens[:queen_amount + 1])) != len(self.queens[:queen_amount + 1]):
            return False  # 列表查重

        for i in range(queen_amount):
            if abs(self.queens[i] - self.queens[queen_amount]) == int(queen_amount - i):
                return False  # 检查现有皇后中是否存在一个皇后，满足与 最后一个皇后 之间的斜率为±1

        return True


table = Table(table_width=8)
table.add_queen(queen_amount=0)

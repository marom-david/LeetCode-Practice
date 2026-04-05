class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        reservedSeats.sort()
        res = 0
        rowReserved = {}

        for row, col in reservedSeats:
            if row not in rowReserved:
                rowReserved[row] = set()
            rowReserved[row].add(col)
        

        for row in rowReserved:
            left_filled = False
            right_filled = False
            if 2 not in rowReserved[row] and 3 not in rowReserved[row] and 4 not in rowReserved[row] and 5 not in rowReserved[row]:
                res += 1
                left_filled = True
            if 6 not in rowReserved[row] and 7 not in rowReserved[row] and 8 not in rowReserved[row] and 9 not in rowReserved[row]:
                res += 1
                right_filled = True
            if not left_filled and not right_filled and 4 not in rowReserved[row] and 5 not in rowReserved[row] and 6 not in rowReserved[row] and 7 not in rowReserved[row]:
                res += 1

        res += (n-len(rowReserved))*2
        return res
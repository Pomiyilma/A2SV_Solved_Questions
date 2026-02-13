for i in range(5):
  row = list(map(int, input().split()))  #the input is splitted (list of str) then mapped into int, Then into List
  if 1 in row:
    col_index = row.index(1)  #eg row = [0, 0, 1, 0, 0], then row.index(1) ===> col_index = 2
    row_index = i
total_moves = abs(row_index - 2) + abs(col_index - 2)   #THE manhattan distance formula
print(total_moves)

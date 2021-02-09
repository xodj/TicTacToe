# write your code here
def display_string(cells_list):
    return """---------
| """ + cells_list[0] + """ """ + cells_list[1] + """ """ + cells_list[2] + """ |
| """ + cells_list[3] + """ """ + cells_list[4] + """ """ + cells_list[5] + """ |
| """ + cells_list[6] + """ """ + cells_list[7] + """ """ + cells_list[8] + """ |
---------"""


print(display_string(list(input('Enter cells: '))))

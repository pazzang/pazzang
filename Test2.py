# str1 = "1억 1,000"
# str2 = "1억"

# editedStr1 = str1.split("억")
# editedStr2 = str2.split("억")


# if editedStr1[1] == "": 
#     firstInt = int(editedStr1[0])*100000000
#     secondInt = 0
#     finalValue = firstInt + secondInt
# else:
#     firstInt = int(editedStr1[0])*100000000
#     secondInt = int(editedStr1[1].replace(",", "")) *10000
#     finalValue = firstInt + secondInt


# # editedInt1 = int(editedStr1[0])*100000000 + int(editedStr1[1].replace(",", "").replace("", 0))*10000
# # editedInt2 = int(editedStr2[0])*100000000 + int(editedStr2[1].replace(",", ""))*10000


# print(finalValue)



# str = "추천.민영. 귀한판상형.탁트인뷰  세안고매매"
# print(str.contains("세안고"))

import pandas as pd

df = pd.DataFrame({'SENDFROM': {0: 'xx@gmail.com', 1: 'yy@xxx.com'},
                   'Test': {0: '1억 5,000',
                            1: '1억'}})

# Use str.split and str.join and astype
df['Test'] = df['Test'].str.split('억')

df['Test'][1]

print(df['Test'][1])
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')
print(data[0])

# 文字計數

wc = {} # word_count

for d in data:
	words = d.split()  # words 是清單
	for word in words:
		if word in wc:
			wc[word] += 1
		else: # word not in words:
			wc[word] = 1 # 新字進字典
			
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))
print(wc['Allen'])

while True:
	word = input('請問你想查甚麼字:')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('這個字沒有出現過喔')














# # 算平均留言長度
# sum_len = 0
# for d in data:
# 	sum_len += len (d)
# 	average_len = sum_len / len(data)
# print('留言的平均長度是', average_len)

# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)
# print('一共有', len(new), '筆留言長度小於100')
# print(new[0])
# print(new[1])

# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)
# print('一共有', len(good), '筆留言提到good')
# print(good[0])



# 1233333333123
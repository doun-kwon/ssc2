from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# MongoDB에 insert 하기

# 'users'라는 collection에 {'name':'bobby','age':21}를 넣습니다.
# db.users.insert_one({
#     'name':'bobby',
#     'age':21
# })
# db.users.insert_one({
#     'name':'kay',
#     'age':27
# })
# db.users.insert_one({
#     'name':'john',
#     'age':30
# })

#list() 함수
# MongoDB에서 데이터 모두 보기
all_users = list(db.users.find())

# 참고) MongoDB에서 특정 조건의 데이터 모두 보기
same_ages = list(db.users.find({'age': 21}))

print(all_users[0])  # 0번째 결과값을 보기
print(all_users[0]['name'])  # 0번째 결과값의 'name'을 보기

for user in all_users:  # 반복문을 돌며 모든 결과값을 보기
    print(user)
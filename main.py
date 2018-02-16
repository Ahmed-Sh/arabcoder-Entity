import models
import store
member1=models.member("ahmed",32)
member2=models.member("ali",25)
post1=models.post("1st post","this is my 1st post")
post2=models.post("2nd post","this is my 2nd post")
post3=models.post("3rd post","this is my 3rd post")

memberStore1=store.MemberStore()
postStore1=store.PostStore()
memberStore1.add(member1)
memberStore1.add(member2)
postStore1.add(post1)
postStore1.add(post2)
postStore1.add(post3)
print "test 1 befor delete --------------------------"
for member in memberStore1.get_all():
	print member
for post in postStore1.get_all():
	print post
print "test 2 after delete --------------------------"
memberStore1.delete(2)
for member in memberStore1.get_all():
	print member
for post in postStore1.get_all():
	print post
print "test 3  --------------------------"
print memberStore1.entity_exists(member2)
print memberStore1.entity_exists(member1)












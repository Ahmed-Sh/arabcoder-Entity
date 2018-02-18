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

def print_all_member():
	print 30*"="+"names"
	for member in memberStore1.get_all():
		print member
def print_all_post():
	print 30*"="+"posts"
	for post in postStore1.get_all():
		print post


def check_member(member):
	if memberStore1.entity_exists(member):
		print "this member is alredy exist"
	else:
		print "not found"	


def print_all_same_members(name):
	print 30*"="+name+" members"
	for member in memberStore1.get_by_name(name):
		print member
def update_member(member):
	new_name=raw_input("enter the new name:")
	new_age=raw_input("enter the new age:")
	memberStore1.update(member,new_name,new_age)

print_all_member()
update_member(member1)
print_all_member()
update_member(member2)
print_all_same_members("mohamed")
check_member(member1)












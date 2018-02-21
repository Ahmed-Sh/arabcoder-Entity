import itertools
class MemberStore:

  members = []
 
  last_id=1

  #def __contains__(self, id):
    #return self.get_by_id(id)!=None
      
          
  def get_all(self):
    return MemberStore.members

  def add(self, member):
      # append member
        member.id=MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id +=1

  def entity_exists(self, member):
      # checks if an entity exists in a store
    return member in self.get_all()

  def get_by_id(self, id):
      # search for member by id
      result=None
      for member in self.get_all():
        if member.id==id:
          result=member
          break
      return result
      

  def delete(self, id):
     # delete member by id
    member=self.get_by_id(id) 
    if self.entity_exists(member): 
      MemberStore.members.remove(member)

  def update(self, member):
     result = member
     all_members = self.get_all()

     for index, current_member in enumerate(all_members):
         if current_member.id == member.id:
             all_members[index] = member
             break

     return result
  def get_by_name(self,name):
    
    for member in self.get_all():
      if member.name==name:
        yield member

  def get_members_with_posts(self,all_post):
    all_members=self.get_all()
    for member, post in itertools.product(all_members, all_post):
      if member.id==post.member_id:
        member.posts.append(post)
          #self.update(member)  
    return self.get_all() 

  def  get_top_two(self,all_post):
    sorted_members=sorted(self.get_members_with_posts(all_post))
    return sorted_members[:2]

        

#-----------------------------------------------------------------------------------------------

class PostStore:

  posts = []
  
  def get_all(self):
    return PostStore.posts

  def add(self, post):
    PostStore.posts.append(post)

  def entity_exists(self, post): 
        return post in PostStore.posts


   

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

  def update(self,member,new_name,new_age):
    member.name=new_name
    member.age=new_age

  def get_by_name(self,name):
    
    for member in self.get_all():
      if member.name==name:
        yield member

#-----------------------------------------------------------------------------------------------

class PostStore:

  posts = []
  
  def get_all(self):
    return PostStore.posts

  def add(self, post):
    PostStore.posts.append(post)

  def entity_exists(self, post): 
        return post in PostStore.posts
           


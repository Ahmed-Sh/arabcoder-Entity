class MemberStore:

  members = []
  last_id=1

  def __contains__(self, id):
        if self.get_by_id(id)!=None:
          return True
        return False  
          

  def get_all(self):
    return MemberStore.members

  def add(self, member):
      # append member
        member.id=MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id =member.id+1

  def entity_exists(self, member):
      # checks if an entity exists in a store
    return member.id in self           


  def get_by_id(self, id):
      # search for member by id
      for member in MemberStore.members:
        if member.id==id:
          return member
      return None 

  def delete(self, id):
     # delete member by id
    if id in self: 
      member=self.get_by_id(id)
      MemberStore.members.remove(member)
  

#-----------------------------------------------------------------------------------------------

class PostStore:

  posts = []
  
  def get_all(self):
    return PostStore.posts

  def add(self, post):
    PostStore.posts.append(post)

  def entity_exists(self, post): 
        return post in PostStore.posts
           


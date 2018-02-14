class MemberStore:

  members = []

  def get_all(self):
      for member in MemberStore.members:
        print member

  def add(self, member):
      # append member
      if MemberStore().entity_exists(member):
        print "this member is already exists"
      else:
        MemberStore.members.append(member)

  def entity_exists(self, member):
      # checks if an entity exists in a store
      if len(MemberStore.members) !=0: 
        if member in MemberStore.members:
          return True
        else:
          for x in MemberStore.members:
            if x.id==member.id:
             return True
      return False           


  def get_by_id(self, id):
      # search for member by id
      for member in MemberStore.members:
        if member.id==id:
          return member
      return None 
  def delete(self, id):
     # delete member by id 
    member=MemberStore().get_by_id(id)
    if member !=None:
      MemberStore.members.remove(member)
    else:
      print "this id not found"  




class PostStore:
  posts = []
  def get_all(self):
    for post in PostStore.posts:
      print post

  def add(self, post):
      # append post
      if PostStore().entity_exists(post):
        print "this post is already exists"
      else:
        PostStore.posts.append(post)

  def entity_exists(self, post):
      # checks if an entity exists in a store
      if len(PostStore.posts) !=0: 
        if post in PostStore.posts:
          return True
      return False           


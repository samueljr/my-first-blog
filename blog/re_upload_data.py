import csv
from blog.models import Post
from django.contrib.auth.models import User
me = User.objects.get(username='samueljr')

with open('blog/pol_data.csv', 'r') as dat:
  reader = csv.reader(dat, delimiter=',', quotechar='|')
  for i, row in enumerate(reader):
    if i > 0:
      print (row[1] + " of " + row[3])
      try:
        Post.objects.create(author=me, name=row[1], party=row[2], state_code=row[3], np_score=row[4], id=row[0], house_start=row[5], house_end=row[6], senate_start=row[7], senate_end=row[8], rank=row[9], rank_percent=row[10])
      except:
        pass
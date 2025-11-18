blog_views = [150, 800, 2500, 600, 1200, 450, 3000]

total_views = 0 
trending_post = 0

for i in blog_views:
    if i > 1000:
        print("trending")
        trending_post += 1
    elif 500 < i <= 1000:
        print("average")
    else:
        print("low traffic")

    total_views += i

print("Total trending posts:", trending_post)
print("Total views over the period:", total_views)


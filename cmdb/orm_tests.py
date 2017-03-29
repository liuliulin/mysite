import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

django.setup()

from cmdb import models

#
# models.Colors.objects.create(colors='黑黑1')
# models.Colors.objects.filter(colors='橙色').delete()

# models.Colors.objects.filter(colors='黑黑').update(colors='橙色')
# print(models.Colors.objects.filter(id__gt=1, id__lt=5))




# print(models.Ball.objects.get(description="红球").color.colors)
# print(models.Colors.objects.get(ball__description="红球").colors)

# print(models.Colors.objects.get(colors="红色").ball.description)
# print(models.Ball.objects.get(color__colors="红色").description)

# color_obj = models.Colors.objects.create(colors="黑色")
# models.Ball.objects.create(color=color_obj, description="黑球")

# models.Ball.objects.filter(color__colors="红色").update(description="红红球")

# print(models.Ball.objects.all())


# print(models.Clothes.objects.get(description="红内裤").color.colors)
# print(models.Colors.objects.get(clothes__description="红内裤").colors)

# color_obj = models.Colors.objects.get(colors="红色")
# print(color_obj.clothes_set.all())
# print(models.Colors.objects.get(colors="红色").clothes_set.all())

# print(models.Clothes.objects.filter(color=models.Colors.objects.get(colors="红色")))
# print(models.Clothes.objects.filter(color__colors="红色"))

# color_id = models.Colors.objects.get(colors="红色").id
# print(models.Clothes.objects.filter(color_id=color_id))


# print(models.Clothes.objects.filter(color=models.Colors.objects.get(colors="红色")).values('color__colors', 'description'))
# print(models.Clothes.objects.filter(color__colors="红色").values('color__colors', 'description'))

# models.Clothes.objects.create(color=models.Colors.objects.get(colors="绿色"), description="绿裤子")

# models.Clothes.objects.filter(color__colors="绿色").update(description="绿帽子")
# models.Clothes.objects.get(description="绿帽子").delete()
# models.Colors.objects.filter(colors="绿色").delete()


# child_obj = models.Child.objects.get(name="小明")
# print(child_obj.favor.all())
# print(models.Child.objects.get(name="小明").favor.all())
# print(models.Colors.objects.filter(child__name="小明"))

# print(models.Colors.objects.get(colors="黄色").child_set.all())
# print(models.Child.objects.filter(favor__colors="黄色"))=-09
# child_obj = models.Child.objects.create(name="小红")
# colors_obj = models.Colors.objects.all()
# child_obj.favor.add(*colors_obj)

# child_obj = models.Child.objects.get(name="小红")
# colors_obj = models.Colors.objects.filter(colors__in=["蓝色", "黄色"])
# child_obj.favor.clear()
# child_obj.favor.add(*colors_obj)

# child_obj = models.Child.objects.get(name="小红")
# colors_obj = models.Colors.objects.get(colors="黄色")
# child_obj.favor.clear()
# child_obj.favor.add(colors_obj)


# child_obj = models.Child.objects.get(name="小红")
# colors_obj = models.Colors.objects.get(colors="蓝色")
# colors_obj.child_set.add(child_obj)

# children_obj = models.Child.objects.all()
# colors_obj = models.Colors.objects.get(colors="蓝色")
# colors_obj.child_set.add(*children_obj)


# models.Child.objects.get(name="小红").favor.clear()
# models.Colors.objects.get(colors="蓝色").child_set.clear()

child_obj = models.Child.objects.get(name="果然")
print(child_obj.sex)
print(child_obj.get_sex_display())

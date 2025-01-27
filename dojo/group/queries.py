from crum import get_current_user
from django.db.models import Exists, OuterRef

from dojo.authorization.authorization import get_roles_for_permission
from dojo.authorization.roles_permissions import Permissions
from dojo.models import Dojo_User, Dojo_Group, Dojo_Group_Member, Product_Group, Product_Type_Group, Role


def get_authorized_groups(permission):
    user = get_current_user()

    if user is None:
        return Dojo_Group.objects.none()

    if user.is_superuser:
        return Dojo_Group.objects.all().order_by("name")

    roles = get_roles_for_permission(permission)
    authorized_roles = Dojo_Group_Member.objects.filter(group=OuterRef("pk"),
        user=user,
        role__in=roles)
    groups = Dojo_Group.objects.annotate(user=Exists(authorized_roles)).order_by("name")
    return groups.filter(user=True)


def get_authorized_group_members(permission):
    user = get_current_user()

    if user is None:
        return Dojo_Group_Member.objects.none()

    if user.is_superuser:
        return Dojo_Group_Member.objects.all().order_by("id").select_related("role")

    groups = get_authorized_groups(permission)
    return Dojo_Group_Member.objects.filter(group__in=groups).order_by("id").select_related("role")


def get_authorized_group_members_for_user(user):
    groups = get_authorized_groups(Permissions.Group_View)
    return Dojo_Group_Member.objects.filter(user=user, group__in=groups).order_by("group__name").select_related("role", "group")


def get_group_members_for_group(group):
    return Dojo_Group_Member.objects.filter(group=group).select_related("role")


def get_product_groups_for_group(group):
    return Product_Group.objects.filter(group=group).select_related("role")


def get_product_type_groups_for_group(group):
    return Product_Type_Group.objects.filter(group=group).select_related("role")


def get_group_member_roles():
    return Role.objects.exclude(name="API_Importer").exclude(name="Writer")

def get_users_for_group(group_name):
    group_members = Dojo_Group_Member.objects.filter(group__name=group_name).values_list("user", flat=True)
    return Dojo_User.objects.filter(id__in=group_members)
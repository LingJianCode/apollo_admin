from django.shortcuts import render
from django.db.models import Subquery, Count
from django.db import connection
from django.http import JsonResponse
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *


def show(request, user_name):
	user_roles = Userrole.objects.values("roleid").filter(userid=user_name, isdeleted=0)
	# print(user_roles.query)
	# print(user_roles)


	roles = Role.objects.values("id").filter(id__in=Subquery(user_roles.values('roleid')), isdeleted=0)
	# print(roles.query)
	print(roles)
	have_roles = []
	for role in roles:
		have_roles.append(role["id"])

	context = {}
	context['user_name'] = user_name
	context['have_roles'] = have_roles
	all_roles = Role.objects.values("id","rolename").filter(isdeleted=0)
	context['all_roles'] = all_roles
	return render(request, 'permission/show.html', context)

def display(request):
	users = Users.objects.values("username").filter(enabled=1)
	apps = App.objects.filter(isdeleted=0)


	context={}
	context['users'] = users
	context['apps'] = apps
	return render(request, 'permission/display.html', context)


@csrf_exempt
def query(request):
	if(request.method == 'POST'):
		print(request.body)
		data = json.loads(request.body)
		sql = "SELECT NamespaceName as app_namespace from ApolloConfigDB_pro.Namespace where AppId='%s' and ClusterName='default' and IsDeleted=0" % data['app_name']
		print(sql)

		with connection.cursor()  as cursor:
			cursor.execute(sql)
			res = cursor.fetchall()
			# columns = [col[0] for col in cursor.description]
			# res = [dict(zip(columns, row)) for row in cursor.fetchall()]
			# print(res)
		roles=[
			"Master+%s" % data['app_name'],
		]

		env = ['DEV','FAT','UAT','PRO']
		for r in res:
			roles.append("ModifyNamespace+%s+%s" % (data['app_name'], r[0]))
			roles.append("ReleaseNamespace+%s+%s" % (data['app_name'], r[0]))
			for e in env:
				roles.append("ModifyNamespace+%s+%s+%s" % (data['app_name'], r[0], e))
				roles.append("ReleaseNamespace+%s+%s+%s" % (data['app_name'], r[0], e))

		roles = Role.objects.values("id","rolename").filter(rolename__in=roles, isdeleted=0)
		# print(roles.query)
		# print(roles)

		role_ids = []
		for role in roles:
			role_ids.append(role['id'])

		print(role_ids)
		user_roles = Userrole.objects.values_list("roleid").filter(userid=data['user_name'], roleid__in=role_ids, isdeleted=0)
		print(user_roles.query)
		exist_roles = []
		for user_role in user_roles:
			exist_roles.append(user_role[0])

		res_data = {}
		res_data['all_roles'] = list(roles)
		res_data['exist_roles'] = exist_roles
		return JsonResponse(res_data)

@csrf_exempt
def update(request):
	if(request.method == 'POST'):
		data = json.loads(request.body)
		res_data={"status":"ok"}
		
		if data['fun'] == 'revoke':
			print("+++++++++++++%s" % data['fun'])
			role = Role.objects.get(id=data['role_id'], isdeleted=0)
			print(role.rolename)
			if role.rolename.split('+')[0] == 'Master':
				res = Userrole.objects.filter(roleid=data['role_id'], isdeleted=0).annotate(count=Count('id')).values('count')
				if res[0]['count'] == 1:
					res_data['status'] = 'error'
					res_data['msg'] = 'Master lest exist one people'
					return JsonResponse(res_data)
			res = Userrole.objects.filter(roleid=data['role_id'], userid=data['user_name'], isdeleted=0).update(isdeleted=1)
			res_data['msg'] = res
		elif data['fun'] == 'add':
			print("-------------%s" % data['fun'])
			res = Userrole.objects.filter(roleid=data['role_id'], userid=data['user_name'], isdeleted=0).annotate(count=Count('id')).values('count')
			print(res.query)
			print(res)

			if res and res[0]['count'] >= 1:
				res_data['msg'] = '权限已经存在'
				return JsonResponse(res_data)

			user_role = Userrole()
			user_role.roleid=data['role_id']
			user_role.userid=data['user_name']
			user_role.datachange_createdby='lingjian'
			user_role.datachange_lastmodifiedby='lingjian'
			user_role.datachange_createdtime=now()
			res=user_role.save()
			res_data['msg'] = '还行'

		
		return JsonResponse(res_data)


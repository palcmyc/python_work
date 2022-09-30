current_users = ('admin','eric','amy','anne','ani')
new_users = ['ani','mike','nike','addidas','newbalance','eric']
for new_user in new_users:
	if new_user in current_users:
		print("false")
	else:
		print("OK")
		
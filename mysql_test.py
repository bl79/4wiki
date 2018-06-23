# -*- coding: utf-8 -*-
import urllib.parse

# import paramiko
#
# host = 'tools-login.wmflabs.org'
# user = 'vladi2016'
# secret = 'goreibeda'
# port = 22
#
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname=host, username=user, password=secret, port=port)
# stdin, stdout, stderr = ssh.exec_command('ls -l')
# data = stdout.read() + stderr.read()
#
#
#
# print(str(data))



from sqlalchemy import create_engine

user = 'u14134'
pw = '4mlodHqAsy3xTivW'
host = '127.0.0.1:4711'  # tools-login.wmflabs.org/
db = 'ruwiki_p'

e = create_engine("mysql://%s:%s@%s/%s?charset=utf8" % (user, pw, host, db))

tpl = 'Любкер'
time_lastcheck = 20160910000000
sql = """SELECT
		  page.page_title,
		  MAX(revision.rev_timestamp) AS timestamp
		FROM page
		  INNER JOIN templatelinks
			ON page.page_id = templatelinks.tl_from
		  INNER JOIN revision
			ON page.page_id = revision.rev_page
		WHERE templatelinks.tl_namespace = 10
		AND page.page_namespace = 0
		AND templatelinks.tl_title = '%s'
		AND revision.rev_timestamp > %d
		GROUP BY page.page_title
		ORDER BY page.page_title""" % (tpl, time_lastcheck)
for row in e.execute(sql):
	print(dict(row))
	# print(row)

	# if len(result) > 0:
	# print(len(result))
	# for rs in result:
	time_lastedit = row['timestamp']
	r = row['page_title']
	r = urllib.parse.quote_from_bytes(r)
	# r = urllib.parse.urlencode(r, encoding='utf8')
	r = urllib.parse.unquote(r, encoding='utf8')
	print(r, time_lastedit)

# ssh.close()
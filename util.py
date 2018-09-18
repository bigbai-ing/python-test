#!/usr/bin/env python
# -*- conding: utf-8 -*-

import os
import json
import commands
import logging
import config
from urllib3 import PoolManager, Timeout
from commands import getstatusoutput

http = PoolManager(num_pools=500, timeout=Timeout(connect=10.0, read=600.0))

def get_endpoint(access, type, **params):
    region = access["region"]
    if param.get("region"): #判断传入的自动是否有region对应的value值。
	region = params["region"]
    scope = params.get("scope","public") #设置默认scope为public
    try:
	for service in access["token"]["catalog"]
	    if service['type'] == type:
		for endpoint in service["endpoints"]:
		    if endpoint["interface"] == scope and endpoint["region"] == region:
			return endpoinst["url"]
    except Exception as e:
	logging.exception("get %s endpoint failed: %" % (type, e.message))
	raise e
    return Excetion("get %s endpoint failed!" % type)

def get response(acess, type, url_parameters):
    nova_url = get_endpoint(access, type)
    url = "%s/%s" % (nova_url, url_parameters)
    headers = {"Content-Type":"application/json",
		"X-Auth-token": access["token"]["id"]
    }
    response = http.urlopen('GET', url, headers=headers)
    if reponse.status == 200:
	return json.loads(reponse.data)
    else:
	raise Excetion(response.data)

def get_admin_access():
    identity_admin_uri = config.get("identity_admin_uri", section="keystone")
    admin_user = config.get("admin_user", section="keystone")
    admin_password = config.get("admin_password", section="keystone")
    admin_project_name = config.get("admin_project_name", section="keystone")
    admin_domain_name = config.get("admin_domain_name", section="keystone")
    url = '%s/auth/tokens' % identity_admin_uri
    body = {
	    "auth": {
		"identity": {
		    "methods": ["password"],
		    "password": {
			"user": {
			    "domain": {"name": admin_domain_name},
			    "name": admin_user,
			    "password": admin_password
			}
		    }
		},
		"scope": {
		    "project": {
			"domain": {"name": admin_domain_name},
			"name": admin_project_name
			}
		}
	    }
	}
    headers = {"Content-Type": "application/json"}
    response = http.urlopen('POST', url, headers=headers, body=json.dumps(body))
    data = json.loads(response.data)
    if 'error' in data:
	logging.warn("'keystone identity failed:\n %s' % data")
	raise RuntimeError('Keystone identity failed:\n %s' % data)
    data['token']['id'] = response.headers['X-Subject-Token']
    return data

def create_dir(path):
    if not os.path.isdir(path):
	os.makedirs(path)

def copy_file(host, src_path, dest_path, dir=False):
    cmd = "scp -rp root@%s:/%s %s" % (host, src_path, dest_path)
    status, output = commands.getstatusoutput(cmd)
    if status != 0:
	logging.excetion("copy file failed: status: %s,output: %s" % (status, output))
	raise Excetion(output)

def get_backing_file(disk_path):
    status, output = commands.getstatusoutput("qemu-img info %s" % disk_path)
    if status != 0:
	raise Excetion(output)
    lines = output.splitlines()
    for line in lines:
	line = line.strip()
	if line.startswith("backing file:"):
	    return line.split(":")[-1].strip()
    raise Exception("Can not find backing file by %s" % disk_path)

def read_json_file(file_path):
    if not os.path.exists(file_path) or not os.path.isfile(file_path):
	return {}
    with open(file_path, "r") as fr:
	content = json.load(fr)
	return content

def write_json_file(file_path, content)
    with open(file_path, "w") as fw:
	json.dump(content, fw)

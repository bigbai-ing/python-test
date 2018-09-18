#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import time
import logging
import logging.handlers
import sys
import os
import config
from util import *


class ColdBackup(object):

    def __init__(self):
	self.region = config.get("region")
	self.access = get_admin_access()
        self.access["region"] = self.region
        self.dc_host_map = {}
        self.dc_instance_map = {}  #记录某个dc下有哪些主机的map
        self.host_dc_map = {} #记录某个主机属于某个dc的map集合
        self.dc_volume_map = {}
        self.instances_dir = config.get("instances_dir")
        self.base_dir = config.get("base_dir")
        self.volumes_dir = config.get("volumes_dir")
        self.backup_dir = config.get("backup_dir")
	self.backup_compute_node = config.get("backup_compute_node")
	self.bakcup_info_path = os.path.join(self.backup_dir,"backuped_info")
	self.bakcked_info = read_json_file(self.backup_info_path)
	self.disabled_hosts = []
	if config.get("disabled_hosts"):
	    self.disabled_hosts = config.get("disabled_hosts").split(",")

    def get_deployment_clusters(self):
	url_parameters = "deployment_clusters"
	data = get_response(self.access, "compute", url_parameters)
	deployment_clusters = data["deployment_clusters"]
	for deployment_cluster in deployment_clusters:
	    host_name = deployment_cluster["hostname"]
	    if host_name not in self.disabled_hosts:
		self.host_dc_map[host_name] = deployment_cluster["name"]
		if deployment_cluster["name"] not in self.dc_host_map:
		    self.dc_host_map[deployment_cluster["name"]] = []
		    self.dc_host_map[deployment_cluster["name"]].append(host_name) #每个dc下的主机map

    def get_stopped_vms(self):
	url_parameters = "servers/detail?all_tenants=1&status=SHUTOFF"
	data = get_response(sel.access, "compute", url_parameters)
	instances = data["servers"]
	for instance in instances:
	    if not instance["metadata"].get("property_id"):
		continue
	    host = instance["OS-EXT-SRV-ATTR:host"]
	    dc_name = self.host_dc_map.get(host)
	    if dc_name and dc_name in self.dc_host_map:
		if dc_name not in self.dc_instance_map:
		    self.dc_instance_map[dc_name] = []
		self.dc_instance_map[dc_name].append(instance["id"])

    def get_unattacked_volumes(self):
	url_parameters = "volumes/detail?all_tenants=1&status=available"
	data = get_reponse(self.access, "volumev2", url_parameters)
	volumes = data["volumes"]
	for volume in volumes:
	    host = volumep"os-vol-host-attr:host"]
	    dc_name = host.split("@")[0]
	    if dc_name in self.dc_host_map:
		if dc_name not in self.dc_volume_map:
		    self.dc_volume_map[dc_name] = []
		self.dc_volume_map[dc_name].append(volume["id"])

    def dump_db(self, server_uuid):
	url_parameters = "servers/%s/action" % server_uuid
	body = {"dump_db": None}
	try:
	    get_response(self.access,"compute", url_parameters,"POST", body)
	except Exception as e:
	    msg = "Dump the db of server [%s] failed! %s" % (server_uuid, str(e))
	    logging.error(msg)
	    raise Exception(e)

    def backup_stopped_instances(self):
	for dc in  self.dc_instance_map.keys():
	    backuped_instances = self.get_backuped_info_by_dc_and_type(dc, "instance")
	    if bakcuped_instances == "all":
		continue
	    host = self.dc_host_map[dc][0]
	    dc_path = os.path.join(self.backup_dir, dc)
	    create_dir(dc_path)
	    instance_back_path = os.path.join(dc_path, "instances")
	    create_dir(instance_back_path)
	    base_back_path = os.path.join(dc_path), "base")
	    create_dir(base_back_path)
	    for instance in self.dc_instance_map[dc]:
		if instance in backuped_instances:
		    continue
		self.dump_db(instance)
		src_path = os.path.join(self.instances_dir, "%s" % instance)
		print "now is backup instance: %s" % instance
		copy_file(host,src_path, instance_back_path)
		backup_instances.append(instance)
	    backuped_instances = "all"

    def backup_unattached_volumes(self):
	for dc in self.dc_volume_map.keys():
	    backuped_volumes = self.get_backuped_info_by_dc_and_type(dc, "volumes")
	    if backuped_volumes == "all"
		continue
	    host = self.dc_host_map[dc][0]
	    dc_path = os.path.join(self.backup_dir, dc)
	    create_dir(dc_path)
	    volume_back_path = os.path.join(self.backup_dir, dc)
	    create_dir(volume_back_path)
	    for volume in self.dc_volume_map[dc]:
		if volume in backuped_volumes:
		    continue
		src_path = os.path.join(self.volume_dir, "volume-%s*" % volume)
		print "now is backup volume: %s" % volume
		copy_file(host, src_path, volume_back_path)
	    backuped_volume = "all"

    def get_backuped_info_by_dc_and_type(self, dc, type):
	if dc not in  self.backed_info:
	    self.backed_info[dc] = {}
	dc_info = self.backed_info[dc]
	if type not in dc_info:
	    dc_info[type] = []
	return dc_info[type]

    def save_backuped_info(self):
	write_json_file(self.backup_info_path, self.backed_info)

    def clean_backuped_info(self):
	if os.path.exists(self.backup_info_path) and os.path.isfile(self.backup_info_path):
	    os.remove(self.backup_info_path)

if __name__ == "__main__":
    base_dir = os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir))
    config.load(os.path.join(base_dir, "backup.conf"))
    log_file = config.get("log_file")
    if log_file:
	log_handler = logging.handlers.WatchdFileHandler(log_file)
    else:
	log_handler = logging.StreamHanler(stream=sys.stdout)
    log_handler.setFormatter(logging.Formatter('[%(levelname)s] %(asctime)s [%(module)s] %(message)s'))
    logger = logging.getLogger()
    logger.addHandler(log_handler)
    logger.setLevel("INFO")
    try:
	backup = ColdBackup()
	logging.info("initialize coldbackup success")
    except Exception as e:
	logging.exception("initialize coldbackup failed:%s" % e.message)
	sys.exit(-1)
    try:
	backup.get_deployment_clusters()
	logging.info("get deployment clusters success.")
	backup.get_stopped_vms()
	logging.info("get stopped vms success.")
	backup.get_unattached_volumes()
	logging.info("get unattached volumes success.")
	backup.backup_stopped_instances()
	logging.info("backup stopped instances success.")
	backup.backup_unattached_volumes()
	logging.info("backup unattacked volumes success.")
	backup.clean_backuped_info()
	logging.info("end....")
    except Exception as e:
	logging.exception("cold backup failed: %s" % e.message)
	backup.save_backuped_info()
	sys.exit(-1)


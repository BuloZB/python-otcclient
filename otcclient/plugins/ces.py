#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy


from otcclient.core.OtcConfig import OtcConfig 
from otcclient.utils import utils_http

from otcclient.core.otcpluginbase import otcpluginbase
from otcclient.core.pluginmanager import getplugin
import base64
from time import sleep
import sys
import json
from otcclient.plugins.ecs import ecs
import os
    
class ces(otcpluginbase):
    ar = {}    
    
    @staticmethod
    def otcOutputHandler(): 
        return getplugin(OtcConfig.OUTPUT_FORMAT)
 
    def otctype(self):
        return "func" 


    @staticmethod
    def describe_alarms():
        url = ces.baseurl+ "/V1.0/" + OtcConfig.PROJECT_ID + "/alarms"
        if not (OtcConfig.ALARM_NAME is None):
            ces.convertALALMNameToId()
            url = ces.baseurl+ "/V1.0/" + OtcConfig.PROJECT_ID + "/alarms?start=" + OtcConfig.ALARM_ID       
                           
        ret = utils_http.get(url)
        print (json.dumps(json.loads(ret), indent=4, sort_keys=True))
        #elb.otcOutputHandler().print_output(ret, mainkey="") 
        #listkey={"id", "name", "status", "vip_address","update_time","bandwidth","type"}
        return ret

    @staticmethod
    def list_metrics():
        url = ces.baseurl+ "/V1.0/" + OtcConfig.PROJECT_ID + "/metrics"                           
        ret = utils_http.get(url)
        print (json.dumps(json.loads(ret), indent=4, sort_keys=True))
        return ret

    @staticmethod
    def list_favorite_metrics():
        url = ces.baseurl+ "/V1.0/" + OtcConfig.PROJECT_ID + "/favorite-metrics"                           
        ret = utils_http.get(url)
        print (json.dumps(json.loads(ret), indent=4, sort_keys=True))
        return ret

    @staticmethod
    def list_metric_data():
        url = ces.baseurl+ "/V1.0/" + OtcConfig.PROJECT_ID + "/metric-data"                           
        ret = utils_http.get(url)
        print (json.dumps(json.loads(ret), indent=4, sort_keys=True))
        return ret

    @staticmethod
    def describe_quotas():
        url = ces.baseurl+ "/V1.0/" + OtcConfig.PROJECT_ID + "/quotas"                           
        ret = utils_http.get(url)
        print (json.dumps(json.loads(ret), indent=4, sort_keys=True))
        return ret


#     @staticmethod
#     def delete_alarms():        
#         if not (OtcConfig.ALARM_NAME is None):
#             ces.convertALARMNameToId()            
#         if not (OtcConfig.VPCNAME is None):
#             ecs.convertVPCNameToId()   
#         url = ces.baseurl+ "/v1.0/" + OtcConfig.PROJECT_ID + "/alarms" + "?start=" + OtcConfig.ALARM_ID              
# 
#         ret = utils_http.delete(url)
#         print(ret)
#         return ret
# 
# 
#     @staticmethod
#     def convertALARMNameToId():
#         url = ces.baseurl+ "/v1.0/" + OtcConfig.PROJECT_ID + "/alarms"        
#         JSON = utils_http.get(url)        
#         parsed  = json.loads(JSON)
#         alarms = parsed["alarms"]        
#         ret = None
#         for alarm in alarms:
#             if alarm.get("name") == OtcConfig.ALARM_NAME: # and ( loadbalancer.get("vpc_id") == OtcConfig.VPCID or OtcConfig.VPCID is None ) :
#                 OtcConfig.ALARM_ID = alarm["id"]
#                 ret = OtcConfig.ALARM_ID
#         return ret               
# 
# 
#     @staticmethod 
#     def create_alarms():
#         if not (OtcConfig.ALARM_NAME is None):
#             ces.convertALARMNameToId()
#         if not (OtcConfig.VPCNAME is None):
#             ecs.convertVPCNameToId()        
#         
#          
#         REQ_CREATE_ALARM = "{ \"name\": \"" + OtcConfig.LOADBALANCER_NAME + "\", \"description\": \"" + OtcConfig.LOADBALANCER_NAME+ "\", \"vpc_id\": \"" + OtcConfig.VPCID +"\", \"bandwidth\": 10, \"type\": \"External\", \"admin_state_up\": true }" 
#         url = ces.baseurl+ "/v1.0/" + OtcConfig.PROJECT_ID + "/alarms"
#         ret = utils_http.post(url, REQ_CREATE_ALARM)
#         print( ret )
#         maindata = json.loads(ret)
#         if "code" in  maindata:            
#             print("Can not create:" +maindata["message"])  
#             os._exit( 1 )             
#                             
#         #ecs.otcOutputHandler().print_output(ret, mainkey="loadbalancer")
#         return ret




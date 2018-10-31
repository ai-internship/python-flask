#!/usr/bin/python

#-*-coding: utf-8 -*-
##from __future__ import absolute_import
###
from flask import Flask, jsonify, render_template, request
from flask_jsonpify import jsonpify
import json
import time

from flask_restful import Resource, Api, reqparse
import re
import random


app = Flask(__name__)
api = Api(app)

stocktable = {}
stocktable['dtac'] = 29.1
stocktable['ais'] = 49.4
stocktable['true'] = 16.1
stocktable['ptt'] = 52.3
stocktable['scg'] = 55.2





def get_stockprice(stockname): 
	try:
		stockprice =  "The current price is " + str(stocktable[stockname])
	except:
		stockprice = 'cannot find stock'
	return stockprice
		

class getstockpriceapi(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('stockname', type=str)
        dictp = parser.parse_args()
        inputname = dictp['stockname']
        returnstring = get_stockprice(inputname)
        return returnstring

class heyyou(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        dictp = parser.parse_args()
        inputname = dictp['name']
        returnstring = 'hello '+inputname

        r = {'message': returnstring}
        r = json.dumps(r)
        return json.loads(r)

api.add_resource(heyyou, '/heyyou',endpoint='heyyou')
api.add_resource(getstockpriceapi, '/getstock',endpoint='getstock')
#api.add_resource(check_balance, '/checkbalance',endpoint='checkbalance')
if __name__ == '__main__':
    app.run(threaded=True)

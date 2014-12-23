from flask import render_template, request
from flask.views import View
from urllib2 import urlopen
from kati import mongo
from kati import utils
from elasticsearch import Elasticsearch
import json
from slugify import slugify


class ElasticIndexer(View):

    def dispatch_request(self):

        transcripts_cursor = mongo.db.transcripts.find()

        es = Elasticsearch()


        for doc in transcripts_cursor:
            for speech in doc['speech']:
                es.index(index="transcriptus", doc_type="speech", body=speech)
            for agenda in doc['agenda']:
                es.index(index="transcriptus", doc_type="agenda", body=agenda)

        return render_template('index.html')

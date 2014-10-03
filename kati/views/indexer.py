from flask import render_template
from flask.views import View
from kati import mongo
from elasticsearch import Elasticsearch


class ElasticIndexer(View):

    def dispatch_request(self):
        transcripts_cursor = mongo.db.transcripts.find()
        es = Elasticsearch()
        for doc in transcripts_cursor:
            for speech in doc['speech']:
                es.index(index="transcript", doc_type="speech", body=speech)

            for agenda in doc['agenda']:
                es.index(index="transcript", doc_type="agenda", body=speech)

        return render_template('index.html')

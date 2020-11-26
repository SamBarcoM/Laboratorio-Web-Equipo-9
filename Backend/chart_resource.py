from flask import jsonify
from flask_restful import Resource
from collections import Counter, defaultdict
from pprint import pprint
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from mongo_functions import mongoController

class ChartResource(Resource):
    def get(self):
        # requests = mongoController.INSTANCE.retrieve_requests()
        # students = mongoController.INSTANCE.retrieve_students()
        
        # Create number of users using the feature.
        # Needs a set of users by date.
        unique_users_per_month = []
        for idx, month in enumerate(mongoController.INSTANCE.get_unique_users_per_month()):
            unique_users_per_month.append({
                'x': idx,
                'y': month['total'],
                'y0': 0,
            })
        
        # Get number of missing counts per requirements.
        no_missing_per_reqs = [
            { 'x': "Career Exam", 'y': mongoController.INSTANCE.get_student_field_count('career exam'), 'y0': 0 }, # Career Exam.
            { 'x': "CENEVAL", 'y': mongoController.INSTANCE.get_student_field_count('CENEVAL'), 'y0': 0 }, # CENEVAL.
            { 'x': "e Signature", 'y': mongoController.INSTANCE.get_student_field_count('e sign'), 'y0': 0 }, # E Signature.
            { 'x': "Education Credit", 'y': mongoController.INSTANCE.get_student_field_count('education credit'), 'y0': 0 }, # Education Credit.
            { 'x': "English Exam", 'y': mongoController.INSTANCE.get_student_field_count('english exam'), 'y0': 0 }, # English Exam.
            { 'x': "Financial Services", 'y': mongoController.INSTANCE.get_student_field_count('financial services'), 'y0': 0 }, # Financial Services.
            { 'x': "Graduation Requests", 'y': mongoController.INSTANCE.get_student_field_count('graduation request'), 'y0': 0 }, # Graduation Requests.
            { 'x': "Library", 'y': mongoController.INSTANCE.get_student_field_count('library'), 'y0': 0 }, # Library.
            { 'x': "Photography", 'y': mongoController.INSTANCE.get_student_field_count('photography'), 'y0': 0 }, # Photography.
            { 'x': "Program", 'y': mongoController.INSTANCE.get_student_field_count('program'), 'y0': 0 }, # Program.
            { 'x': "Social Service", 'y': mongoController.INSTANCE.get_student_field_count('social service'), 'y0': 0 }, # Social Service.
        ]

        # % of students ready to graduate.
        percentage_student_to_graduate = 100 * mongoController.INSTANCE.get_student_completed_count() / mongoController.INSTANCE.get_students_count()
        # print(percentage_student_to_graduate)

        # Most searched for requirements
        entity_word_cloud = [
            { "text": 'Photography', "value": mongoController.INSTANCE.get_entity_amount("photography") },
            { "text": 'CENEVAL', "value": mongoController.INSTANCE.get_entity_amount("CENEVAL") },
            { "text": 'E-sign', "value": mongoController.INSTANCE.get_entity_amount("e sign") },
            { "text": 'Education Credit', "value": mongoController.INSTANCE.get_entity_amount("education credit") },
            { "text": 'English Exam', "value": mongoController.INSTANCE.get_entity_amount("english exam") },
            { "text": 'Financial Services', "value": mongoController.INSTANCE.get_entity_amount("financial services") },
            { "text": 'Graduation Request', "value": mongoController.INSTANCE.get_entity_amount("graduation request") },
            { "text": 'Library', "value": mongoController.INSTANCE.get_entity_amount("library") },
            { "text": 'Program', "value": mongoController.INSTANCE.get_entity_amount("program") },
            { "text": 'Social Service', "value": mongoController.INSTANCE.get_entity_amount("social service") }
        ]

        requirements_per_campus = [
            # Career Exam 0
            [
                {"x": "CEM", "y":mongoController.INSTANCE.get_req_per_campus("career exam","CEM")},
                {"x": "CSF", "y":mongoController.INSTANCE.get_req_per_campus("career exam","CSF")},
                {"x": "CCM", "y":mongoController.INSTANCE.get_req_per_campus("career exam","CCM")}
            ],
            # E-sign 1
            [
                {"x": "CEM", "y":mongoController.INSTANCE.get_req_per_campus("e sign","CEM")},
                {"x": "CSF", "y":mongoController.INSTANCE.get_req_per_campus("e sign","CSF")},
                {"x": "CCM", "y":mongoController.INSTANCE.get_req_per_campus("e sign","CCM")}
            ],
            # Education Credit 2
            [
                {"x": "CEM", "y":mongoController.INSTANCE.get_req_per_campus("education credit","CEM")},
                {"x": "CSF", "y":mongoController.INSTANCE.get_req_per_campus("education credit","CSF")},
                {"x": "CCM", "y":mongoController.INSTANCE.get_req_per_campus("education credit","CCM")}
            ],
            # English Exam 3
            [
                {"x": "CEM", "y":mongoController.INSTANCE.get_req_per_campus("english exam","CEM")},
                {"x": "CSF", "y":mongoController.INSTANCE.get_req_per_campus("english exam","CSF")},
                {"x": "CCM", "y":mongoController.INSTANCE.get_req_per_campus("english exam","CCM")}
            ],
            # Financial Services 4
            [
                {"x": "CEM", "y":mongoController.INSTANCE.get_req_per_campus("financial services","CEM")},
                {"x": "CSF", "y":mongoController.INSTANCE.get_req_per_campus("financial services","CSF")},
                {"x": "CCM", "y":mongoController.INSTANCE.get_req_per_campus("financial services","CCM")}
            ],
            # Graduation Request 5
            [
                {"x": "CEM", "y":mongoController.INSTANCE.get_req_per_campus("graduation request","CEM")},
                {"x": "CSF", "y":mongoController.INSTANCE.get_req_per_campus("graduation request","CSF")},
                {"x": "CCM", "y":mongoController.INSTANCE.get_req_per_campus("graduation request","CCM")}
            ],
            # Library 6
            [
                {"x": "CEM", "y":mongoController.INSTANCE.get_req_per_campus("library","CEM")},
                {"x": "CSF", "y":mongoController.INSTANCE.get_req_per_campus("library","CSF")},
                {"x": "CCM", "y":mongoController.INSTANCE.get_req_per_campus("library","CCM")}
            ],
            # Photography 7
            [
                {"x": "CEM", "y":mongoController.INSTANCE.get_req_per_campus("photography","CEM")},
                {"x": "CSF", "y":mongoController.INSTANCE.get_req_per_campus("photography","CSF")},
                {"x": "CCM", "y":mongoController.INSTANCE.get_req_per_campus("photography","CCM")}
            ],
            # Program 8
            [
                {"x": "CEM", "y":mongoController.INSTANCE.get_req_per_campus("program","CEM")},
                {"x": "CSF", "y":mongoController.INSTANCE.get_req_per_campus("program","CSF")},
                {"x": "CCM", "y":mongoController.INSTANCE.get_req_per_campus("program","CCM")}
            ],
            # Social Service 9
            [
                {"x": "CEM", "y":mongoController.INSTANCE.get_req_per_campus("social service","CEM")},
                {"x": "CSF", "y":mongoController.INSTANCE.get_req_per_campus("social service","CSF")},
                {"x": "CCM", "y":mongoController.INSTANCE.get_req_per_campus("social service","CCM")}
            ],
        ]

        # Returns top 10 words which are relavant and its count.
        word_count = defaultdict(int)
        all_failed_intents = mongoController.INSTANCE.get_failed_intents()
        for failed_intent in all_failed_intents:
            text_tokens = word_tokenize(failed_intent['message'].lower())
            tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
            filtered_sentence = (" ").join(tokens_without_sw)
            for word in filtered_sentence.split():
                # word sanitize.
                filtered_word = ''.join(c for c in word if c.isalnum())
                if len(filtered_word) > 2:
                    word_count[filtered_word] += 1
        
        top_dict = Counter(word_count).most_common(5)
        # pprint(top_dict)
        # print(len(all_failed_intents))
        failed_intent_word_count = [
            {"text": key, "value": value} for key, value in top_dict
        ]

        return jsonify({
            'unique_users_per_month': unique_users_per_month,
            'no_missing_per_reqs': no_missing_per_reqs,
            'percentage_student_to_graduate': percentage_student_to_graduate,
            'entity_word_cloud': entity_word_cloud,
            'requirements_per_campus':requirements_per_campus,
            'failed_intent_word_count': failed_intent_word_count,
        })

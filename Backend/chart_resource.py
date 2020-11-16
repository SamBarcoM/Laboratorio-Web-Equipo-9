from flask import jsonify
from flask_restful import Resource

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

        return jsonify({
            'unique_users_per_month': unique_users_per_month,
            'no_missing_per_reqs': no_missing_per_reqs,
            'percentage_student_to_graduate': percentage_student_to_graduate,
        })

from odoo import fields, models


class school_student(models.Model):
    _inherit = 'school_student.school_student'

    student_full_name = fields.Char("Full Name")
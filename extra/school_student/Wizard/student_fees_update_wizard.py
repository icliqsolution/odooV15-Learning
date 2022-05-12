from odoo import api,models, fields

class StudentFeesUpdateWizard(models.TransientModel):
    _name = "student.fees.update.wizard"

    total_fees = fields.Float(string="Fees")


    def update_student_fees(self):
        print("Yeah successfully click on update_student_fees method....")

        self.env['school_student.school_student'].browse(self._context.get("active_ids")).update({'total_fees': self.total_fees})
        return True
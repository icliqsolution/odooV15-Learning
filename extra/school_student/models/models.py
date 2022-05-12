# -*- coding: utf-8 -*-
from lxml import etree
from odoo import models, fields, api, _, registry, tools as tl
from odoo.exceptions import UserError
import random

class student_test_fees(models.Model):
    _name = "student.test.fees"
    _table = "student_fees_testing"

    name = fields.Char("Fees")

class student_test(models.Model):
    _name = "student.test"

    name = fields.Char(string="Test")

class Address(models.Model):
    _name = "address"
    _rec_name = "street"

    street = fields.Char("street")
    street_one = fields.Char("street2")
    city = fields.Char("city")
    state = fields.Char("State")
    country = fields.Char("Country")
    Zip_code = fields.Char("Zip Code")


class log_access_attribute_class(models.Model):
    _name = "log.access.attribute.class"
    _log_access = False

    name = fields.Char(string="Name")

class school_student(models.Model):
    _name = 'school_student.school_student'
    _inherit = "address"
    _description = 'school_student.school_student'
    _rec_name = "name"
    _order = "name, id desc"
    # _log_access = False

    roll_number = fields.Char("Roll Number")
    name = fields.Char()
    school_id = fields.Many2one("school.profile", string="school", domain="[('school_type','=','public')]"
    )
    hobby_list = fields.Many2many("hobby", "school_hobby_rel","student_id","hobby_id",string="Hobbies")
    is_virtual_school = fields.Boolean(related="school_id.is_virtual_class",string="Is Virtual Class")
    school_address = fields.Text(related="school_id.address",string="Address")
    currency_id =fields.Many2one("res.currency",string="currency")
    student_fees = fields.Monetary(string="student fees", default="1900.00")
    total_fees = fields.Float(string="Total Fees")
    ref_id = fields.Reference([('school.profile', 'school'),
                              ('account.move','Invoice')] ,
                              string="Reference Field")

    active = fields.Boolean(string="Active",default=True)
    bdate = fields.Date(string="Date of Birth")
    student_age = fields.Char(string="Total Age")

    _sql_constraints = [
        ('total_fees_check','check(total_fees>100)','please provide other student name,Given name already exists.')
    ]

    @api.onchange("school_id")
    def _onchange_school_profile(self):
        currency_id = 0
        if self.school_id:
            currency_id = self.school_id.currency_id.id
        return {"domain":{'currency_id':[('id','=', currency_id)]}}

    @api.model
    def _change_roll_number(self):
        """This method is used to add roll number to the student profile."""
        for stud in self.search([('roll_number','=',False)]):
            stud.roll_number = "STD" + str(stud.id)

    def wiz_open(self):

        return {'type': 'ir.actions.act_window',
                'res_model': 'student.fees.update.wizard',
                'view_mode': 'form',
                'target': 'new'}  

    def custom_button_method(self):
        self.env.cr.execute("insert into school_student_school_student(name, active) values('from button click',True)")
        self.env.cr.commit()





        # print("Envi....",self.env)
        # print("user id....",self.env.uid)
        # print("current user....",self.env.user)
        # print("super user....",self.env.su)
        # print("company....",self.env.company)
        # print("companies....",self.env.companies)
        # print("lang....",self.env.lang)
        # print("cr....",self.env.cr)
        # print("Hello this is custom_button_method called by you...",self)
        self.total_fees = random.randint(1,1000)

        cli_commands = tl.config.options
        # print(cli_commands)
        # print(cli_commands.get("db_name"))
        # print(cli_commands.get("db_user"))
        # print(cli_commands.get("db_password"))
        # print(cli_commands.get("addons_path"))
        # print(cli_commands.get("dbfilter"))

    def custom_new_method(self, total_fees):
        self.total_fees = total_fees

    def custom_method(self):
        try:
            self.ensure_one()
            # print(self.name)
            # print(self.bdate)
            # print(self.school_id.name)
        except ValueError:
            pass


    
    # def fields_view_get(self,view_id=None, view_type='from', toolbar=False, submenu=False):
    # print("View id",view_id)
    # print("View Type",view_type)
    # print("toolbar",toolbar)
    # print("submenu",submenu)
        # res = super(school_student,self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        # print("Return Disc",res)
        # if view_type == "form":
        #     doc = etree.XML(res['arch'])
        #     name_field = doc.xpath("//field[@name='name']")
        #     if name_field:
                # Added one label in form view.
                # name_field[0].addnext(etree.Element('label', {'string':'Hello this is custom label from fields_view_get method'}))

            #override attribute
            # address_field = doc.xpath("//field[@name='school_address']")
            # if address_field:
            #     address_field[0].set("string", "Hello This is School Address.")
            #     address_field[0].set("nolabel", "0")


            # res['arch'] = etree.tostring(doc, encoding='unicode')

            # if view_type == 'tree':
            #     doc = etree.XML(res['arch'])
            #     school_field = doc.xpath("//field[@name='school_id']")
            #     if school_field:
                    # Added one field in tree view.
        #             school_field[0].addnext(etree.Element('field', {'string':'Total Fees',
        #                                                             'name': 'total_fees'}))
        #         res['arch'] = etree.tostring(doc, encoding='unicode')
        # return res
        

    @api.model
    def default_get(self, field_list=[]):
        print("field_list",field_list)
        rtn = super(school_student,self).default_get(field_list)
        print("Before Edit",rtn)
        rtn['active'] = True
        rtn['name'] = "dhara"
        rtn['total_fees'] = 4000.00
        print("return statement",rtn)
        return rtn

    @api.model
    def create(self, values):
        print("Before Edit Values ",values)
        values['active'] = True
        print("After Edit Values",values)
        print("Values of create method",values)
        print("self",self)
        rtn = super(school_student, self).create(values)
        # print("Return statement",rtn)
        return rtn    

    def write(self,values):
        rtn = super(school_student,self).write(values)
        print("Values ....",values)
        values['active'] = True
        rtn = super(school_student, self).write(values)
        print("Return data",rtn)
        return rtn  

    @api.returns('self',lambda value: value.id)     
    def copy(self,default={}):
        default['active'] = False
        print("Default values",default)
        print("self recordset",self)
        default['name']="copy ("+self.name+")"
        rtn = super(school_student,self).copy(default=default)
        print("return statemen",rtn)
        rtn.total_fees = 500
        return rtn 

    # def unlink(self):
    #     print("self statement",self)
    #     for stud in self:
    #         if stud.total_fees > 0:
    #             raise UserError(_("you can't delete this %s student profile"%stud.name))
    #     rtn = super(school_student, self).unlink()
    #     print("Return statement",rtn)
    #     return rtn                           
    
    # @api.model
    # def create(self, vals):
    #     rtn = super('school.profile', self).create(vals)
    #     if not rtn.school_list:
    #         raise UserError(_("student list is empty!"))
    #     return rtn     
    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

class schoolprofile(models.Model):
    _inherit = "school.profile"

    school_list = fields.One2many("school_student.school_student", "school_id",
                                string="school List")

    school_number = fields.Char("school code")


    # @api.model
    # def name_search(self, name, args=None, operator='ilike', limit=100):
    #     args = args or []
    #     print("Name",name)
    #     print("operator",operator)
    #     print("limit",limit)
    #     if name:
    #         records = self.search(['|','|',('name',operator,name),('email',operator,name),('school_number',operator,name),('school_type',operator,name)])
    #         return records.name_get()
    #     return super(schoolprofile, self).name_search(name=name, args=args, operator=operator, limit=limit) 


    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):

        args = args or []
        domain = []
        print("Name ",name)
        print("Args ",args)
        print("operator ",operator)
        print("limit ",limit)
        print("name_get_uid ",name_get_uid)
        if name:
            domain = ['|','|','|',('name',operator,name),('email',operator,name),
                     ('school_number',operator,name),('school_type',operator,name)]
        school_ids = self.search(domain+args, limit=limit)
        return school_ids.ids


    # @api.model
    # def create(self, vals):
    #     rtn = super("schoolprofile", self).create(vals)
    #     if not rtn.school_list:
    #         raise UserError(_("student list is empty!"))
    #     return rtn     


class Hobbies(models.Model):
    _name = "hobby"

    name = fields.Char("Hobby")    


class partner(models.Model):
    _inherit = "res.partner"

    @api.model
    def create(self, vals):

        print("User Env....",self.env)
        print("User Env....",self.env.user)
        print("User Env....",self.env.company)
        print("User Env....",self.env.companies)
        print("User Env....",self.env.context)

        print(" partner values ",vals)

        if 'company_id' not in vals:
            vals['company_id'] = self.env.company.id

        return super(partner, self).create(vals)

class SchoolStudent(models.Model):
    _inherit = 'school_student.school_student'

    parent_name = fields.Char("parent Name")

class Car(models.Model):
    _name = "car"

    name = fields.Char("car Name")
    price = fields.Float("Cost")

# class CarEngine(models.Model):
#     _name = "car.engine"
    # _inherits = {"car":"car_id"}

    # name = fields.Char("Car Engine Name")
    # car_id = fields.Many2one("car",string=Car)


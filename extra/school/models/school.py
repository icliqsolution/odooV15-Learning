from email.policy import default
from odoo import fields, models, api

class Schoolprofile(models.Model):
    _name = "school.profile"
    _rec_name = "name"
    



    def get_default_rank(self):
        if 1==1:
            return 200
        else:
            return 100

    def default_establish_date(self):
        return fields.Date.today() 


    name = fields.Char(string="School Name", help="This is school Name", default="Dhara") 
    email = fields.Char(string="Email")
    phone = fields.Char("Phone", default="12345")
    is_virtual_class = fields.Boolean(string="Virtual Class Support?")
    school_rank= fields.Integer(string="Rank" ,help="This is school rank", required=True, default=lambda lm:lm.get_default_rank())
    result = fields.Float(string="Result", help="This is tool tip", default=1.1)
    address = fields.Text(string="Address")
    estalish_date = fields.Date(string="Establish Date", default=fields.Date.today())
    open_date = fields.Datetime("Open Date", help="This is tooltip and" "select date and time.", default=lambda lm:lm.default_establish_date())
    school_type=fields.Selection([('public','Public School'),('private','Private School')],string="Type of School",)
    documents=fields.Binary(string='Documents')
    document_name = fields.Char(string="File Name")
    school_image = fields.Image(string="Upload School Image", max_width=100,
                                max_height=100)
    school_description = fields.Html(string="Description")
    auto_rank = fields.Integer(compute="_auto_rank_populate", string="AutoRank")

    # _sql_constraints = [
    #     ('unique_name','unique(name)','please provide other student name,Given name already exists.')
    # ]
    

    @api.depends("school_type")
    def _auto_rank_populate(self):
        for rec in self:
            if rec.school_type == "private":
                rec.auto_rank = 50
            elif rec.school_type == "public":
                rec.auto_rank =100
            else:  
                rec.auto_rank = 0  
    @api.model
    def name_create(self, name):
        rtn = self.create({"name":name, "email":"abc@gmail.com"})
        return rtn.name_get()[0]
        # print("self",self)
        # print("School Name",name)
        # rtn = self.create({'name':name})
        # print("rtn",rtn)
        # print("rtn.name_get()[0] ",rtn.name_get()[0])
        # return rtn.name_get()[0]         
    
    def name_get(self):
        student_list = []
        for school in self:
            name = school.name
            if school.school_type:
                name += " ({})".format(school.school_type)
            student_list.append((school.id, name))
        return student_list

    @api.model
    def create(self, vals):
        print("School Profile vals",vals)
        return super(Schoolprofile, self).create(vals)

    def write(self,vals):
        print("School Profile vals",vals)
        return super(Schoolprofile, self).create(vals)

    def SpecialCommand(self):

        student_obj = self.env['school_student.school_student']
        # stud_id = student_obj.create({'name':"student ONE", 'school_description':self.id})

        #parent model and child model.
        # school_id = self.create({"name":"Kapil"})
        # student_obj.create({"name":"Kapil Stu 11","school_id":school_id.id})
        # student_obj.create({"name":"Kapil Stu 22","school_id":school_id.id})
        # student_obj.create({"name":"Kapil Stu 33","school_id":school_id.id})
        # student_obj.create({"name":"Kapil Stu 44","school_id":school_id.id})
        # student_obj.create({"name":"Kapil Stu 55","school_id":school_id.id})

        #using special command
        # self.create({"name":"Babita School","school_list":[(0,0,{'name':"Babita Student 1", "total_fees":300}),
        #                                                    (0,0,{'name':"Babita Student 2", "total_fees":400}),
        #                                                    (0,0,{'name':"Babita Student 3", "total_fees":500}),
        #                                                    (0,0,{'name':"Babita Student 4", "total_fees":600}),
        #                                                    (0,0,{'name':"Babita Student 5", "total_fees":700})]})

    def SpecialCommand1(self):

             

        for student in self.school_list:
            student.name = student.name + "" +str(student.id)
            student.total_fees = 3600
            student.student_fees = 12000

        # vals = {'school_list':[]}
        # for student in self.school_list:
        #     vals['school_list'].append([1, student.id, {'name':student.name +" Name",
        #                                                 'total_fees':400,
        #                                                 "student_fees":4500}])

        # self.write(vals)

        # for student in self.school_list:
        #     student.update({'name':student.name + "1234567890",
        #                     'total_fees':251,
        #                     'student_fees':6500})
    
    def SpecialCommand3(self):
        self.write({'school_list':[(2, 237, False)]})

    def SpecialCommand4(self):
        self.write({'school_list':[(4, 237, 0)]})

    def SpecialCommand5(self):
        self.write({'school_list':[(5,0,0)]})




class TestseqPurpose(models.Model):
    _name = "test.seq.purpose"

    name = fields.Char("Name")

class TestForceSequence(models.Model):
    _name = "test.force.sequence"

    name = fields.Char("sequence Name")

   
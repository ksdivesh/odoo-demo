from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = "hospital.patient" #odoo will create table hospital_patient in the db
    _description = "Hospital Patient"
    
    name = fields.Char(string='Name')
    ref = fields.Char(string='Reference')
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    active = fields.Boolean(string='Active', default=True) #reserved field in odoo, for the Arhive & Unarchive option
    
from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = "hospital.patient" #odoo will create table hospital_patient in the db
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient"
    
    name = fields.Char(string='Name', tracking=True)
    ref = fields.Char(string='Reference', tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True)
    active = fields.Boolean(string='Active', default=True, tracking=True) #reserved field in odoo, for the Arhive & Unarchive option
    
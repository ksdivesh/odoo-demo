from datetime import date
from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"  # odoo will create table hospital_patient in the db
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient"
    _rec_name = "name"

    name = fields.Char(string='Name', tracking=True)
    date_of_birth = fields.Date(string='Date Of Birth')
    ref = fields.Char(string='Reference', tracking=True, default='Odoo Mates')
    age = fields.Integer(string='Age', compute='_compute_age', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')],
                              string='Gender', tracking=True, default='female')
    # reserved field in odoo, for the Arhive & Unarchive option
    active = fields.Boolean(string='Active', default=True, tracking=True)

    @api.depends('date_of_birth')
    def _compute_age(self):

        for rec in self:

            if rec.date_of_birth:
                today = date.today()
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0
